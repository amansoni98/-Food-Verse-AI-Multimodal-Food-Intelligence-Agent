"""
Mock data and fallback responses for Food Verse AI - Multimodal Food Intelligence Agent.
Provides realistic structured JSON outputs for food recognition, freshness, hygiene, recipes, and meal plans.
"""

def get_mock_food_analysis(image_name="Default Meal"):
    return {
        "dish_name": "Grilled Salmon Bowl with Quinoa & Roasted Asparagus",
        "cuisine": "Mediterranean / Fusion",
        "portion_size": "350g (Standard Serving)",
        "calories": 540,
        "protein_g": 42.5,
        "carbs_g": 48.0,
        "fats_g": 19.2,
        "fiber_g": 8.5,
        "health_score": 92,
        "ingredients": ["Atlantic Salmon (180g)", "Organic Quinoa (100g)", "Asparagus (80g)", "Extra Virgin Olive Oil", "Lemon Herb Dressing", "Sesame Seeds"],
        "allergen_alerts": ["Fish (Salmon)", "Sesame"],
        "nutrition_insights": "High in Omega-3 fatty acids, complete high-biological-value protein, and complex low-glycemic carbohydrates. Excellent for cardiovascular health and muscle recovery.",
        "recommendations": "Great post-workout or heart-healthy dinner option. Pair with a glass of water or green tea."
    }

def get_mock_freshness_analysis(item_name="Produce / Meat"):
    return {
        "item_name": item_name,
        "freshness_stage": "Fresh",
        "confidence_score": 0.94,
        "safety_status": "Safe to consume",
        "shelf_life_remaining": "3 to 5 days when stored properly",
        "surface_texture_assessment": "Firm turgor pressure, natural vibrant pigmentation, no signs of mushiness or water-soaking.",
        "discoloration_notes": "Uniform natural color distribution. Zero enzymatic browning or yellowing observed.",
        "mold_inspection": "Zero fungal hyphae or mycelium growth detected on surface or stem junctions.",
        "storage_tips": "Store in the refrigerator crisper drawer at 34°F - 38°F (1°C - 3°C) in a breathable container or produce bag."
    }

def get_mock_hygiene_analysis():
    return {
        "overall_compliance_score": 88,
        "facility_status": "Satisfactory / Pass with minor corrective notes",
        "indicators": {
            "chef_hat_hairnet": {"status": "Compliant", "score": 100, "notes": "All kitchen personnel wearing proper hair containment."},
            "glove_usage": {"status": "Mostly Compliant", "score": 85, "notes": "Gloves worn during plating; one instance of touch contamination noted."},
            "sanitization_state": {"status": "Compliant", "score": 90, "notes": "Work surfaces clean, sanitizer bucket present with correct ppm concentration."},
            "cross_contamination_hazard": {"status": "Warning", "score": 75, "notes": "Raw poultry cutting board located too close to ready-to-eat salad prep area."}
        },
        "violations": [
            {
                "severity": "Medium",
                "category": "Cross-Contamination Risk",
                "description": "Raw poultry cutting board placed adjacent to vegetable prep station without physical partition.",
                "corrective_action": "Relocate raw meat prep station to designated meat zone and maintain minimum 2-meter separation from ready-to-eat foods."
            },
            {
                "severity": "Low",
                "category": "PPE Protocol",
                "description": "Cook touched apron while handling fresh garnishes without immediate glove sanitization.",
                "corrective_action": "Reinforce hand sanitation protocols and glove change frequency after touching personal clothing."
            }
        ],
        "summary": "Commercial kitchen demonstrates strong overall hygiene practices. Immediate correction required regarding raw meat proximity to vegetable prep."
    }

def get_mock_recipes(ingredients_list):
    ingredients_str = ", ".join(ingredients_list) if ingredients_list else "Chicken Breast, Broccoli, Garlic, Olive Oil"
    return [
        {
            "recipe_name": f"Garlic Herb Sautéed {ingredients_list[0] if ingredients_list else 'Protein'} with Roasted Greens",
            "cooking_time": "20 minutes",
            "difficulty": "Easy",
            "calories": 420,
            "protein": "38g",
            "carbs": "12g",
            "fats": "22g",
            "description": f"A quick, nutrient-dense skillet meal utilizing available pantry staples: {ingredients_str}.",
            "steps": [
                "Prep all available ingredients by washing and chopping into bite-sized pieces.",
                "Heat extra virgin olive oil in a skillet over medium-high heat.",
                "Sauté primary protein until golden brown and fully cooked (internal temp 165°F).",
                "Add aromatics (garlic/onions) and greens, tossing for 3-4 minutes until tender-crisp.",
                "Season with sea salt, black pepper, and a squeeze of fresh lemon juice before serving."
            ],
            "substitutions": "Substitute olive oil with avocado oil; swap greens with spinach or kale."
        },
        {
            "recipe_name": f"Nourishing {ingredients_list[1] if len(ingredients_list) > 1 else 'Vegetable'} Bowl",
            "cooking_time": "30 minutes",
            "difficulty": "Medium",
            "calories": 480,
            "protein": "30g",
            "carbs": "45g",
            "fats": "18g",
            "description": "A balanced, fiber-rich bowl combining wholesome carbohydrates with lean protein and healthy fats.",
            "steps": [
                "Simmer grains or base ingredients in vegetable broth until fluffy.",
                "Roast vegetables on a baking sheet at 400°F (200°C) for 20 minutes with olive oil and herbs.",
                "Combine base, roasted vegetables, and protein in a serving bowl.",
                "Drizzle with house vinaigrette or tahini dressing."
            ],
            "substitutions": "Use quinoa, brown rice, or cauliflower rice as the base."
        }
    ]

def get_mock_meal_plan(profile):
    goal = profile.get("goal", "Fat Loss")
    diet = profile.get("diet", "Balanced")
    calories = profile.get("target_calories", 2000)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = []

    for i, day in enumerate(days):
        meal_plan.append({
            "day": day,
            "breakfast": {
                "name": "Greek Yogurt Parfait with Berries & Almonds",
                "calories": int(calories * 0.25),
                "protein": "24g", "carbs": "35g", "fat": "12g"
            },
            "lunch": {
                "name": "Grilled Chicken & Quinoa Salad with Lemon Vinaigrette",
                "calories": int(calories * 0.35),
                "protein": "42g", "carbs": "40g", "fat": "16g"
            },
            "dinner": {
                "name": "Baked Salmon with Sweet Potato Mash & Roasted Asparagus",
                "calories": int(calories * 0.35),
                "protein": "45g", "carbs": "45g", "fat": "18g"
            },
            "snacks": {
                "name": "Apple Slices with 2 tbsp Peanut Butter & Protein Shake",
                "calories": int(calories * 0.05),
                "protein": "25g", "carbs": "20g", "fat": "8g"
            }
        })

    shopping_list = {
        "Produce": ["Spinach (2 bags)", "Avocados (4)", "Asparagus (1 bunch)", "Apples (1 bag)", "Sweet Potatoes (3 lbs)", "Lemons (4)", "Garlic (1 bulb)"],
        "Proteins & Dairy": ["Chicken Breast (3 lbs)", "Atlantic Salmon Fillets (2 lbs)", "Greek Yogurt (32 oz)", "Eggs (1 dozen)", "Whey Protein Isolate"],
        "Pantry & Grains": ["Organic Quinoa (1 lb)", "Extra Virgin Olive Oil", "Almonds (1 bag)", "Natural Peanut Butter", "Sea Salt & Black Pepper"]
    }

    return meal_plan, shopping_list
