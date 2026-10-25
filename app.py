"""
Food Verse AI – Multimodal Food Intelligence Agent
Skill Wallet Capstone Project 3
Category: Generative AI | Nutrition, Freshness & Kitchen Safety
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import io

from utils.ai_client import (
    analyze_food_image,
    analyze_freshness_image,
    analyze_hygiene_media,
    generate_smart_recipes,
    generate_ai_meal_plan
)
from utils.nutrition_calc import calculate_bmr_tdee, calculate_macros

# Page Configuration
st.set_page_config(
    page_title="Food Verse AI — Multimodal Food Intelligence",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    .badge-fresh {
        background-color: #DEF7EC;
        color: #03543F;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
    }
    .badge-moderate {
        background-color: #FEF08A;
        color: #713F12;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
    }
    .badge-spoiled {
        background-color: #FDE8E8;
        color: #9B1C1C;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3B82F6;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Configuration & Persona
with st.sidebar:
    st.image("https://img.icons8.com/color/96/kawaii-sushi.png", width=70)
    st.markdown("### **Food Verse AI**")
    st.markdown("*Multimodal Food Intelligence & Kitchen Safety Agent*")
    st.markdown("---")

    st.markdown("### 🔑 API Configuration")
    api_key_input = st.text_input("Google Gemini API Key", type="password", placeholder="AIzaSy...")
    if api_key_input:
        st.success("API Key Active (Live Mode)")
        active_api_key = api_key_input
    else:
        st.info("Using Standalone Demo Mode (Mock AI)")
        active_api_key = ""

    st.markdown("---")
    st.markdown("### 🧭 Intelligence Pillars")
    selected_tab = st.radio(
        "Navigate Modules",
        [
            "🍎 Food Recognition & Nutrition",
            "🥑 Freshness & Spoilage Diagnostic",
            "🛡️ Kitchen Hygiene Compliance",
            "👨‍🍳 Smart Recipe Assistant",
            "📅 Personalized Meal Planner"
        ]
    )

    st.markdown("---")
    st.markdown("### 📊 Project Metadata")
    st.markdown("**Category:** Generative AI")
    st.markdown("**Platform ID:** `6ac4ca021dcde6d7857c169a`")
    st.markdown("**Version:** 3.0 Production-Ready")

# Main Header
st.markdown('<p class="main-header">🍽️ Food Verse AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced Multimodal Food Intelligence, Freshness Diagnostics, Kitchen Hygiene & Smart Nutrition Ecosystem</p>', unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 1: FOOD RECOGNITION & NUTRITION AUDIT (EPIC 2)
# ----------------------------------------------------
if selected_tab == "🍎 Food Recognition & Nutrition Nutrition" or selected_tab == "🍎 Food Recognition & Nutrition":
    st.markdown("### 🍎 Food Recognition & Nutrition Audit")
    st.write("Upload a meal or dish photo to perform instant multimodal recognition, macro breakdown, allergen detection, and health scoring.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 📸 Upload Meal Image")
        uploaded_file = st.file_uploader("Choose an image (JPG, PNG, WEBP)", type=["jpg", "jpeg", "png", "webp"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Meal", use_container_width=True)
        else:
            st.info("No image uploaded. Click 'Run Demo Analysis' below to test with a sample gourmet salmon bowl.")
            if st.button("🚀 Run Demo Analysis", type="primary"):
                image = None
            else:
                image = None

    with col2:
        st.markdown("#### 🔬 AI Vision & Nutrient Breakdown")
        if st.button("🔍 Analyze Meal Composition", type="primary") or uploaded_file or 'demo_run' in st.session_state:
            with st.spinner("Analyzing dish features, ingredients, and nutritional profile..."):
                sample_img = image if uploaded_file else Image.new('RGB', (300, 300), color=(73, 109, 137))
                analysis = analyze_food_image(sample_img, active_api_key)

            st.markdown(f"### **{analysis.get('dish_name')}**")
            st.caption(f"Cuisine: {analysis.get('cuisine')} | Portion: {analysis.get('portion_size')}")

            # Metrics Row
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Calories", f"{analysis.get('calories')} kcal")
            m2.metric("Protein", f"{analysis.get('protein_g')}g")
            m3.metric("Carbs", f"{analysis.get('carbs_g')}g")
            m4.metric("Fats", f"{analysis.get('fats_g')}g")

            # Health Score & Fiber
            col_a, col_b = st.columns(2)
            col_a.metric("Fiber", f"{analysis.get('fiber_g')}g")
            health_score = analysis.get('health_score', 85)
            col_b.metric("Health Score (1-100)", f"{health_score} / 100", delta="Excellent" if health_score > 80 else "Good")

            # Macro Breakdown Chart
            st.markdown("#### 📊 Macronutrient Distribution")
            macro_df = pd.DataFrame({
                "Macro": ["Protein", "Carbohydrates", "Fats"],
                "Grams": [analysis.get('protein_g'), analysis.get('carbs_g'), analysis.get('fats_g')]
            })
            fig = px.pie(macro_df, names="Macro", values="Grams", hole=0.4, color_discrete_sequence=["#3B82F6", "#10B981", "#F59E0B"])
            fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=220)
            st.plotly_chart(fig, use_container_width=True)

            # Ingredients & Allergens
            st.markdown("#### 🥗 Detected Ingredients")
            st.write(", ".join(analysis.get('ingredients', [])))

            st.markdown("#### ⚠️ Allergen Alerts")
            allergens = analysis.get('allergen_alerts', [])
            if allergens:
                for alg in allergens:
                    st.warning(f"Contains allergen: **{alg}**")
            else:
                st.success("No major allergens detected.")

            st.markdown("#### 💡 Nutritionist Insights")
            st.info(analysis.get('nutrition_insights'))
        else:
            st.markdown("""
            <div class="card">
                <h4>Instructions:</h4>
                <ol>
                    <li>Upload a photo of your meal or salad.</li>
                    <li>Click <b>Analyze Meal Composition</b>.</li>
                    <li>View instant calorie count, macro charts, allergen alerts, and health scores.</li>
                </ol>
            </div>
            """, unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 2: FOOD FRESHNESS & SPOILAGE DIAGNOSTIC (EPIC 3)
# ----------------------------------------------------
elif selected_tab == "🥑 Freshness & Spoilage Diagnostic":
    st.markdown("### 🥑 Food Freshness & Spoilage Diagnostic Agent")
    st.write("Upload an image of perishable raw produce, meat, dairy, or seafood to inspect surface texture, discoloration, wrinkling, and mold growth.")

    col1, col2 = st.columns([1, 1])

    with col1:
        item_category = st.selectbox("Select Perishable Category", ["Fresh Produce (Fruits/Vegetables)", "Raw Meat / Poultry", "Dairy & Cheese", "Seafood"])
        item_name_input = st.text_input("Specific Item Name", value="Organic Hass Avocado")

        fresh_file = st.file_uploader("Upload Item Photo", type=["jpg", "jpeg", "png", "webp"], key="fresh_upload")
        if fresh_file:
            st.image(fresh_file, caption=item_name_input, use_container_width=True)

    with col2:
        st.markdown("#### 🔍 Spoilage & Quality Assessment")
        if st.button("🔬 Run Freshness Diagnosis", type="primary") or fresh_file:
            with st.spinner("Analyzing surface texture, color pigmentation, and fungal indicators..."):
                sample_img = Image.open(fresh_file) if fresh_file else Image.new('RGB', (300, 300), color=(100, 150, 100))
                f_result = analyze_freshness_image(sample_img, item_name_input, active_api_key)

            stage = f_result.get("freshness_stage", "Fresh")
            badge_class = "badge-fresh" if stage == "Fresh" else ("badge-moderate" if stage == "Moderately Fresh" else "badge-spoiled")

            st.markdown(f"### Item: **{f_result.get('item_name')}**")
            st.markdown(f"#### Freshness Stage: <span class='{badge_class}'>{stage}</span>", unsafe_allow_html=True)
            st.metric("Confidence Score", f"{f_result.get('confidence_score') * 100:.1f}%")

            safety = f_result.get("safety_status")
            if "Safe" in safety:
                st.success(f"🛡️ **Safety Status:** {safety}")
            elif "24h" in safety:
                st.warning(f"⚠️ **Safety Status:** {safety}")
            else:
                st.error(f"❌ **Safety Status:** {safety}")

            st.markdown(f"**Estimated Shelf Life Remaining:** {f_result.get('shelf_life_remaining')}")

            with st.expander("🔬 Detailed Visual Inspection Report", expanded=True):
                st.write(f"- **Surface Texture:** {f_result.get('surface_texture_assessment')}")
                st.write(f"- **Discoloration & Blemishes:** {f_result.get('discoloration_notes')}")
                st.write(f"- **Mold & Fungal Inspection:** {f_result.get('mold_inspection')}")

            st.markdown("#### 🧊 Proper Storage & Preservation Tips")
            st.info(f_result.get('storage_tips'))
        else:
            st.markdown("""
            <div class="card">
                <h4>Guidelines:</h4>
                <p>Select your food item category, input the item name, upload a close-up photo of the item, and run diagnosis to prevent foodborne illness and reduce household food waste.</p>
            </div>
            """, unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 3: KITCHEN HYGIENE COMPLIANCE (EPIC 4)
# ----------------------------------------------------
elif selected_tab == "🛡️ Kitchen Hygiene Compliance":
    st.markdown("### 🛡️ Commercial Kitchen Hygiene & Food Safety Compliance")
    st.write("Monitor commercial kitchen environments, sanitation protocols, PPE compliance, and cross-contamination hazards.")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("#### 📷 Kitchen Environment Media")
        kitchen_file = st.file_uploader("Upload Kitchen Photo or Video Frame", type=["jpg", "jpeg", "png", "mp4"], key="kitchen_upload")
        if kitchen_file:
            if kitchen_file.type.startswith("image"):
                st.image(kitchen_file, caption="Kitchen Prep Station", use_container_width=True)
            else:
                st.video(kitchen_file)
        else:
            st.info("No media uploaded. Click below to run audit on sample commercial kitchen inspection.")

    with col2:
        st.markdown("#### 📋 Hygiene Audit & Violation Log")
        if st.button("🔍 Run Hygiene Compliance Audit", type="primary") or kitchen_file:
            with st.spinner("Scanning kitchen workspace for PPE compliance, sanitation, and cross-contamination hazards..."):
                h_result = analyze_hygiene_media("kitchen inspection", active_api_key)

            score = h_result.get("overall_compliance_score", 88)
            st.metric("Overall Hygiene Compliance Score", f"{score} / 100", delta="Pass" if score >= 85 else "Action Required")
            st.caption(f"Facility Status: {h_result.get('facility_status')}")

            # Indicators breakdown
            indicators = h_result.get("indicators", {})
            ind_df = pd.DataFrame([
                {"Indicator": k.replace("_", " ").title(), "Score": v["score"], "Status": v["status"], "Notes": v["notes"]}
                for k, v in indicators.items()
            ])
            st.dataframe(ind_df, use_container_width=True)

            st.markdown("#### ⚠️ Itemized Violation Logs & Corrective Actions")
            violations = h_result.get("violations", [])
            if violations:
                for v in violations:
                    sev = v.get("severity")
                    color = "red" if sev == "High" else ("orange" if sev == "Medium" else "blue")
                    st.markdown(f"<span style='color:{color}; font-weight:bold;'>[{sev} Severity] {v.get('category')}</span>", unsafe_allow_html=True)
                    st.write(f"- **Issue:** {v.get('description')}")
                    st.write(f"- **Corrective Action:** {v.get('corrective_action')}")
                    st.markdown("---")
            else:
                st.success("Zero safety violations detected.")

            st.markdown("#### 📝 Executive Summary")
            st.info(h_result.get("summary"))
        else:
            st.markdown("""
            <div class="card">
                <h4>Key Hygiene Indicators Monitored:</h4>
                <ul>
                    <li>Chef Hat / Hairnet Compliance</li>
                    <li>Glove Usage & Sanitization Frequency</li>
                    <li>Surface Sanitization State</li>
                    <li>Cross-Contamination Hazards (Raw vs. Ready-to-Eat)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ----------------------------------------------------
