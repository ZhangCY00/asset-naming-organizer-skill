#!/usr/bin/env python3
"""Audit creative asset folders before content-based renaming.

This script does not rename files. It summarizes file types, finds weak names,
and can extract representative video frames when ffmpeg is installed.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path


MEDIA_EXTS = {
    ".png", ".jpg", ".jpeg", ".webp", ".tga", ".exr", ".hdr", ".gif",
    ".mp4", ".mov", ".avi", ".webm", ".mp3", ".wav",
    ".fbx", ".obj", ".glb", ".blend", ".max", ".mb", ".stp", ".step",
    ".uproject", ".uasset", ".umap", ".psd", ".psb", ".ai", ".aep",
    ".pptx", ".pdf", ".docx", ".xlsx", ".zip", ".7z", ".rar",
}

VIDEO_EXTS = {".mp4", ".mov", ".avi", ".webm"}

SKIP_DIRS = {
    ".git", "node_modules", ".next", "dist", "build", "Library", "Saved",
    "Intermediate", "DerivedDataCache", "__pycache__",
}

WEAK_NAME_PATTERNS = [
    r"^image(?:\s*\(\d+\))?$",
    r"^img[_-]?\d+",
    r"^dsc[_-]?\d+",
    r"^download",
    r"^untitled",
    r"^new\s*folder",
    r"^final(?:[_\s-]*final)+",
    r"^chatgpt image",
    r"^generated image",
    r"^screen\s*shot",
    r"^screenshot",
    r"^\d{8}[-_]\d{6}$",
    r"^\d{13,}$",
]


@dataclass
class FileRecord:
    path: str
    extension: str
    size_bytes: int
    weak_name: bool
    reasons: list[str]


def iter_files(root: Path, include_all: bool) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file():
            continue
        if include_all or path.suffix.lower() in MEDIA_EXTS:
            files.append(path)
    return files


def weak_name_reasons(path: Path) -> list[str]:
    stem = path.stem.strip().lower()
    reasons: list[str] = []
    for pattern in WEAK_NAME_PATTERNS:
        if re.search(pattern, stem, flags=re.IGNORECASE):
            reasons.append(f"weak-name:{pattern}")
    if path.name.count(".") > 1 and path.suffix.lower() in path.stem.lower():
        reasons.append("possible-duplicate-extension")
    if len(stem) <= 2:
        reasons.append("too-short")
    if re.fullmatch(r"[\d_\-\s]+", stem):
        reasons.append("numeric-only")
    return reasons


def build_inventory(root: Path, include_all: bool) -> dict:
    files = iter_files(root, include_all)
    records: list[FileRecord] = []
    by_ext: Counter[str] = Counter()
    by_dir: Counter[str] = Counter()
    weak: list[FileRecord] = []

    for file in files:
        rel = file.relative_to(root).as_posix()
        ext = file.suffix.lower() or "[no extension]"
        reasons = weak_name_reasons(file)
        record = FileRecord(
            path=rel,
            extension=ext,
            size_bytes=file.stat().st_size,
            weak_name=bool(reasons),
            reasons=reasons,
        )
        records.append(record)
        by_ext[ext] += 1
        parent = file.parent.relative_to(root).as_posix()
        by_dir[parent if parent != "." else "[root]"] += 1
        if reasons:
            weak.append(record)

    return {
        "root": str(root),
        "file_count": len(records),
        "extensions": dict(by_ext.most_common()),
        "directories": dict(by_dir.most_common(30)),
        "weak_names": [asdict(item) for item in weak[:200]],
        "records": [asdict(item) for item in records],
    }


def print_report(data: dict) -> None:
    print(f"Root: {data['root']}")
    print(f"Files: {data['file_count']}")
    print("\nExtensions:")
    for ext, count in data["extensions"].items():
        print(f"  {ext}: {count}")
    print("\nTop directories:")
    for folder, count in data["directories"].items():
        print(f"  {folder}: {count}")
    print("\nWeak names:")
    if not data["weak_names"]:
        print("  none")
    for item in data["weak_names"][:50]:
        print(f"  {item['path']} | {', '.join(item['reasons'])}")


def extract_video_frames(root: Path, output_dir: Path, seconds: list[int]) -> None:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg not found; install ffmpeg or skip --extract-video-frames.")
    output_dir.mkdir(parents=True, exist_ok=True)
    videos = [p for p in iter_files(root, include_all=False) if p.suffix.lower() in VIDEO_EXTS]
    for video in videos:
        safe_stem = re.sub(r"[^A-Za-z0-9._-]+", "_", video.stem).strip("_") or "video"
        for sec in seconds:
            out = output_dir / f"{safe_stem}_frame-grab_{sec:04d}s.jpg"
            cmd = [
                ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
                "-ss", str(sec), "-i", str(video),
                "-frames:v", "1", str(out),
            ]
            subprocess.run(cmd, check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit creative asset folders.")
    parser.add_argument("folder", type=Path, help="Folder to audit")
    parser.add_argument("--json", action="store_true", help="Print JSON")
    parser.add_argument("--include-all", action="store_true", help="Include every file extension")
    parser.add_argument("--extract-video-frames", action="store_true", help="Extract representative video frames with ffmpeg")
    parser.add_argument("--frames-dir", type=Path, default=None, help="Output directory for frame grabs")
    parser.add_argument("--seconds", default="0,5,15", help="Comma-separated timestamps in seconds")
    args = parser.parse_args()

    root = args.folder.resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Folder not found: {root}")

    data = build_inventory(root, include_all=args.include_all)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print_report(data)

    if args.extract_video_frames:
        seconds = [int(part.strip()) for part in args.seconds.split(",") if part.strip()]
        frames_dir = args.frames_dir or (root / "_asset_frame_grabs")
        extract_video_frames(root, frames_dir, seconds)
        print(f"\nFrame grabs written to: {frames_dir}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
