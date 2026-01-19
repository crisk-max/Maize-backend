def decide(symptoms, crop_stage, plant_part):
    symptoms_text = " ".join(symptoms).lower()

    # 1. Disease — STRICT RULE
    if any(word in symptoms_text for word in ["lesion", "pustule", "rot", "mold", "blight"]):
        return {
            "category": "Disease",
            "diagnosis": "Disease symptoms detected",
            "confidence": 0.85,
            "evidence": symptoms,
            "actions": [
                "Confirm disease with field agronomist",
                "Follow integrated disease management practices"
            ],
            "risk": "High"
        }

    # 2. Pest damage — STRICT RULE
    if any(word in symptoms_text for word in ["chewing", "holes", "frass", "dead heart"]):
        return {
            "category": "Pest Damage",
            "diagnosis": "Insect damage detected",
            "confidence": 0.85,
            "evidence": symptoms,
            "actions": [
                "Inspect whorl and stem for pests",
                "Apply IPM practices if infestation confirmed"
            ],
            "risk": "High"
        }

    # 3. Nutrient deficiency / physiological stress
    if any(word in symptoms_text for word in ["purple", "yellow", "pale", "discoloration"]):
        return {
            "category": "Nutrient / Physiological Stress",
            "diagnosis": "Likely phosphorus deficiency or temperature-related stress",
            "confidence": 0.75,
            "evidence": symptoms,
            "actions": [
                "Check soil nutrient status",
                "Avoid unnecessary pesticide sprays",
                "Stress often reduces as crop establishes"
            ],
            "risk": "Low"
        }

    # 4. Healthy
    return {
        "category": "Healthy",
        "diagnosis": "No visible stress symptoms",
        "confidence": 0.9,
        "evidence": symptoms,
        "actions": [
            "Continue recommended agronomic practices"
        ],
        "risk": "None"
    }
