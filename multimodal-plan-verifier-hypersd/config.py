from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

HF_DEVICE = os.getenv("HF_DEVICE", "cuda")

PLANNER_BACKEND = os.getenv("PLANNER_BACKEND", "hf_local").lower()
HF_LLM_MODEL_ID = os.getenv("HF_LLM_MODEL_ID", "Qwen/Qwen2.5-3B-Instruct")
HF_LLM_MAX_NEW_TOKENS = int(os.getenv("HF_LLM_MAX_NEW_TOKENS", "96"))

VERIFIER_BACKEND = os.getenv("VERIFIER_BACKEND", "hf_local").lower()
HF_VLM_MODEL_ID = os.getenv("HF_VLM_MODEL_ID", "Qwen/Qwen2.5-VL-3B-Instruct")
HF_VLM_MAX_NEW_TOKENS = int(os.getenv("HF_VLM_MAX_NEW_TOKENS", "96"))

SIMULATOR_BACKEND = os.getenv("SIMULATOR_BACKEND", "diffusers").lower()
DIFFUSION_MODEL_ID = os.getenv("DIFFUSION_MODEL_ID", "stable-diffusion-v1-5/stable-diffusion-v1-5")
HYPERSD_LORA_ID = os.getenv("HYPERSD_LORA_ID", "ByteDance/Hyper-SD")
DIFFUSION_DEVICE = os.getenv("DIFFUSION_DEVICE", "cuda")
DIFFUSION_NUM_STEPS = int(os.getenv("DIFFUSION_NUM_STEPS", "12"))

HF_LOW_CPU_MEM_USAGE = os.getenv("HF_LOW_CPU_MEM_USAGE", "true").lower() == "true"
