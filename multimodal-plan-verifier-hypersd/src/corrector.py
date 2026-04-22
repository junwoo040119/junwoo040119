from typing import Dict, Any


def revise_plan(
    scenario: Dict[str, Any],
    plan: Dict[str, Any],
    verification: Dict[str, Any]
) -> Dict[str, Any]:
    original_action = plan.get("action", "")
    observed_outcome = verification.get("observed_outcome", "")
    risk_detected = verification.get("risk_detected", False)
    conflict_with_plan = verification.get("conflict_with_plan", False)
    reason = verification.get("reason", "")

    # 안전하다고 판단되면 기존 계획 유지
    if not risk_detected and not conflict_with_plan:
        return {
            "revised_action": original_action,
            "final_decision": "safe",
            "revision_reason": "The simulated future is consistent with the original plan.",
        }

    scenario_id = scenario.get("id", "")

    # 시나리오별로 더 자연스러운 대안 제안
    if scenario_id == "scenario_01":
        revised_action = (
            "Do not push the cup toward the table edge. "
            "Move it inward to a more stable position away from the edge first."
        )
    elif scenario_id == "scenario_02":
        revised_action = (
            "Do not push the cracked glass door strongly. "
            "Reduce force, inspect the damage first, or choose a safer alternative path."
        )
    elif scenario_id == "scenario_03":
        revised_action = (
            "Do not pull the bottom box directly. "
            "Stabilize the stack first or remove upper boxes before moving the lower one."
        )
    else:
        revised_action = (
            "Avoid the original action and choose a safer alternative based on the observed risk."
        )

    revision_reason = (
        f"The original plan was revised because the simulated future showed: {observed_outcome}. "
        f"Verification reason: {reason}"
    )

    return {
        "revised_action": revised_action,
        "final_decision": "unsafe",
        "revision_reason": revision_reason,
    }