# Hugging Face Generation Runbook

## 1) Set your Hugging Face token (PowerShell)

```powershell
$env:HF_TOKEN="hf_your_token_here"
```

## 2) Generate image

```powershell
python .\generate_hf_image.py
```

Expected output image:
- `output/gradient-descent-naturalist.png`

## 3) Build submission JSON (already done once, safe to rerun)

```powershell
python .\build_submission_json.py
```

Expected output JSON:
- `output/submission.json`

## 4) Upload both files to public CORS-enabled URLs

Submit in this exact order separated by one space:

`<public-image-url> <public-json-url>`

Example file mapping:
- image -> `output/gradient-descent-naturalist.png`
- json -> `output/submission.json`
