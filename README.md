# Food Verse AI – Multimodal Food Intelligence Agent

**Skill Wallet Capstone Project 3**  
**Category:** Generative AI | Nutrition, Freshness & Kitchen Safety  
**Platform ID:** `6ac4ca021dcde6d7857c169a`

---

## 🌟 Overview & Objective
**Food Verse AI** is a complete, production-ready multimodal food intelligence ecosystem built in Python and Streamlit. It analyzes food images, raw perishable items, and commercial kitchen environments using state-of-the-art vision AI (Google Gemini 1.5) with robust standalone demonstration fallbacks. 

It covers 5 core intelligence pillars across all required capstone epics:
1. **Food Recognition & Nutrition Audit (Epic 2):** Multimodal dish recognition, macro/micronutrient breakdown, allergen alerts, and health scores (1-100).
2. **Food Freshness & Spoilage Diagnostic (Epic 3):** Perishable raw item inspection (surface texture, discoloration, wrinkling, mold), freshness classification (`Fresh` | `Moderately Fresh` | `Spoiled`), safety advice, and preservation storage tips.
3. **Kitchen Hygiene & Food Safety Compliance (Epic 4):** Commercial kitchen hygiene monitoring (chef hat/hairnet compliance, glove usage, sanitization state, cross-contamination hazards) with itemized violation logs.
4. **Smart Kitchen Recipe Assistant (Epic 4):** Pantry inventory recipe generation with cooking time, difficulty, step-by-step instructions, and ingredient substitutions.
5. **Personalized Meal Planner (Epic 5):** Biometric profile capture (age, gender, weight, activity level, dietary constraints, fitness goals), Mifflin-St Jeor BMR/TDEE calculation, adaptive 7-day meal schedule, and automated categorized grocery shopping list.

---

## 🚀 Tech Stack
- **Python 3.9+**
- **Streamlit** (Interactive Dashboard UI)
- **Google Generative AI (Gemini 1.5 Flash)** (Multimodal Vision & Structured Reasoning)
- **Plotly** (Interactive Macronutrient & Health Charts)
- **Pillow & NumPy & Pandas** (Image processing & data handling)

---

## 📦 Project Structure
```text
Food Verse AI/
├── app.py                  # Main Streamlit application with 5 intelligence pillars
├── requirements.txt        # Python package dependencies
├── utils/
│   ├── __init__.py
│   ├── ai_client.py        # Gemini multimodal API client with robust fallback simulation
│   ├── nutrition_calc.py   # Mifflin-St Jeor BMR/TDEE & macro calculation formulas
│   └── mock_data.py        # Comprehensive standalone demo data
└── README.md               # Project documentation
```

---

## 🛠️ Local Installation & Running

1. **Clone or Navigate to Project Directory:**
   ```bash
   cd "D:\College Essentials\Skill wallet"
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

4. **Access the App:**
   Open your browser at `http://localhost:8501`.

---

## ☁️ Deployment on Streamlit Community Cloud
1. Push this repository to GitHub.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New App**, select your repository, branch (`main`), and set the main file path to `app.py`.
4. Click **Deploy**!
