from fastapi import APIRouter, UploadFile, File, Form
from app.vision_ai import analyze_image_with_ai
from app.decision_engine import decide
from app.audit import log_audit

router = APIRouter()

@router.post("/analyze")
async def analyze(
    image: UploadFile = File(...),
    crop_stage: str = Form(...),
    plant_part: str = Form(...)
):
    image_bytes = await image.read()

    ai = analyze_image_with_ai(image_bytes)
    decision = decide(ai["visible_symptoms"], crop_stage, plant_part)

    result = {
        "crop": "Maize",
        "crop_stage": crop_stage,
        "plant_part": plant_part,
        "category": decision["category"],
        "primary_diagnosis": decision["diagnosis"],
        "confidence": decision["confidence"],
        "evidence": decision["evidence"],
        "recommended_actions": decision["actions"],
        "risk_level": decision["risk"],
        "disclaimer": "Advisory only"
    }

    log_audit(result)
    return result
