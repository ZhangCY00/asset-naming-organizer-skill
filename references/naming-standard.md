# Asset Naming Standard

## Principles

- Name from broad to specific: subject, variant, asset type, part/content, view/state, usage/version.
- Prefer reusable categories over project-specific numbering.
- Keep names short enough to scan but detailed enough to search.
- Use one spelling for the same subject everywhere.
- Use `unknown`, `suspected`, or `to-confirm` for uncertain information.
- Use shot numbers only where order is meaningful: `SB01`, `frame_0001`, `step01`.

## Generic Pattern

```text
subject_variant_asset-type_part-or-content_view-or-state_usage-or-version.ext
```

Field guidance:

| Field | Meaning | Examples |
| --- | --- | --- |
| `subject` | Product, vehicle, character, place, brand, project object | `EXLANTIX_ET`, `OMODA_4`, `hero`, `golf-course`, `medical-robot` |
| `variant` | Color, material, trim, outfit, version | `silver`, `blue`, `light-interior`, `v02`, `beige-outfit` |
| `asset-type` | Exterior, interior, render, model, source, storyboard, prop, scene | `exterior`, `interior`, `render`, `FBX-model`, `PSD-source`, `storyboard` |
| `part-or-content` | Specific area, object, feature, or action | `front-face`, `tail`, `center-screen`, `wireless-charging`, `base` |
| `view-or-state` | Camera angle, status, lighting, action state | `front-45`, `side`, `topdown`, `sunset`, `lie-flat`, `expanded` |
| `usage-or-version` | Reference, final, draft, source, export, version | `reference`, `final`, `draft`, `source`, `v01`, `to-confirm` |

Use lowercase English when publishing a generic library. In Chinese working folders, the same order can be used with Chinese terms.

## Controlled Type Words

Visual:

- `exterior`
- `interior`
- `character-sheet`
- `product-design`
- `prop-design`
- `location-reference`
- `render`
- `KV`
- `storyboard`
- `storyboard-table`
- `composite-reference`

Video:

- `animatic`
- `reference-video`
- `demo-video`
- `motion-graphics`
- `frame-grab`

3D and source:

- `FBX-model`
- `Blender-source`
- `Maya-source`
- `Max-source`
- `CAD-model`
- `UE-project`
- `UE-asset`
- `UE-map`
- `PSD-source`
- `AI-source`
- `AE-project`
- `texture`
- `material`

Documents and archives:

- `PPT-deck`
- `PDF-reference`
- `brief`
- `spreadsheet`
- `archive`

## Vehicle Assets

Pattern:

```text
model_color-or-trim_exterior-or-interior_part_view-or-state.ext
```

Examples:

```text
EXLANTIX_ET_silver_exterior_front-45.jpg
EXLANTIX_ET_silver_exterior_rear-straight.jpg
EXLANTIX_ET_light-interior_rear-seat_lie-flat.jpg
EXLANTIX_ET_dark-interior_cockpit_dual-screen-ambient-light.jpg
support-vehicle_interior_cockpit_rear-seat-view_reference.png
unknown-vehicle_silver_exterior_rear-45_to-confirm.jpg
```

Vehicle identification priority:

1. User or project brief.
2. Visible badge/nameplate, tail label, steering-wheel logo, screen UI, or plate text.
3. Existing folder and neighboring file context.
4. Visual inference only when marked as `suspected` or `to-confirm`.

## Product, Robot, and Prop Assets

Pattern:

```text
subject_variant_asset-type_part_view-or-state.ext
```

Examples:

```text
medical-robot_white_exterior_front-standing.png
traffic-police-robot_v02_base-design_front-45.png
robot-dog_black_topology_communication-link.png
charging-pile_silver-black_product-design_front.png
handheld-terminal_black_prop-design_expanded.png
```

## Characters and Wardrobe

Pattern:

```text
character_outfit-or-role_asset-type_state.ext
```

Examples:

```text
hero_beige-outfit_character-sheet_three-view.png
support-man_gray-outfit_character-sheet_three-view.png
nurse-robot_blue-white-uniform_costume-design_v02.png
assistant-character_business-outfit_half-body_to-confirm.png
```

## Scenes, Architecture, and KV

Pattern:

```text
place-or-brand_space-or-theme_time-or-mood_asset-type_version.ext
```

Examples:

```text
golf-course_parking-lot_sunset_location-reference.png
office-building_facade_night_render.png
exhibition-hall_entrance_day_location-reference.jpg
robot-scene-KV_city-plaza_night_PSD-source_v03.psd
```

## Storyboards and Video Production

Shot numbers are allowed because order is meaningful.

Pattern:

```text
story-or-project_shot_content_camera-or-view.ext
```

Examples:

```text
story1_SB01_interior-autonomous-driving_POV.png
story1_SB02_center-screen-route_closeup.png
story1_SB03_vehicle-exits-tight-space_topdown.png
story1_animatic_incomplete.mp4
story1_storyboard-table.png
```

Frame-grabs:

```text
source-video_frame-grab_00m05s.png
parking-lot-reference-video_frame-grab_00m12s.png
```

## Source and Engineering Files

Pattern:

```text
project-or-subject_module_software-or-format_usage_version.ext
```

Examples:

```text
traffic-police-robot_base_FBX-model_editable_v02.fbx
medical-robot_head_Blender-source_v01.blend
robot-expression_UI-motion_AE-project_source_v03.aep
building-facade_AiMOGA_PSD-source_layered_v04.psd
vehicle-masterclass_scene_UE-project_source.uproject
```

## Weak Names to Replace

Replace vague or platform-generated names:

```text
image.png
IMG_0001.jpg
ChatGPT Image 2026...
download.mp4
untitled.psd
final_final.psd
new folder.zip
20260603-135501.jpg
```

Use content names instead:

```text
golf-course_parking-lot_sunset_location-reference.png
EXLANTIX_ET_dark-interior_cockpit_dual-screen-ambient-light.jpg
hero_beige-outfit_character-sheet_three-view.png
story1_SB03_vehicle-exits-tight-space_topdown.png
```

## Privacy Checklist

Before publishing a skill, archive, or GitHub repo:

- Remove local paths and usernames.
- Remove project scans, inventory outputs, and private client/project names unless intentionally public.
- Remove downloaded-file listings and source URLs.
- Remove API keys, access credentials, account names, private emails, and internal hostnames.
- Keep only generic examples and reusable scripts.
