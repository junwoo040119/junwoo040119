# Multimodal Plan Verifier

A minimal prototype that verifies LLM-generated plans using diffusion-style future simulation and a verification loop.

## What this does
1. Reads a natural-language scenario
2. Generates an initial plan
3. Builds a future-scene prompt
4. Generates a mock future image placeholder
5. Verifies whether the simulated future conflicts with the plan
6. Revises the plan if needed

## Modes
- **Mock mode (default)**: runs immediately without API keys
- **API mode (optional later)**: you can replace the stubs in `planner.py`, `simulator.py`, and `verifier.py`

## Quick start
```bash
python main.py --scenario scenarios/scenario_01.json
```

Run all scenarios:
```bash
python main.py --all
```

## Project structure
```text
multimodal-plan-verifier/
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── scenarios/
├── src/
│   ├── planner.py
│   ├── prompt_builder.py
│   ├── simulator.py
│   ├── verifier.py
│   ├── corrector.py
│   └── utils.py
└── outputs/
```

## Notes
- This repository is intentionally small and prototype-oriented.
- The current implementation uses rule-based mock logic so you can test the loop immediately.
- Replace the stubs with real model calls after you are ready.
