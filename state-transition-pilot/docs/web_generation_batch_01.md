# Web Generation Batch 01

Use this sheet to generate the first 8 videos manually in a web text-to-video model.

## Setup

- Use one video generation service for the whole batch.
- Keep the same settings for every prompt when possible.
- Recommended duration: 4-6 seconds.
- Recommended aspect ratio: 16:9 or 1:1, but keep it consistent.
- If the service has a seed field, use `1`.
- If there is no seed field, leave seed as `1` in the manifest and note that the service did not expose a seed.
- Save each downloaded video using the exact filename shown below.

After downloading videos, place them in:

```text
state-transition-pilot/videos/
```

Then update `data/videos_manifest.csv`:

- Replace `modelA` with the real model or service name.
- Fill `generated_at` with the date.
- Add notes for missing seed controls, watermarks, low quality, or failed generations.

## Batch Prompts

### 1. cut_move_apple_cut

Save as:

```text
videos/cut_move_apple_cut_modelA_seed1.mp4
```

Prompt:

```text
A close-up video of a whole apple on a wooden cutting board. A knife cuts the apple into clearly separated pieces. The final frame shows the apple visibly cut.
```

Expected final state:

```text
The intact apple becomes visibly cut into pieces.
```

### 2. cut_move_apple_move

Save as:

```text
videos/cut_move_apple_move_modelA_seed1.mp4
```

Prompt:

```text
A close-up video of a whole apple on a wooden cutting board. A hand moves the apple to the side without cutting it. The final frame shows the apple still whole and intact.
```

Expected final state:

```text
The apple remains intact but changes position.
```

### 3. cut_move_paper_cut

Save as:

```text
videos/cut_move_paper_cut_modelA_seed1.mp4
```

Prompt:

```text
A video of a single sheet of paper on a desk. Scissors cut the paper into two separated pieces. The final frame shows the paper split apart.
```

Expected final state:

```text
The sheet is visibly cut into two pieces.
```

### 4. cut_move_paper_move

Save as:

```text
videos/cut_move_paper_move_modelA_seed1.mp4
```

Prompt:

```text
A video of a single sheet of paper on a desk. A hand slides the paper to another position without cutting it. The final frame shows one intact sheet.
```

Expected final state:

```text
The sheet remains intact but changes position.
```

### 5. melt_warm_butter_melt

Save as:

```text
videos/melt_warm_butter_melt_modelA_seed1.mp4
```

Prompt:

```text
A close-up video of a small cube of butter in a pan. Heat melts the butter until it becomes a visible liquid puddle. The final frame shows melted butter.
```

Expected final state:

```text
Solid butter becomes visibly melted or liquid.
```

### 6. melt_warm_butter_warm

Save as:

```text
videos/melt_warm_butter_warm_modelA_seed1.mp4
```

Prompt:

```text
A close-up video of a small cube of butter in a pan. The butter is warmed gently but does not melt. The final frame shows the butter still solid.
```

Expected final state:

```text
Solid butter stays solid while becoming warm.
```

### 7. melt_warm_chocolate_melt

Save as:

```text
videos/melt_warm_chocolate_melt_modelA_seed1.mp4
```

Prompt:

```text
A close-up video of a piece of chocolate on a plate. Heat melts the chocolate until it becomes soft and glossy liquid. The final frame shows melted chocolate.
```

Expected final state:

```text
Solid chocolate becomes visibly melted or liquid.
```

### 8. melt_warm_chocolate_warm

Save as:

```text
videos/melt_warm_chocolate_warm_modelA_seed1.mp4
```

Prompt:

```text
A close-up video of a piece of chocolate on a plate. The chocolate is warmed gently without melting. The final frame shows the chocolate still solid.
```

Expected final state:

```text
Solid chocolate stays solid while becoming warm.
```

## After Generation

Run:

```powershell
python scripts/make_annotation_sheet.py --manifest data/videos_manifest.csv --out data/human_annotations.csv --annotator-id junwoo
```

Then fill `data/human_annotations.csv` while watching the videos.

The most important evidence pattern is:

```text
prompt_understood = 1
perceptual_quality_ok = 1
target_state_achieved = 0
overall_failure_type = dynamics
```

