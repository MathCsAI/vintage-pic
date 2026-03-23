import json
import os
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out_dir = root / "output"
    out_dir.mkdir(exist_ok=True)

    prompt_file = os.getenv("PROMPT_FILE", "prompt.txt")
    negative_prompt_file = os.getenv("NEGATIVE_PROMPT_FILE", "negative_prompt.txt")
    output_json_name = os.getenv("OUTPUT_JSON_NAME", "submission.json")

    prompt = (root / prompt_file).read_text(encoding="utf-8").strip()
    negative_prompt = (root / negative_prompt_file).read_text(encoding="utf-8").strip()

    full_prompt = (
        f"{prompt}\\n\\nNegative prompt: {negative_prompt}\\n"
        "Parameters: width=1280, height=1600, num_inference_steps=8"
    )

    submission = {
        "prompt": full_prompt,
        "model": "black-forest-labs/FLUX.1-schnell (Hugging Face Inference API)",
        "concept": "Gradient descent optimization",
        "tradition_name": "Victorian botanical illustration (Curtis's Botanical Magazine tradition)",
        "tradition_period": "1827-1890",
        "tradition_approach": "Applied plate-style specimen isolation, fine pen-and-ink contour and stipple, restrained hand-colored chromolithographic washes, Latin scientific labeling, and exploded anatomical insets to embed iterative descent steps in period natural-history grammar.",
    }

    # Optional attribution field: set to True if you want your email attribution.
    # submission["publish_email"] = True

    out_path = out_dir / output_json_name
    out_path.write_text(json.dumps(submission, ensure_ascii=True, indent=2), encoding="utf-8")
    print(f"Saved JSON: {out_path}")


if __name__ == "__main__":
    main()
