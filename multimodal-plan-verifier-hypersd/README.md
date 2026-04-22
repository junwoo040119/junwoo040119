# Multimodal Plan Verifier (Full Pipeline with Hyper-SD15)

This version is configured for a full local pipeline:
- Planner: Qwen/Qwen2.5-3B-Instruct
- Verifier: Qwen/Qwen2.5-VL-3B-Instruct
- Simulator: stable-diffusion-v1-5/stable-diffusion-v1-5 + ByteDance/Hyper-SD

Core loop:
Plan -> Simulate -> Verify -> Revise

## Install
```bash
pip install -r requirements.txt
```

## Run (Windows CMD)
```bat
set HF_DEVICE=cuda
set PLANNER_BACKEND=hf_local
set VERIFIER_BACKEND=hf_local
set SIMULATOR_BACKEND=diffusers

set HF_LLM_MODEL_ID=Qwen/Qwen2.5-3B-Instruct
set HF_VLM_MODEL_ID=Qwen/Qwen2.5-VL-3B-Instruct
set DIFFUSION_MODEL_ID=stable-diffusion-v1-5/stable-diffusion-v1-5
set HYPERSD_LORA_ID=ByteDance/Hyper-SD

set HF_LLM_MAX_NEW_TOKENS=96
set HF_VLM_MAX_NEW_TOKENS=96
set DIFFUSION_NUM_STEPS=8

python main.py --scenario scenarios/scenario_01.json
```

## Notes
- This package removes mock paths from planner / verifier / simulator.
- To reduce VRAM pressure, each model is unloaded after use.
- Hyper-SD LoRA is loaded on top of SD1.5.