# TAB 4: SMART KITCHEN RECIPE ASSISTANT (EPIC 4)
# ----------------------------------------------------
elif selected_tab == "👨‍🍳 Smart Recipe Assistant":
    st.markdown("### 👨‍🍳 Smart Kitchen Recipe Assistant")
    st.write("Input available pantry inventory and ingredients to generate creative, nutritious recipes with cooking instructions and substitutions.")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("#### 🧺 Pantry Inventory")
        default_ingredients = ["Chicken Breast", "Broccoli", "Garlic", "Olive Oil", "Quinoa", "Spinach", "Tomatoes"]
        selected_ingredients = st.multiselect(
            "Select or type your available ingredients:",
            options=["Chicken Breast", "Salmon", "Eggs", "Broccoli", "Spinach", "Tomatoes", "Garlic", "Onions", "Quinoa", "Brown Rice", "Olive Oil", "Avocado", "Bell Peppers", "Mushrooms", "Lemon"],
            default=default_ingredients
        )

        custom_ing = st.text_input("Add custom ingredient:")
        if custom_ing and st.button("Add Ingredient"):
            selected_ingredients.append(custom_ing)

        meal_type = st.selectbox("Meal Type", ["Any", "Breakfast", "Lunch", "Dinner", "Quick Snack"])
        diet_pref = st.selectbox("Dietary Preference", ["Balanced", "High Protein", "Low Carb", "Vegetarian", "Vegan", "Keto", "Gluten-Free"])

        generate_btn = st.button("✨ Generate Smart Recipes", type="primary")

    with col2:
        st.markdown("#### 🍲 AI Generated Recipes")
        if generate_btn or selected_ingredients:
            with st.spinner("Crafting gourmet recipes from your pantry inventory..."):
                recipes = generate_smart_recipes(selected_ingredients, active_api_key)

            for i, recipe in enumerate(recipes):
                with st.expander(f"🌟 {recipe.get('recipe_name')} ({recipe.get('cooking_time')} | {recipe.get('difficulty')})", expanded=(i==0)):
                    rc1, rc2, rc3, rc4 = st.columns(4)
                    rc1.metric("Calories", f"{recipe.get('calories')} kcal")
                    rc2.metric("Protein", recipe.get('protein'))
                    rc3.metric("Carbs", recipe.get('carbs'))
                    rc4.metric("Fats", recipe.get('fats'))

                    st.markdown(f"**Description:** {recipe.get('description')}")

                    st.markdown("**Step-by-Step Instructions:**")
                    for s_idx, step in enumerate(recipe.get('steps', [])):
                        st.write(f"{s_idx + 1}. {step}")

                    st.markdown(f"**💡 Ingredient Substitutions:** {recipe.get('substitutions')}")
        else:
            st.info("Select your available pantry ingredients on the left and click **Generate Smart Recipes**.")

