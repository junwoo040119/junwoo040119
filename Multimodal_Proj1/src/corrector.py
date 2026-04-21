from typing import Dict, Any


def revise_plan(scenario: Dict[str, Any], plan: Dict[str, str], verification: Dict[str, Any]) -> Dict[str, str]:
    if verification.get("conflict_with_plan", False):
        text = f'{scenario.get("context", "")} {scenario.get("question", "")}'.lower()

        if "cup" in text:
            return {
                "revised_action": "Do not push the cup to the right. Move it inward away from the edge.",
                "final_decision": "unsafe"
            }

        if "glass door" in text and "crack" in text:
            return {
                "revised_action": "Do not push the cracked door strongly. Inspect it or use an alternative route.",
                "final_decision": "unsafe"
            }

        if "boxes" in text or "stacked" in text:
            return {
                "revised_action": "Do not pull the bottom box. Stabilize the stack first or unload top boxes.",
                "final_decision": "unsafe"
            }

        return {
            "revised_action": "Avoid the original action and gather more information first.",
            "final_decision": "unsafe"
        }

    return {
        "revised_action": plan.get("action", "Proceed."),
        "final_decision": "safe"
    }
