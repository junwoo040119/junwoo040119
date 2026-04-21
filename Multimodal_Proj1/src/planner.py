from typing import Dict, Any


def generate_plan(scenario: Dict[str, Any]) -> Dict[str, str]:
    context = scenario.get("context", "")
    question = scenario.get("question", "")
    text = f"{context} {question}".lower()

    # Mock planner: intentionally optimistic in risky scenarios
    if "cup" in text or "glass cup" in text:
        return {
            "action": "Push the cup slightly to the right.",
            "expected_outcome": "The cup will remain stable on the table.",
            "planner_reasoning": "A small movement seems manageable."
        }

    if "cracked glass door" in text or ("glass door" in text and "crack" in text):
        return {
            "action": "Push the door strongly to open it.",
            "expected_outcome": "The door will open successfully.",
            "planner_reasoning": "A stronger push may open the door quickly."
        }

    if "boxes" in text or "stacked" in text or "bottom box" in text:
        return {
            "action": "Pull the bottom box out carefully.",
            "expected_outcome": "The target box will be removed without issue.",
            "planner_reasoning": "A careful pull may work."
        }

    return {
        "action": "Proceed with the requested action.",
        "expected_outcome": "The action will likely succeed.",
        "planner_reasoning": "No obvious risk was identified from the text alone."
    }
