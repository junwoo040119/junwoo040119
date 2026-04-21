import argparse
import json
from pathlib import Path

from src.utils import load_json, save_json
from src.planner import generate_plan
from src.prompt_builder import build_simulation_prompt
from src.simulator import generate_future_image
from src.verifier import verify_simulation
from src.corrector import revise_plan


def run_pipeline(scenario_path: str) -> dict:
    scenario = load_json(scenario_path)

    plan = generate_plan(scenario)
    sim_prompt = build_simulation_prompt(scenario, plan)
    image_path = generate_future_image(sim_prompt, scenario["id"])
    verification = verify_simulation(scenario, plan, image_path)
    revised = revise_plan(scenario, plan, verification)

    result = {
        "scenario": scenario,
        "initial_plan": plan,
        "simulation_prompt": sim_prompt,
        "generated_image": image_path,
        "verification": verification,
        "revised_plan": revised,
    }

    output_path = Path("outputs") / f'{scenario["id"]}_result.json'
    save_json(result, output_path)
    return result


def main():
    parser = argparse.ArgumentParser(description="Run the multimodal plan verifier prototype.")
    parser.add_argument("--scenario", type=str, help="Path to a scenario JSON file")
    parser.add_argument("--all", action="store_true", help="Run all scenarios in the scenarios folder")
    args = parser.parse_args()

    if args.all:
        scenario_dir = Path("scenarios")
        paths = sorted(scenario_dir.glob("*.json"))
        for path in paths:
            result = run_pipeline(str(path))
            print(f'Finished: {path.name}')
            print(json.dumps(result, indent=2))
            print("-" * 60)
    elif args.scenario:
        result = run_pipeline(args.scenario)
        print(json.dumps(result, indent=2))
    else:
        parser.error("Provide --scenario <path> or --all")


if __name__ == "__main__":
    main()
