# Pilot v0: 5-Video Evaluation

This is the first runnable evaluation slice using the five Pika 2.5 videos that were successfully generated on 2026-07-09.

## Scope

Use only the rows currently listed in `data/videos_manifest.csv`.

Generated videos:

| sample_id | prompt_id | expected check |
| --- | --- | --- |
| `cut_move_apple_cut_pika_seed1` | `cut_move_apple_cut` | final apple should be visibly cut |
| `cut_move_apple_move_pika_seed1` | `cut_move_apple_move` | final apple should stay whole and move position |
| `cut_move_paper_cut_pika_seed1` | `cut_move_paper_cut` | final paper should be visibly split |
| `cut_move_paper_move_pika_seed1` | `cut_move_paper_move` | final paper should stay intact and move position |
| `cut_move_cloth_cut_pika_seed1` | `cut_move_cloth_cut` | final cloth should be visibly separated |

Missing from the intended 8-video first batch:

| prompt_id | reason |
| --- | --- |
| `cut_move_cloth_move` | Pika credits ran out before generation |
| `melt_warm_butter_melt` | Pika credits ran out before generation |
| `melt_warm_butter_warm` | Pika credits ran out before generation |

## Annotation Procedure

1. Open `docs/annotation_review_01.html` in a browser.
2. Watch each video at least once.
3. Fill `data/human_annotations.csv`.
4. Use `1` for yes, `0` for no, and blank only when unsure.

Most important labels:

- `prompt_understood`: object and requested action family are visible.
- `target_state_achieved`: final world state matches the prompt.
- `wrong_state_transition`: final state looks closer to the opposite minimal pair.
- `same_scene_preserved`: object and scene stay coherent enough to judge.
- `perceptual_quality_ok`: video is clear enough to evaluate.

Failure type rule:

- Use `dynamics` when the object/action are understandable and the clip is visually judgeable, but the final state is wrong.
- Use `comprehension` when the object or action family is missing.
- Use `perception` when visual quality prevents judgment.
- Use `scene_preservation` when object identity or scene continuity breaks.
- Use `ambiguous` when multiple readings remain plausible.
- Use `none` when there is no major failure.

## Run Summary

After annotation:

```powershell
python scripts/analyze_annotations.py --annotations data/human_annotations.csv --out results/pilot_v0_summary.csv
```

The useful early evidence pattern is:

```text
prompt_understood = 1
perceptual_quality_ok = 1
target_state_achieved = 0
overall_failure_type = dynamics
```

## Interpretation

This v0 slice is not enough for the full Go / No-Go criteria. It is enough to test whether the annotation schema can separate:

- prompt/object comprehension failure
- perceptual quality failure
- same-scene preservation failure
- actual state-transition or dynamics failure

If at least one row is confidently labeled as `dynamics`, the next step is to regenerate the missing control videos and add a second model or second seed.
