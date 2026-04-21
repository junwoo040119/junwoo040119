from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def generate_future_image(prompt: str, scenario_id: str) -> str:
    output_path = Path("outputs") / f"{scenario_id}_future.png"

    # Mock image generation: creates a placeholder image with text.
    img = Image.new("RGB", (1024, 576), color=(245, 245, 245))
    draw = ImageDraw.Draw(img)

    header = f"Mock future simulation: {scenario_id}"
    body = prompt[:220] + ("..." if len(prompt) > 220 else "")

    draw.rectangle((40, 40, 984, 536), outline=(60, 60, 60), width=3)
    draw.text((70, 80), header, fill=(20, 20, 20))
    draw.text((70, 150), body, fill=(40, 40, 40))

    # Add a simple visual cue depending on scenario id
    cue = {
        "scenario_01": "Cup falls from table edge",
        "scenario_02": "Cracked glass shatters",
        "scenario_03": "Stacked boxes collapse",
    }.get(scenario_id, "Uncertain future consequence")

    draw.text((70, 260), f"Simulated outcome: {cue}", fill=(120, 20, 20))
    img.save(output_path)
    return str(output_path)
