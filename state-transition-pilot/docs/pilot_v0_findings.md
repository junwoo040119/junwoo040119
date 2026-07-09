# Pilot v0 Findings

Date: 2026-07-09

Model/service: Pika 2.5 web generation

Samples: 5 generated videos from the `cut_vs_move` phenomenon

## Aggregate Result

| metric | value |
| --- | ---: |
| n | 5 |
| prompt understood rate | 1.000 |
| target state success rate | 0.400 |
| wrong opposite state rate | 0.000 |
| same scene preservation rate | 1.000 |
| perceptual quality rate | 1.000 |

Failure labels from the first annotation pass:

```text
none: 2
no_clear_position_change: 2
no_visible_cut_or_separation: 1
```

## Per-Sample Reading

| sample_id | target achieved | first-pass interpretation |
| --- | ---: | --- |
| `cut_move_apple_cut_pika_seed1` | 1 | Successful cut transition |
| `cut_move_apple_move_pika_seed1` | 0 | Apple remains intact, but position change is unclear |
| `cut_move_paper_cut_pika_seed1` | 1 | Successful cut transition |
| `cut_move_paper_move_pika_seed1` | 0 | Paper remains intact, but position change is minimal or unclear |
| `cut_move_cloth_cut_pika_seed1` | 0 | Scissors interact with cloth, but no visible cut/separation appears |

## Early Evidence

The strongest pilot signal is:

```text
prompt_understood = 1
perceptual_quality_ok = 1
same_scene_preserved = 1
target_state_achieved = 0
```

This pattern appears in 3 out of 5 samples. It suggests that the generated clips can be visually coherent and prompt-relevant while still failing the requested final state transition.

## Label Normalization Note

The first annotation pass used descriptive failure labels:

- `no_clear_position_change`
- `no_visible_cut_or_separation`

For cross-model or cross-seed comparison, these should be mapped into the rubric-level failure type `dynamics` when the object/action and perceptual quality are both adequate but the intended final state is not achieved.

Suggested normalized counts:

```text
none: 2
dynamics: 3
```

## What This Does And Does Not Prove

This v0 result is useful as an annotation/evaluation pipeline check. It does not yet satisfy the full Go / No-Go criteria because there is only one model, one seed, and one annotated human pass.

It does support the next step: generate the missing control videos and add either a second seed or second model, then test whether the same `prompt understood + visual quality OK + target state failed` pattern repeats.
