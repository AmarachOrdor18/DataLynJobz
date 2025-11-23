# Power BI Dashboard

This directory contains the Power BI dashboard for LinkedIn Job Analytics.

## 📁 Files

- **LinkedIn_Job_Analytics.pbix**: Main Power BI dashboard file
- **screenshots/**: Preview images of the dashboard

## 🚀 Getting Started

### Prerequisites
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Free)
- Windows 10 or later (for Power BI Desktop)

### Opening the Dashboard

1. **Install Power BI Desktop**
   - Download from [Microsoft Power BI](https://powerbi.microsoft.com/desktop/)
   - Free version is sufficient

2. **Open the Dashboard**
   ```
   Double-click: LinkedIn_Job_Analytics.pbix
   ```

3. **Refresh Data (if needed)**
   - Click "Refresh" in the Home ribbon
   - Ensure data files are in the `/model` directory

## 📊 Dashboard Pages

### 1. Overview Page
**Purpose**: High-level summary of the job market

**Key Metrics (Top Row):**
- Total Jobs: 6,669
- Entry Level Jobs: 445 (6.67%)
- Seniority breakdown with donut chart

**Visualizations:**
- **Monthly Job Trends**: Area chart showing job posting volume over time (Jan-Dec)
- **Top 5 Job Titles**: Bar chart with Data Analyst (2,177), Senior Data Analyst (278), Junior Data Analyst (206), Business Intelligence Analyst (146), Business Data Analyst (140)
- **Educational Requirements**: 
  - Donut chart: Mentioned (60.41%) vs Not Mentioned (39.59%)
  - Bar chart: Engineering (2.22K), Statistics (1.85K), Computer Science (1.66K)
- **Talent Demand Breakdown by Domain**:
  - Technology: 2,332 jobs (34.97%)
  - Financial: 1,682 jobs (25.22%)
  - Retail: 610 jobs (9.15%)
  - Healthcare: 499 jobs (7.48%)

**Filters:**
- Year: 2024, 2025
- Level: Entry level, Junior, Lead, Mid-level, Senior

**Key Visuals:**
- Area chart for trends
- Horizontal bar charts for comparisons
- Donut charts for distributions
- Table with domain breakdown

### 2. Basic Skills Page
**Purpose**: Analyze fundamental required skills

**Key Metrics (Top Row):**
- Basic Skill Mentions: 6,518 (97.74% of jobs)
- Soft Skills Job Count: 5,373 (80.6%)
- Analytical Skills Job Count: 3,898 (58.45%)
- Technical Skills Job Count: 6,385 (95.74%)

**Skill Breakdowns:**
- **Soft Skills**: Communication, Problem-solving, Collaboration (shown as cards)
- **Analytical Skills**: Data Visualization, Statistical Analysis, Data Mining
- **Technical Skills**: SQL, Excel, Python, Reporting

**Visualizations:**
- **Monthly Job Counts**: Area chart showing trends (Jan-Dec)
  - Peak: March (531), April (500), February (442)
  - Low: August (159), November (24)
- **Company Skill Demand**: Horizontal bar chart
  - TikTok: 32 mentions
  - Meta: 20 mentions
  - Amazon: 17 mentions
  - GRAYCE: 9 mentions
- **Skill Detail Table**: Expandable by company (e.g., TikTok breakdown shows Data Visualization: 28, Data Mining: 4, Statistical Analysis: 2)

**Tabs:** analytical_skills, soft_skills, technical_skills

**Filters:**
- Year: 2024, 2025
- Level: Entry level, Junior, Lead, Mid-level, Senior

### 3. Add-on Skills (Advanced) Page
**Purpose**: Analyze specialized and advanced skills

**Key Metrics (Top Row):**
- Advanced Skills: 3,718 (55.75% of jobs)
- Cloud Skill Mentions: 1,642 (24.62%)
- DE (Data Engineering) Skill Mentions: 2,210 (33.14%)
- ML Skill Mentions: 1,606 (24.08%)

**Skill Breakdowns:**
- **Cloud Skills**: AWS, Azure, Snowflake (shown as cards)
- **Data Engineering**: ETL, Data Modeling, Data Warehouse
- **ML Skills**: Automation, Machine Learning, Predictive Modeling

**Visualizations:**
- **Monthly Job Counts**: Area chart showing hiring trends
  - Peaks: March (257), February (251), April (250), September (262)
  - Lows: August (85), November (10)
- **Company Skill Demand**: Horizontal bar chart
  - GRAYCE: 9 mentions
  - Meta: 7 mentions
  - TikTok: 5 mentions
  - Amazon: 3 mentions
- **Skill Detail Table**: Shows job counts by company

**Tabs:** cloud_skills, data_engineering, ml_skills

**Filters:**
- Year: 2024, 2025
- Level: Entry level, Junior, Lead, Mid-level, Senior

## 🔗 Data Connections

The dashboard connects to Excel files in the `/model` directory:

### Dimension Tables
- `dim_company.xlsx`
- `dim_country.xlsx`
- `dim_date.xlsx`
- `dim_title.xlsx`
- `dim_category.xlsx`
- `dim_skill.xlsx`
- `dim_seniority.xlsx`

### Fact & Bridge Tables
- `fact_jobs.xlsx`
- `bridge_job_skill.xlsx`
- `bridge_job_seniority.xlsx`

### Additional Data
- `association_rules.csv`

## 🔄 Updating Data Connections

If you move the project folder or data files:

1. **Go to**: Home → Transform data → Data source settings
2. **Change Source**: Update file paths to `/model` directory
3. **Apply Changes**
4. **Refresh**: Click "Refresh" to reload data

## 🎨 Customization

### Changing Colors
1. Go to **View** → **Themes**
2. Select a built-in theme or create custom

### Adding New Visuals
1. Click blank area on canvas
2. Select visual type from **Visualizations** pane
3. Drag fields to configure

### Creating Calculated Measures
```DAX
Total Jobs = COUNTROWS(fact_jobs)

Avg Skills Per Job = 
DIVIDE(
    COUNTROWS(bridge_job_skill),
    COUNTROWS(fact_jobs),
    0
)

Top Skill = 
CALCULATE(
    FIRSTNONBLANK(dim_skill[skill_name], 1),
    TOPN(1, VALUES(dim_skill[skill_name]), [Skill Count])
)
```

## 📸 Screenshots

Preview images are available in the `screenshots/` folder:
- `overview_page.png` - Total jobs, trends, top titles, education, domain breakdown
- `basic_skills_page.png` - Soft, analytical, and technical skills analysis
- `addon_skills_page.png` - Cloud, data engineering, and ML skills

## 🐛 Troubleshooting

### Issue: Data Not Loading
**Solution:** Check that all Excel/CSV files are in the `/model` directory

### Issue: Relationships Not Working
**Solution:** 
1. Go to **Model View** (left sidebar)
2. Verify relationships between tables
3. Ensure Primary Keys match Foreign Keys

### Issue: Custom Visual Not Showing
**Solution:** 
1. Enable custom visuals: File → Options → Security
2. Download required custom visuals from AppSource

### Issue: Performance Issues
**Solution:**
1. Reduce data volume (filter years/countries)
2. Use Import mode instead of DirectQuery
3. Optimize DAX measures

## 📚 Resources

- [Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [DAX Guide](https://dax.guide/)
- [Power BI Community](https://community.powerbi.com/)
- [Custom Visuals Marketplace](https://appsource.microsoft.com/marketplace/apps?product=power-bi-visuals)

## 🤝 Contributing

To contribute to the Power BI dashboard:
1. Make changes in Power BI Desktop
2. Save the `.pbix` file
3. Take screenshots of new pages/visuals
4. Update this README with new features

## 📧 Support

For questions about the Power BI dashboard:
- Open an issue on GitHub
- Tag with `power-bi` label
- Include screenshots if relevant

---

**Pro Tip:** Export your dashboard to PDF for sharing:
File → Export → Export to PDF