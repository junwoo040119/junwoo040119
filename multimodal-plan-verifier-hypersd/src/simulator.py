from pathlib import Path
import torch
from diffusers import StableDiffusionPipeline

from config import (
    OUTPUT_DIR,  # 🔥 추가
    SIMULATOR_BACKEND,
    DIFFUSION_MODEL_ID,
    HYPERSD_LORA_ID,
    DIFFUSION_DEVICE,
    DIFFUSION_NUM_STEPS,
)
from src.utils import clear_memory

_PIPE = None


def _get_diffusion_pipe():
    global _PIPE
    if _PIPE is not None:
        return _PIPE

    dtype = torch.float16 if DIFFUSION_DEVICE == "cuda" else torch.float32

    _PIPE = StableDiffusionPipeline.from_pretrained(
        DIFFUSION_MODEL_ID,
        torch_dtype=dtype,
        safety_checker=None,
        requires_safety_checker=False,
    )
    _PIPE = _PIPE.to(DIFFUSION_DEVICE)

    # Hyper-SD LoRA 적용
    _PIPE.load_lora_weights(
        HYPERSD_LORA_ID,
        weight_name="Hyper-SD15-8steps-lora.safetensors"
    )
    _PIPE.fuse_lora()

    try:
        _PIPE.enable_attention_slicing()
    except Exception:
        pass

    return _PIPE


def unload_simulator():
    global _PIPE
    _PIPE = None
    clear_memory()


def generate_future_image(prompt: str, scenario_id: str) -> str:
    if SIMULATOR_BACKEND != "diffusers":
        raise ValueError(f"Unsupported SIMULATOR_BACKEND: {SIMULATOR_BACKEND}")

    pipe = _get_diffusion_pipe()

    output_path = OUTPUT_DIR / f"{scenario_id}_future.png"

    image = pipe(
        prompt=prompt,
        num_inference_steps=DIFFUSION_NUM_STEPS,
        guidance_scale=0.0,
    ).images[0]

    image.save(output_path)

    print(f"🖼️ Image saved to: {output_path.resolve()}")

    return str(output_path)