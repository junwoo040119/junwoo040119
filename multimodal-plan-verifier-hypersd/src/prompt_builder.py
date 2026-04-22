from typing import Dict, Any


def build_simulation_prompt(scenario: Dict[str, Any], plan: Dict[str, str]) -> str:
    context = scenario.get("context", "")
    action = plan.get("action", "")
    scenario_id = scenario.get("id", "")

    risk_map = {
        "scenario_01": (
            "a glass cup near the edge of a table, "
            "after being pushed to the right, tipping over or falling off the edge"
        ),
        "scenario_02": (
            "a cracked glass door, after being pushed strongly, "
            "showing visible fracture expansion or shattering"
        ),
        "scenario_03": (
            "unstable stacked heavy boxes, after the bottom box is pulled, "
            "showing collapse and falling objects"
        ),
    }

    risk_description = risk_map.get(
        scenario_id,
        "the most physically plausible future consequence of the action"
    )

    return (
        "Realistic future scene, photorealistic, physically plausible, "
        "clear visible consequence of the action. "
        f"Scene: {context} "
        f"Action: {action} "
        f"Show: {risk_description}. "
        "Emphasize instability, motion aftermath, and visible physical outcome."
    )