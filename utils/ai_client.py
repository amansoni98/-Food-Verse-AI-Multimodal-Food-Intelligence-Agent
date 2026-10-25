"""
AI Client wrapper for Food Verse AI.
Integrates with Google Gemini API (gemini-1.5-flash / gemini-1.5-pro) with robust fallback to mock analysis.
"""
import os
import json
from PIL import Image
from utils.mock_data import (
    get_mock_food_analysis,
    get_mock_freshness_analysis,
    get_mock_hygiene_analysis,
    get_mock_recipes,
    get_mock_meal_plan
)

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def configure_genai(api_key):
    if not HAS_GENAI or not api_key:
        return False
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        print(f"Error configuring genai: {e}")
        return False

def analyze_food_image(image: Image.Image, api_key: str = ""):
    """
    Analyzes food image using Gemini multimodal or falls back to mock analysis.
    """
    if configure_genai(api_key):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = """
            Analyze this food/meal image and return a JSON object with EXACTLY the following keys:
            {
                "dish_name": "string",
                "cuisine": "string",
                "portion_size": "string",
                "calories": integer,
                "protein_g": float,
                "carbs_g": float,
                "fats_g": float,
                "fiber_g": float,
                "health_score": integer (1-100),
                "ingredients": ["string"],
                "allergen_alerts": ["string"],
                "nutrition_insights": "string",
                "recommendations": "string"
            }
            Return ONLY valid JSON.
            """
            response = model.generate_content([prompt, image])
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            print(f"Gemini API error (Food Analysis), falling back: {e}")

    # Fallback to mock data
    return get_mock_food_analysis()

def analyze_freshness_image(image: Image.Image, item_name: str, api_key: str = ""):
    """
    Analyzes freshness/spoilage of perishable item using Gemini or falls back to mock.
    """
    if configure_genai(api_key):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"""
            Analyze this image of a perishable food item ({item_name}) for freshness and spoilage.
            Return a JSON object with EXACTLY the following keys:
            {{
                "item_name": "{item_name}",
                "freshness_stage": "Fresh" or "Moderately Fresh" or "Spoiled",
                "confidence_score": float (0.0 to 1.0),
                "safety_status": "Safe to consume" or "Consume within 24h" or "Discard immediately",
                "shelf_life_remaining": "string",
                "surface_texture_assessment": "string",
                "discoloration_notes": "string",
                "mold_inspection": "string",
                "storage_tips": "string"
            }}
            Return ONLY valid JSON.
            """
            response = model.generate_content([prompt, image])
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            print(f"Gemini API error (Freshness), falling back: {e}")

    return get_mock_freshness_analysis(item_name)

def analyze_hygiene_media(image_or_video_desc: str, api_key: str = ""):
    """
    Analyzes kitchen hygiene compliance.
    """
    if configure_genai(api_key):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = """
            Analyze this commercial kitchen environment for food safety and hygiene compliance.
            Return a JSON object with EXACTLY the following keys:
            {
                "overall_compliance_score": integer (0-100),
                "facility_status": "string",
                "indicators": {
                    "chef_hat_hairnet": {"status": "string", "score": integer, "notes": "string"},
                    "glove_usage": {"status": "string", "score": integer, "notes": "string"},
                    "sanitization_state": {"status": "string", "score": integer, "notes": "string"},
                    "cross_contamination_hazard": {"status": "string", "score": integer, "notes": "string"}
                },
                "violations": [
                    {
                        "severity": "Low" or "Medium" or "High",
                        "category": "string",
                        "description": "string",
                        "corrective_action": "string"
                    }
                ],
                "summary": "string"
            }
            Return ONLY valid JSON.
            """
            response = model.generate_content([prompt])
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            print(f"Gemini API error (Hygiene), falling back: {e}")

    return get_mock_hygiene_analysis()

def generate_smart_recipes(ingredients: list, api_key: str = ""):
    """
    Generates smart recipes based on pantry ingredients.
    """
    if configure_genai(api_key):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            ing_str = ", ".join(ingredients)
            prompt = f"""
            Given these available pantry ingredients: {ing_str}, generate 2 nutritious, creative recipes.
            Return a JSON array of objects with EXACTLY the following structure:
            [
                {{
                    "recipe_name": "string",
                    "cooking_time": "string",
                    "difficulty": "Easy" or "Medium" or "Hard",
                    "calories": integer,
                    "protein": "string",
                    "carbs": "string",
                    "fats": "string",
                    "description": "string",
                    "steps": ["string"],
                    "substitutions": "string"
                }}
            ]
            Return ONLY valid JSON.
            """
            response = model.generate_content([prompt])
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            print(f"Gemini API error (Recipes), falling back: {e}")

    return get_mock_recipes(ingredients)

def generate_ai_meal_plan(profile: dict, api_key: str = ""):
    """
    Generates 7-day meal plan and shopping list based on user profile.
    """
    if configure_genai(api_key):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"""
            Generate a 7-day adaptive meal plan and automated grocery shopping list for a user with the following profile:
            Age: {profile.get('age')}, Gender: {profile.get('gender')}, Weight: {profile.get('weight_kg')}kg,
            Activity: {profile.get('activity_level')}, Goal: {profile.get('goal')},
            Dietary Constraint: {profile.get('diet')}, Target Calories: {profile.get('target_calories')} kcal/day.

            Return a JSON object with EXACTLY the following structure:
            {{
                "meal_plan": [
                    {{
                        "day": "Monday",
                        "breakfast": {{"name": "string", "calories": int, "protein": "string", "carbs": "string", "fat": "string"}},
                        "lunch": {{"name": "string", "calories": int, "protein": "string", "carbs": "string", "fat": "string"}},
                        "dinner": {{"name": "string", "calories": int, "protein": "string", "carbs": "string", "fat": "string"}},
                        "snacks": {{"name": "string", "calories": int, "protein": "string", "carbs": "string", "fat": "string"}}
                    }}
                ],
                "shopping_list": {{
                    "Produce": ["string"],
                    "Proteins & Dairy": ["string"],
                    "Pantry & Grains": ["string"]
                }}
            }}
            Return ONLY valid JSON for all 7 days (Monday through Sunday). Return ONLY valid JSON.
            """
            response = model.generate_content([prompt])
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            return json.loads(text.strip())
        except Exception as e:
            print(f"Gemini API error (Meal Plan), falling back: {e}")

    return get_mock_meal_plan(profile)
