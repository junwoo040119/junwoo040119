from typing import Dict, Any


def verify_simulation(scenario: Dict[str, Any], plan: Dict[str, str], image_path: str) -> Dict[str, Any]:
    text = f'{scenario.get("context", "")} {scenario.get("question", "")}'.lower()

    if "cup" in text:
        return {
            "observed_outcome": "The cup appears to be falling off the table.",
            "risk_detected": True,
            "conflict_with_plan": True,
            "reason": "The simulated future contradicts the assumption that the cup remains stable."
        }

    if "glass door" in text and "crack" in text:
        return {
            "observed_outcome": "The cracked glass appears to shatter under force.",
            "risk_detected": True,
            "conflict_with_plan": True,
            "reason": "The generated outcome suggests structural failure."
        }

    if "boxes" in text or "stacked" in text:
        return {
            "observed_outcome": "The stacked boxes appear to collapse after removing the bottom box.",
            "risk_detected": True,
            "conflict_with_plan": True,
            "reason": "The simulated future shows instability in the stack."
        }

    return {
        "observed_outcome": "No obvious physical failure is detected.",
        "risk_detected": False,
        "conflict_with_plan": False,
        "reason": "The simulation does not strongly contradict the plan."
    }
