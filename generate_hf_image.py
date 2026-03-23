import os
from pathlib import Path
from huggingface_hub import InferenceClient
from PIL import Image


def main() -> None:
    root = Path(__file__).resolve().parent
    out_dir = root / "output"
    out_dir.mkdir(exist_ok=True)

    prompt_file = os.getenv("PROMPT_FILE", "prompt.txt")
    negative_prompt_file = os.getenv("NEGATIVE_PROMPT_FILE", "negative_prompt.txt")
    output_image_name = os.getenv("OUTPUT_IMAGE_NAME", "gradient-descent-naturalist.png")

    prompt = (root / prompt_file).read_text(encoding="utf-8").strip()
    negative_prompt = (root / negative_prompt_file).read_text(encoding="utf-8").strip()

    token = os.getenv("HF_TOKEN")
    if not token:
        raise RuntimeError("HF_TOKEN environment variable is not set.")

    # Allow model override from env while keeping a practical default.
    model = os.getenv("HF_MODEL", "black-forest-labs/FLUX.1-schnell")
    client = InferenceClient(token=token)

    image = client.text_to_image(
        prompt=prompt,
        model=model,
        negative_prompt=negative_prompt,
        width=1280,
        height=1600,
        num_inference_steps=8,
    )

    if not isinstance(image, Image.Image):
        raise RuntimeError("Hugging Face did not return a PIL image.")

    output_path = out_dir / output_image_name
    image.save(output_path, format="PNG")

    print(f"Saved image: {output_path}")
    print(f"Model: {model}")


if __name__ == "__main__":
    main()
