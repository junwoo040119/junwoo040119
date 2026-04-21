from typing import Dict, Any


def build_simulation_prompt(scenario: Dict[str, Any], plan: Dict[str, str]) -> str:
    context = scenario.get("context", "")
    action = plan.get("action", "")
    return (
        "Create a realistic future scene that shows the physical consequence of the action. "
        f"Context: {context} "
        f"Action: {action} "
        "Focus on the most physically plausible result."
    )
