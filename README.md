# 📊 LinkedIn Job Analytics: Data Analyst Skills Intelligence

> An end-to-end data analytics project analyzing LinkedIn job postings to uncover skill requirements, trends, and associations in the data analytics field.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)](https://streamlit.io/)

<img width="1343" height="692" alt="image" src="https://github.com/user-attachments/assets/d8c378a0-e1e2-43cc-9c4e-4ac63d5686c0" />

## 🎯 Project Overview

This project provides comprehensive insights into the data analytics job market by:
- Cleaning and processing 6,000+ scraped LinkedIn job postings (2024 data) obtained from [Rafa Bela-Kurows' dataset](https://github.com/rafabelokurows/data-analyst-job-skills/tree/main/data)
- Extracting skills, requirements, and seniority levels
- Building a star schema data model for analysis
- Discovering skill associations using market basket analysis
- Creating an interactive Streamlit dashboard for exploration


## ✨ Key Features

- **📝 Data Cleaning Pipeline**: Translates non-English postings, extracts HTML, and standardizes data
- **🗂️ Star Schema Design**: Dimension and fact tables optimized for BI tools
- **🔍 Skill Association Mining**: Discovers which skills frequently appear together
- **📊 Power BI Dashboard**: Interactive visualizations for deep insights
- **📈 Streamlit App**: 3-page interactive web app with ML-powered predictions
- **🤖 ML Model**: Predicts seniority level based on skill combinations

## 🛠️ Tech Stack

- **Languages**: Python 3.11
- **Data Processing**: pandas, numpy
- **NLP**: langdetect, googletrans
- **Machine Learning**: scikit-learn, mlxtend
- **Visualization**: plotly, streamlit
- **BI Integration**: Power BI compatible outputs

## 📁 Project Structure

```
linkedin-job-analytics/
├── notebooks/           # Jupyter notebooks for data processing
├── app/                # Streamlit dashboard
├── powerbi/            # powerbi dashboard
├── model/              # Dimension tables & association rules
├── data/               # Raw and processed data (not tracked)
└── docs/               # Documentation
```

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8 or higher
pip or conda package manager
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/linkedin-job-analytics.git
cd linkedin-job-analytics
```

2. **Create a virtual environment**
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n job-analytics python=3.8
conda activate job-analytics
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### 📊 Running the Analysis

#### Step 1: Data Cleaning
```bash
jupyter notebook notebooks/01_data_cleaning.ipynb
```
- Input: `Final Dataset.xlsx`
- Output: `linkedin_data_final.xlsx`
- Duration: ~30 minutes (includes translation)

#### Step 2: Create Dimension Tables
```bash
jupyter notebook notebooks/02_dimension_tables.ipynb
```
- Input: `linkedin_data_final.xlsx`
- Output: 10 Excel files in `/model` directory
- Duration: ~5 minutes

#### Step 3: Generate Association Rules
```bash
jupyter notebook notebooks/03_association_rules.ipynb
```
- Input: Bridge and dimension tables
- Output: `association_rules.csv`
- Duration: ~3 minutes

#### Step 4: Open Power BI Dashboard
1. Open `powerbi/LinkedIn_Job_Analytics.pbix` in Power BI Desktop
2. Refresh data connections (if needed)
3. Explore interactive visualizations

**OR**

#### Step 4: Launch Streamlit Dashboard
```bash
streamlit run app/app.py
```
- Opens at `http://localhost:8501`

## 📱 Dashboard Features

### Power BI Dashboard (3 Pages)

**📊 Page 1: Overview**
- Total jobs analyzed (6,669)
- Monthly job posting trends
- Entry level breakdown (445 jobs, 6.67%)
- Top 5 job titles (Data Analyst leading with 2,177 jobs)
- Educational requirements breakdown
- Talent demand by domain (Technology 35%, Financial 25%, Retail 9%, Healthcare 7%)

**🎯 Page 2: Basic Skills**
- Basic skill mentions (6,518 total, 97.74% coverage)
- Breakdown by category:
  - Soft Skills: 5,373 mentions (80.6%)
  - Analytical Skills: 3,898 mentions (58.45%)
  - Technical Skills: 6,385 mentions (95.74%)
- Top skills: Communication, Problem-solving, Collaboration
- Top analytical: Data Visualization, Statistical Analysis, Data Mining
- Top technical: SQL, Excel, Python, Reporting
- Company skill demand (TikTok, Meta, Amazon, GRAYCE)
- Monthly trends and seniority level filters

**⚙️ Page 3: Add-on Skills (Advanced)**
- Advanced skill mentions (3,718 total, 55.75% coverage)
- Cloud skills: AWS (1,642), Azure, Snowflake (24.62% coverage)
- Data Engineering: ETL, Data Modeling, Data Warehouse (33.14% coverage)
- ML Skills: Automation, Machine Learning, Predictive Modeling (24.08% coverage)
- Company skill demand breakdown
- Monthly trends by skill category
- Interactive filters by year (2024/2025) and seniority level

### Streamlit App

**1️⃣ Skill Mix Predictor by Role**
- Select a seniority level (Entry, Junior, Mid, Senior, Lead)
- Get recommended skill mix across 9 categories
- See top technical skills (SQL, Python, Tableau, etc.)

**2️⃣ Skill Association Finder**
- Search for any skill (e.g., "Python", "SQL", "Excel")
- Discover skills frequently paired together
- View confidence scores for associations

**3️⃣ Predict My Seniority Level**
- Select your skills from 9 categories
- ML model predicts best-fit seniority level
- See probability distribution across all levels

## 📈 Data Model

### Star Schema Design
```
Fact Table: fact_jobs
├── job_id (PK)
├── company_id (FK → dim_company)
├── country_id (FK → dim_country)
├── date_id (FK → dim_date)
└── title_id (FK → dim_title)

Bridge Tables:
├── bridge_job_skill (job_id, skill_id, category_id)
└── bridge_job_seniority (job_id, level_id)

Dimension Tables:
├── dim_company
├── dim_country
├── dim_date (with time intelligence attributes)
├── dim_title
├── dim_skill
├── dim_category
└── dim_seniority
```

## 🎓 Skill Categories

1. **Soft Skills**: Communication, Problem-solving, Teamwork
2. **Analytical Skills**: Data Visualization, Statistical Analysis
3. **Technical Skills**: SQL, Python, Excel, Power BI, Tableau
4. **Data Engineering**: ETL, Data Pipelines, Airflow
5. **ML Skills**: Machine Learning, Predictive Modeling
6. **Cloud Skills**: AWS, Azure, Snowflake
7. **Education Level**: Bachelor's, Master's, PhD
8. **Degree**: Computer Science, Statistics, Mathematics
9. **Domain**: Finance, Healthcare, Retail, Technology

## 📊 Key Insights

From analyzing 6,669 data analyst job postings:

**Most In-Demand Skills:**
- Technical Skills: SQL (95.74%), Excel, Python, Reporting
- Soft Skills: Communication (80.6%), Problem-solving, Collaboration
- Analytical: Data Visualization (58.45%), Statistical Analysis

<img width="1343" height="685" alt="image" src="https://github.com/user-attachments/assets/535eb9e8-0a0b-4a98-9b04-d0d1ba8cb279" />


**Advanced Skills Coverage:**
- Cloud Skills: 24.62% (AWS leading at 1,642 mentions)
- Data Engineering: 33.14% (ETL, Data Modeling, Data Warehouse)
- ML Skills: 24.08% (Automation, Machine Learning, Predictive Modeling)

**Job Market Trends:**
- 97.74% of jobs require basic skills
- 55.75% require advanced/specialized skills
- Top hiring: TikTok, Meta, Amazon, GRAYCE
- Technology sector dominates (35% of jobs)

**Seniority Distribution:**
- Entry Level: 6.67% (445 jobs)
- Senior: 19.27%
- Junior: 7.71%
- Lead: 31.87%
- Not Specified: 34.46%

**Education Requirements:**
- 60.41% jobs mention education requirements
- Top degrees: Engineering (2.22K), Statistics (1.85K), Computer Science (1.66K)

## 👤 Author

**Your Name**
- GitHub: [@AmarachOrdor18](https://github.com/AmarachOrdor18)

## 🙏 Acknowledgments

- Data sourced from LinkedIn job postings (2024)
- Built with love for the data analytics community
- Thanks to all contributors and users

## 📧 Contact

For questions or feedback, please open an issue or contact [amarachiordor2@gmail.com](mailto:amarachiordor2@gmail.com)

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐
