from typing import Dict, Any
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from config import (
    PLANNER_BACKEND,
    HF_LLM_MODEL_ID,
    HF_LLM_MAX_NEW_TOKENS,
    HF_DEVICE,
    HF_LOW_CPU_MEM_USAGE,
)
from src.utils import extract_first_json_object, clear_memory

_PLANNER_MODEL = None
_PLANNER_TOKENIZER = None


def _get_planner_model():
    global _PLANNER_MODEL, _PLANNER_TOKENIZER
    if _PLANNER_MODEL is not None and _PLANNER_TOKENIZER is not None:
        return _PLANNER_MODEL, _PLANNER_TOKENIZER

    _PLANNER_TOKENIZER = AutoTokenizer.from_pretrained(HF_LLM_MODEL_ID)
    _PLANNER_MODEL = AutoModelForCausalLM.from_pretrained(
        HF_LLM_MODEL_ID,
        torch_dtype="auto",
        device_map="auto" if HF_DEVICE == "cuda" else None,
        low_cpu_mem_usage=HF_LOW_CPU_MEM_USAGE,
    )

    if HF_DEVICE != "cuda":
        _PLANNER_MODEL = _PLANNER_MODEL.to(HF_DEVICE)

    _PLANNER_MODEL.eval()
    return _PLANNER_MODEL, _PLANNER_TOKENIZER


def unload_planner():
    global _PLANNER_MODEL, _PLANNER_TOKENIZER
    _PLANNER_MODEL = None
    _PLANNER_TOKENIZER = None
    clear_memory()


def _generate_plan_hf_local(scenario: Dict[str, Any]) -> Dict[str, str]:
    model, tokenizer = _get_planner_model()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a planning assistant for physically grounded scenarios. "
                "Return only valid JSON with exactly these keys: "
                "action, expected_outcome, planner_reasoning."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Context: {scenario.get('context', '')}\n"
                f"Question: {scenario.get('question', '')}\n"
                "Be concise. Output only JSON."
            ),
        },
    ]

    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt")
    if HF_DEVICE == "cuda":
        inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=HF_LLM_MAX_NEW_TOKENS,
            do_sample=False,
            eos_token_id=tokenizer.eos_token_id,
        )

    generated_ids = outputs[0][inputs["input_ids"].shape[1]:]
    generated_text = tokenizer.decode(generated_ids, skip_special_tokens=True)

    parsed = extract_first_json_object(generated_text)
    parsed.setdefault("action", "")
    parsed.setdefault("expected_outcome", "")
    parsed.setdefault("planner_reasoning", "")
    return parsed


def generate_plan(scenario: Dict[str, Any]) -> Dict[str, str]:
    if PLANNER_BACKEND == "hf_local":
        return _generate_plan_hf_local(scenario)
    raise ValueError(f"Unsupported PLANNER_BACKEND: {PLANNER_BACKEND}")
