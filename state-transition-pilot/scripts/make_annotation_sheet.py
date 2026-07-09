import argparse
import csv
from pathlib import Path


FIELDNAMES = [
    "annotator_id",
    "sample_id",
    "prompt_id",
    "model",
    "seed",
    "video_path",
    "prompt_understood",
    "target_state_achieved",
    "wrong_state_transition",
    "same_scene_preserved",
    "perceptual_quality_ok",
    "overall_failure_type",
    "confidence",
    "comment",
]


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_sheet(rows: list[dict[str, str]], out_path: Path, annotator_id: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "annotator_id": annotator_id,
                    "sample_id": row["sample_id"],
                    "prompt_id": row["prompt_id"],
                    "model": row["model"],
                    "seed": row["seed"],
                    "video_path": row["video_path"],
                    "prompt_understood": "",
                    "target_state_achieved": "",
                    "wrong_state_transition": "",
                    "same_scene_preserved": "",
                    "perceptual_quality_ok": "",
                    "overall_failure_type": "",
                    "confidence": "",
                    "comment": "",
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="data/videos_manifest.csv")
    parser.add_argument("--out", default="data/human_annotations.csv")
    parser.add_argument("--annotator-id", default="annotator_01")
    args = parser.parse_args()

    rows = read_manifest(Path(args.manifest))
    write_sheet(rows, Path(args.out), args.annotator_id)
    print(f"Wrote {len(rows)} annotation rows to {args.out}")


if __name__ == "__main__":
    main()

