import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path


BINARY_FIELDS = [
    "prompt_understood",
    "target_state_achieved",
    "wrong_state_transition",
    "same_scene_preserved",
    "perceptual_quality_ok",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_binary(value: str) -> int | None:
    value = value.strip()
    if value == "":
        return None
    if value in {"0", "1"}:
        return int(value)
    raise ValueError(f"Expected 0, 1, or blank; got {value!r}")


def mean_binary(rows: list[dict[str, str]], field: str) -> str:
    values = [parse_binary(row[field]) for row in rows]
    values = [value for value in values if value is not None]
    if not values:
        return ""
    return f"{sum(values) / len(values):.3f}"


def summarize_group(group_key: tuple[str, str], rows: list[dict[str, str]]) -> dict[str, str]:
    phenomenon, model = group_key
    failure_counts = Counter(row["overall_failure_type"].strip() or "blank" for row in rows)
    return {
        "phenomenon": phenomenon,
        "model": model,
        "n": str(len(rows)),
        "prompt_understood_rate": mean_binary(rows, "prompt_understood"),
        "target_state_success_rate": mean_binary(rows, "target_state_achieved"),
        "wrong_state_rate": mean_binary(rows, "wrong_state_transition"),
        "same_scene_rate": mean_binary(rows, "same_scene_preserved"),
        "perceptual_quality_rate": mean_binary(rows, "perceptual_quality_ok"),
        "failure_type_counts": "; ".join(f"{k}:{v}" for k, v in sorted(failure_counts.items())),
    }


def prompt_to_phenomenon(prompt_id: str) -> str:
    if prompt_id.startswith("cut_move"):
        return "cut_vs_move"
    if prompt_id.startswith("melt_warm"):
        return "melt_vs_warm"
    return "unknown"


def write_summary(rows: list[dict[str, str]], out_path: Path) -> None:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[(prompt_to_phenomenon(row["prompt_id"]), row["model"])].append(row)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "phenomenon",
        "model",
        "n",
        "prompt_understood_rate",
        "target_state_success_rate",
        "wrong_state_rate",
        "same_scene_rate",
        "perceptual_quality_rate",
        "failure_type_counts",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for key in sorted(grouped):
            writer.writerow(summarize_group(key, grouped[key]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotations", default="data/human_annotations.csv")
    parser.add_argument("--out", default="results/summary.csv")
    args = parser.parse_args()

    rows = read_rows(Path(args.annotations))
    write_summary(rows, Path(args.out))
    print(f"Wrote summary to {args.out}")


if __name__ == "__main__":
    main()

