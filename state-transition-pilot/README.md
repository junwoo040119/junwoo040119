# State Transition Pilot

Small pilot for testing whether language-conditioned video models preserve the intended world-state transition, not just the surface action appearance.

## Goal

This pilot creates a small, laptop-friendly evidence loop for the topic:

> Do video generation models understand minimal language differences that imply different physical state transitions?

The first pass focuses on two phenomena:

- `cut_vs_move`
- `melt_vs_warm`

Generation can happen outside this repo through a web UI, API, or remote GPU. This folder handles prompt bookkeeping, human annotation, VLM-judge rubric design, and simple evaluation.

## Folder Layout

```text
state-transition-pilot/
  data/
    prompts.csv
    videos_manifest.csv
    human_annotations.csv
  rubrics/
    state_transition_judge.md
  scripts/
    make_annotation_sheet.py
    analyze_annotations.py
  videos/
    .gitkeep
  results/
    .gitkeep
```

## Quick Start

1. Generate videos from `data/prompts.csv` using any model or web UI.
2. Save videos locally under `videos/` or another path.
3. Fill `video_path`, `model`, and `seed` in `data/videos_manifest.csv`.
4. Create an annotation template:

```powershell
python scripts/make_annotation_sheet.py --manifest data/videos_manifest.csv --out data/human_annotations.csv
```

5. Fill `data/human_annotations.csv`.
6. Analyze results:

```powershell
python scripts/analyze_annotations.py --annotations data/human_annotations.csv --out results/summary.csv
```

## Annotation Labels

Use `1` for yes, `0` for no, and blank for not sure.

- `prompt_understood`: The requested object/action is visible.
- `target_state_achieved`: The intended final state appears.
- `wrong_state_transition`: The video moved toward the opposite minimal-pair state.
- `same_scene_preserved`: The object and scene remain coherent across the clip.
- `perceptual_quality_ok`: The video is clear enough to judge.

Set `overall_failure_type` to one of:

- `none`
- `comprehension`
- `perception`
- `dynamics`
- `scene_preservation`
- `ambiguous`

## Go / No-Go Evidence

The pilot is useful if it can show at least one of these:

- A repeatable state-transition failure across models or seeds.
- A case where perceptual quality is acceptable but target state is wrong.
- Human annotations agree enough to support a larger benchmark.
- The VLM-judge rubric can reproduce the human ranking for a small subset.

