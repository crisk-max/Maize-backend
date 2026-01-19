def decide(symptoms, crop_stage, plant_part):
    if any("lesion" in s for s in symptoms):
        return {
            "category": "Disease",
            "diagnosis": "Disease symptoms detected",
            "confidence": 0.8,
            "evidence": symptoms,
            "actions": ["Consult agronomist"],
            "risk": "High"
        }

    if any("chewing" in s for s in symptoms):
        return {
            "category": "Pest",
            "diagnosis": "Pest damage detected",
            "confidence": 0.8,
            "evidence": symptoms,
            "actions": ["Check pest presence"],
            "risk": "High"
        }

    if any("purple" in s for s in symptoms):
        return {
            "category": "Nutrient Stress",
            "diagnosis": "Phosphorus deficiency (probable)",
            "confidence": 0.75,
            "evidence": symptoms,
            "actions": ["Check soil P levels"],
            "risk": "Low"
        }

    return {
        "category": "Healthy",
        "diagnosis": "No visible issues",
        "confidence": 0.9,
        "evidence": symptoms,
        "actions": ["Continue best practices"],
        "risk": "None"
    }