# ----------------------------------------------------
# TAB 5: PERSONALIZED MEAL PLANNER (EPIC 5)
# ----------------------------------------------------
elif selected_tab == "📅 Personalized Meal Planner":
    st.markdown("### 📅 Personalized TDEE Meal Planner & Automated Grocery List")
    st.write("Input your biometric profile and fitness goals to compute BMR/TDEE caloric targets and generate an adaptive 7-day meal schedule with automated grocery shopping lists.")

    with st.form("meal_planner_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Age (Years)", min_value=15, max_value=100, value=28)
            gender = st.selectbox("Gender", ["Male", "Female"])
        with col2:
            weight_kg = st.number_input("Weight (kg)", min_value=35.0, max_value=200.0, value=75.0)
            height_cm = st.number_input("Height (cm)", min_value=120.0, max_value=220.0, value=178.0)
        with col3:
            activity_level = st.selectbox("Activity Level", [
                "Sedentary (little or no exercise)",
                "Lightly active (light exercise/sports 1-3 days/week)",
                "Moderately active (moderate exercise/sports 3-5 days/week)",
                "Very active (hard exercise/sports 6-7 days a week)"
            ])
            goal = st.selectbox("Fitness Goal", ["Fat Loss (-500 kcal)", "Maintenance", "Muscle Gain (+300 kcal)"])

        col_d1, col_d2 = st.columns(2)
        with col_d1:
            diet_constraint = st.selectbox("Dietary Constraint", ["Balanced", "High Protein", "Keto", "Vegetarian", "Vegan", "Diabetic-Friendly"])
        with col_d2:
            st.markdown("<br>", unsafe_allow_html=True)
            submit_profile = st.form_submit_button("🚀 Generate 7-Day Meal Plan & Grocery List", type="primary")

    if submit_profile or 'profile_submitted' in st.session_state:
        st.session_state['profile_submitted'] = True

        # Calculate BMR, TDEE, Calories
        bmr, tdee, target_cal = calculate_bmr_tdee(age, gender, weight_kg, height_cm, activity_level, goal)
        macros = calculate_macros(target_cal, diet_constraint)

        st.markdown("---")
        st.markdown("### 📊 Calculated Energy & Macro Targets")
        mc1, mc2, mc3, mc4, mc5 = st.columns(5)
        mc1.metric("BMR", f"{bmr} kcal")
        mc2.metric("TDEE", f"{tdee} kcal")
        mc3.metric("Target Calories", f"{target_cal} kcal")
        mc4.metric("Protein Target", f"{macros['protein_g']}g")
        mc5.metric("Carbs / Fats", f"{macros['carbs_g']}g / {macros['fat_g']}g")

        profile_dict = {
            "age": age, "gender": gender, "weight_kg": weight_kg, "height_cm": height_cm,
            "activity_level": activity_level, "goal": goal, "diet": diet_constraint, "target_calories": target_cal
        }

        with st.spinner("Generating 7-day adaptive schedule and grocery list..."):
            meal_data, shopping_list = generate_ai_meal_plan(profile_dict, active_api_key)

        st.markdown("---")
        st.markdown("### 🗓️ Adaptive 7-Day Meal Schedule")

        days_tabs = st.tabs([m["day"] for m in meal_data])
        for idx, day_info in enumerate(meal_data):
            with days_tabs[idx]:
                st.markdown(f"#### **{day_info['day']} Menu**")

                b = day_info["breakfast"]
                l = day_info["lunch"]
                d = day_info["dinner"]
                s = day_info["snacks"]

                col_b, col_l, col_d, col_s = st.columns(4)
                with col_b:
                    st.markdown("##### 🍳 Breakfast")
                    st.write(f"**{b['name']}**")
                    st.caption(f"{b['calories']} kcal | P: {b['protein']} | C: {b['carbs']} | F: {b['fat']}")
                with col_l:
                    st.markdown("##### 🥗 Lunch")
                    st.write(f"**{l['name']}**")
                    st.caption(f"{l['calories']} kcal | P: {l['protein']} | C: {l['carbs']} | F: {l['fat']}")
                with col_d:
                    st.markdown("##### 🥩 Dinner")
                    st.write(f"**{d['name']}**")
                    st.caption(f"{d['calories']} kcal | P: {d['protein']} | C: {d['carbs']} | F: {d['fat']}")
                with col_s:
                    st.markdown("##### 🍎 Snack")
                    st.write(f"**{s['name']}**")
                    st.caption(f"{s['calories']} kcal | P: {s['protein']} | C: {s['carbs']} | F: {s['fat']}")

        st.markdown("---")
        st.markdown("### 🛒 Automated Grocery Shopping List")

        g1, g2, g3 = st.columns(3)
        with g1:
            st.markdown("#### 🥦 Produce")
            for item in shopping_list.get("Produce", []):
                st.checkbox(item, value=True, key=f"prod_{item}")
        with g2:
            st.markdown("#### 🥩 Proteins & Dairy")
            for item in shopping_list.get("Proteins & Dairy", []):
                st.checkbox(item, value=True, key=f"prot_{item}")
        with g3:
            st.markdown("#### 🌾 Pantry & Grains")
            for item in shopping_list.get("Pantry & Grains", []):
                st.checkbox(item, value=True, key=f"pntr_{item}")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6B7280; font-size: 0.9rem;'>"
    "Food Verse AI – Multimodal Food Intelligence Agent | Skill Wallet Capstone Project 3 (Platform ID: 6ac4ca021dcde6d7857c169a)<br>"
    "Powered by Streamlit, Google Gemini Multimodal AI & Python"
    "</div>",
    unsafe_allow_html=True
)
