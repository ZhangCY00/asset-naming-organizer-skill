---
name: asset-naming-organizer
description: Professional asset audit and naming workflow for creative project folders. Use when Codex needs to inspect, classify, rename, or propose filenames for images, videos, vehicle/product references, storyboards, renderings, CAD/3D/model files, design source files, Unreal/AE/PSD projects, downloaded assets, or mixed media libraries; includes image recognition, OCR for labels/nameplates, video frame extraction, and privacy-safe GitHub-ready skill packaging.
---

# Asset Naming Organizer

Use this skill to turn mixed creative assets into a stable, searchable naming system. Prefer content-based names over capture dates, download defaults, or global numbering.

## Workflow

1. Audit before renaming.
   - List file types, sizes, timestamps, and folder structure.
   - Identify weak names such as `image`, `IMG_`, `ChatGPT Image`, `download`, `untitled`, `图片节点`, pure dates, duplicate suffixes, and vague `final` names.
   - Run `scripts/asset_inventory.py <folder>` when a quick inventory is useful.

2. Classify from broad to specific.
   - Use the pattern `subject_variant_asset-type_part-or-content_view-or-state_usage-or-version.ext`.
   - Omit fields that do not help distinguish the asset.
   - Do not add global `01`, `02`, `03` prefixes except for shot order, frame sequences, or process steps.

3. Inspect unknown visual assets.
   - Read the surrounding folder names and neighboring files first.
   - Use image vision for visible subject, color, type, angle, environment, and status.
   - Use OCR for vehicle nameplates, logos, UI labels, drawing annotations, slide titles, and product markings.
   - For vehicles, prefer confirmed folder/project context, visible badges/nameplates, steering-wheel logos, screen UI, then visual inference.
   - Mark uncertain facts with `unknown`, `suspected`, or `to-confirm`; do not invent exact models.

4. Inspect videos before naming.
   - Extract representative frames from the start, middle, end, and major visual changes.
   - If `ffmpeg` is available, use `scripts/asset_inventory.py <folder> --extract-video-frames`.
   - Name the video from the dominant subject/action and use extracted frames only as evidence.

5. Rename conservatively.
   - Preserve extensions.
   - Avoid path-sensitive characters: spaces, parentheses, `+`, `&`, `#`, long punctuation.
   - Use consistent spelling for the same subject across the folder.
   - If the folder is active production work, produce a rename plan first, then apply only after the user approves or clearly requested execution.

6. Protect privacy when packaging or publishing.
   - Do not include local user paths, project lists, downloaded-file listings, credentials, API keys, private URLs, client names, or proprietary source assets unless explicitly requested.
   - Publish only generic workflow files, scripts, and examples.
   - Run a sensitive-string scan before creating commits, archives, or GitHub uploads.

## Naming Standard

Read `references/naming-standard.md` for field order, controlled vocabulary, examples for vehicles/products/characters/scenes/storyboards/source files, and anti-patterns.

Core pattern:

```text
subject_variant_asset-type_part-or-content_view-or-state_usage-or-version.ext
```

Examples:

```text
EXLANTIX_ET_silver_exterior_front-45.jpg
EXLANTIX_ET_light-interior_rear-seat_lie-flat.jpg
hero_beige-outfit_character-sheet_three-view.png
golf-course_parking-lot_sunset_location-reference.png
story1_SB03_vehicle-exits-tight-space_topdown.png
building-facade_AiMOGA_PSD-source_layered_v04.psd
```

## Script

`scripts/asset_inventory.py` provides a deterministic first pass:

```bash
python scripts/asset_inventory.py <asset-folder>
python scripts/asset_inventory.py <asset-folder> --json
python scripts/asset_inventory.py <asset-folder> --extract-video-frames
```

Use the script output as orientation only. Final names still require content judgment, image recognition, OCR, or video-frame review when the file content is unclear.
