# State Transition Judge Rubric

Use this rubric for a VLM judge or for human annotation. The key question is not whether the clip looks realistic in general. The key question is whether the final world state matches the minimal language instruction.

## Input

- Prompt
- Expected final state
- Opposite minimal-pair state
- Video

## Required Judgments

Return a JSON object with these fields:

```json
{
  "prompt_understood": 1,
  "target_state_achieved": 1,
  "wrong_state_transition": 0,
  "same_scene_preserved": 1,
  "perceptual_quality_ok": 1,
  "overall_failure_type": "none",
  "confidence": 4,
  "rationale": "The apple is cut into visible pieces by the final frame."
}
```

Use `1` for yes, `0` for no, and `null` when the video cannot be judged.

## Label Definitions

### prompt_understood

Set to `1` if the main object and requested action family are visible. For example, an apple and cutting action appear for a cutting prompt.

### target_state_achieved

Set to `1` only if the expected final state is visible in the final part of the clip. Do not award this label for implied or partial state change.

### wrong_state_transition

Set to `1` if the clip instead matches the opposite minimal-pair state. For example, a `warm without melting` prompt receives melted butter.

### same_scene_preserved

Set to `1` if the main object identity, scene, and relevant object count remain coherent enough to evaluate the state transition.

### perceptual_quality_ok

Set to `1` if the video is clear enough to judge the state transition, even if it is not photorealistic.

## Failure Types

- `none`: No major failure.
- `comprehension`: Object or action family is missing or wrong.
- `perception`: Video is too distorted or unclear to judge.
- `dynamics`: Object/action appears, but the final physical state is wrong.
- `scene_preservation`: The scene or object identity changes too much to judge.
- `ambiguous`: Multiple interpretations remain plausible.

## Important Rule

If `perceptual_quality_ok = 1` and `prompt_understood = 1`, but `target_state_achieved = 0`, prefer `overall_failure_type = dynamics`. This is the most important failure class for this pilot.

