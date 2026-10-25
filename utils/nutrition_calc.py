"""
Nutrition and TDEE Calculator using the Mifflin-St Jeor Equation.
Computes BMR, TDEE, target calories based on goals, and macro breakdowns.
"""

def calculate_bmr_tdee(age, gender, weight_kg, height_cm, activity_level, goal):
    """
    Calculates BMR using Mifflin-St Jeor Equation and TDEE based on activity multiplier.
    """
    # Mifflin-St Jeor Equation:
    # Men: BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) + 5
    # Women: BMR = 10 * weight(kg) + 6.25 * height(cm) - 5 * age(y) - 161
    if gender.lower() in ["male", "m"]:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    multipliers = {
        "Sedentary (little or no exercise)": 1.2,
        "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
        "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
        "Very active (hard exercise/sports 6-7 days a week)": 1.725,
        "Extra active (very hard exercise/physical job)": 1.9
    }

    mult = multipliers.get(activity_level, 1.2)
    tdee = bmr * mult

    # Adjust for goal
    if "Fat Loss" in goal or "Weight Loss" in goal:
        target_calories = tdee - 500  # 500 kcal deficit
    elif "Muscle Gain" in goal or "Bulking" in goal:
        target_calories = tdee + 300  # 300 kcal surplus
    else:
        target_calories = tdee      # Maintenance

    return int(bmr), int(tdee), int(target_calories)

def calculate_macros(target_calories, diet_type):
    """
    Calculates protein, carbs, and fats in grams based on calorie target and diet type.
    """
    if "Keto" in diet_type:
        protein_pct = 0.25
        fat_pct = 0.70
        carb_pct = 0.05
    elif "High Protein" in diet_type or "Muscle Gain" in diet_type:
        protein_pct = 0.35
        fat_pct = 0.25
        carb_pct = 0.40
    elif "Low Carb" in diet_type:
        protein_pct = 0.30
        fat_pct = 0.45
        carb_pct = 0.25
    else: # Balanced / Vegan / Vegetarian / Diabetic-Friendly
        protein_pct = 0.30
        fat_pct = 0.30
        carb_pct = 0.40

    protein_g = (target_calories * protein_pct) / 4.0
    carb_g = (target_calories * carb_pct) / 4.0
    fat_g = (target_calories * fat_pct) / 9.0

    return {
        "protein_g": int(protein_g),
        "carbs_g": int(carb_g),
        "fat_g": int(fat_g)
    }
