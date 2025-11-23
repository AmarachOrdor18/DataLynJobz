import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(layout="wide")
st.title("🔍 Skill Intelligence Dashboard")

# === Load Data === #
@st.cache_data

def load_data():
    job_skill = pd.read_excel("./model/bridge_job_skill.xlsx")
    skill = pd.read_excel("./model/dim_skill.xlsx")
    seniority = pd.read_excel("./model/bridge_job_seniority.xlsx")
    level = pd.read_excel("./model/dim_seniority.xlsx")
    rules = pd.read_csv("./model/association_rules.csv")
    return job_skill, skill, seniority, level, rules

job_skill, dim_skill, bridge_seniority, dim_seniority, rules = load_data()

# === Merge Data === #
job_skills = job_skill.merge(dim_skill, on="skill_id")
job_seniority = bridge_seniority.merge(dim_seniority, on="level_id")
job_skill_combo = job_skills.merge(job_seniority, on="job_id")

# === Skill Categories === #
category_map = {
    "soft_skills": ["communication", "attention to detail", "problem-solving", "presentation", "storytelling", "critical thinking", "collaboration", "teamwork", "stakeholder management", "curiosity", "innovation"],
    "analytical_skills": ["data cleaning", "statistical analysis", "exploratory data analysis", "data visualization", "data mining", "data exploration", "data storytelling", "dashboard"],
    "technical_skills": ["sql", "python", "r", "tableau", "power bi", "excel", "looker", "power point", "database management", "reporting", "documentation", "dax", "macros", "pyspark"],
    "data_engineering": ["data warehouse", "data modeling", "apache spark", "dbt", "etl", "elt", "data pipelines", "airflow", "data lake", "data integration"],
    "ml_skills": ["machine learning", "automation", "predictive modeling", "clustering", "deep learning", "decision tree"],
    "cloud_skills": ["azure", "aws", "databricks", "snowflake", "redshift"],
    "education_level": ["bachelor", "master", "phd", "diploma"],
    "degree": ["computer science", "engineering", "statistics", "mathematics", "economics", "informatics", "information systems", "data science"]
}

# === Page Navigation === #
page = st.sidebar.selectbox("Navigate", [
    "1️⃣ Skill Mix Predictor by Role",
    "2️⃣ Skill Association Finder",
    "3️⃣ Predict My Seniority Level"
])

# === Page 1 === #
if page == "1️⃣ Skill Mix Predictor by Role":
    st.subheader("📌 What is the ideal mix of skills by seniority level?")
    levels = sorted(job_skill_combo["seniority_level"].dropna().unique())
    selected_level = st.selectbox("Select Seniority Level", levels)

    if selected_level:
        level_df = job_skill_combo[job_skill_combo["seniority_level"] == selected_level]
        skill_counts = level_df["skill_name"].str.lower().value_counts()

        output = {}
        for cat, skills in category_map.items():
            matches = skill_counts[skill_counts.index.isin(skills)]
            if not matches.empty:
                if cat == "technical_skills":
                    output[cat] = matches.head(2).index.tolist()
                else:
                    output[cat] = matches.head(1).index.tolist()

        st.markdown("### 🧭 Suggested Skill Mix for " + selected_level.title())
        for cat, skills in output.items():
            if skills:
                cat_name = cat.replace("_", " ").title()
                for s in skills:
                    st.markdown(f"- **{cat_name}**: `{s.title()}`")

# === Page 2 === #
elif page == "2️⃣ Skill Association Finder":
    st.subheader("📌 What skills are often associated together?")
    all_skills = job_skill_combo["skill_name"].str.lower().unique().tolist()
    selected_skill = st.selectbox("Select a skill", sorted(all_skills))

    if selected_skill:
        filtered_rules = rules[rules["If Skills (Antecedents)"].str.contains(selected_skill, case=False)]
        if not filtered_rules.empty:
            top_rules = filtered_rules.sort_values("Confidence", ascending=False).head(2)
            st.markdown(f"### 🔎 Skills that frequently appear with **{selected_skill.title()}**:")
            for i, row in top_rules.iterrows():
                st.markdown(f"- 👉 `{row['Then Skills (Consequents)']}` (Confidence: {row['Confidence']:.2f})")
        else:
            st.warning("No strong associations found for that skill.")

# === Page 3 === #
elif page == "3️⃣ Predict My Seniority Level":
    st.subheader("🔮 Predict your ideal seniority level based on selected skills")

    st.sidebar.header("🧠 Choose Your Skills")
    selected_skills = []

    for cat, skills in category_map.items():
        picked = st.sidebar.multiselect(f"{cat.replace('_', ' ').title()}", skills)
        selected_skills.extend([s.lower() for s in picked])

    grouped = job_skill_combo.groupby("job_id").agg({
        "skill_name": lambda x: list(set(x.str.lower())),
        "seniority_level": "first"
    }).reset_index()

    X = grouped["skill_name"]
    y = grouped["seniority_level"]

    mlb = MultiLabelBinarizer()
    X_encoded = mlb.fit_transform(X)

    model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
    model.fit(X_encoded, y)

    if selected_skills:
        input_vec = mlb.transform([selected_skills])
        prediction = model.predict(input_vec)[0]
        proba = model.predict_proba(input_vec)[0]

        st.success(f"🎯 Based on your selected skills, you best fit **{prediction.upper()}** roles.")

        prob_df = pd.DataFrame({
            "Seniority Level": model.classes_,
            "Probability": proba
        }).sort_values("Probability", ascending=False)

        fig = px.bar(prob_df, x="Probability", y="Seniority Level", orientation="h", color="Probability", color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Please select skills from the sidebar to get your prediction.")