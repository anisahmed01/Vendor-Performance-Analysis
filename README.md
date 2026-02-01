# Vendor Performance & Profitability Analysis  
**End-to-End, Database-Driven Analytics Project**

## 📌 Project Overview
This project performs a comprehensive **Vendor Performance Analysis** for a wine and spirits distribution business.  
It is designed as a **real-world simulation**, covering the full analytics lifecycle from database-level aggregation to business-ready dashboards.

The objective is to evaluate vendor and brand performance, identify profitability drivers, assess purchasing efficiency, and uncover inventory risks to support data-driven decision-making.

---

## 🗄️ Data Source & Architecture
- Data sourced from a **MySQL inventory database**
- Multiple operational tables integrated, including:
  - Purchases
  - Sales
  - Purchase Prices
  - Vendor Invoices
  - Inventory snapshots
- SQL used to aggregate raw transactional data into a consolidated analytical table at the **Vendor–Brand level**

---

## 🛠️ Tools & Technologies
- **SQL (MySQL)** – Data extraction, joins, aggregations, and table creation  
- **Python** – Data cleaning, feature engineering, EDA, and statistical analysis  
  - Libraries: `pandas`, `numpy`, `scipy`, `sqlalchemy`, `matplotlib`, `seaborn`
- **Power BI** – Interactive dashboards and business reporting  

---

## 📊 Key Metrics Engineered
- Gross Profit  
- Profit Margin (%)  
- Stock Turnover  
- Sales-to-Purchase Ratio  
- Unit Purchase Price  
- Unsold Inventory Value  
- Order Size Classification (Small / Medium / Large)

---

## 🔍 Key Analytical Insights
- Vendor performance is highly skewed: a small subset drives most sales and purchases
- High sales volume does **not** guarantee high profit margins
- Bulk purchasing reduces unit costs by approximately **72%**
- Over **$2.7M** in capital is locked in unsold inventory
- Low-performing vendors often sell high-margin niche products
- Statistical testing confirms significant profit margin differences between high- and low-performing vendors

---

## 📈 Analysis Techniques Used
- Exploratory Data Analysis (EDA)
- Distribution & outlier analysis
- Correlation analysis
- Pareto (80/20) analysis
- Inventory turnover analysis
- Confidence intervals (95%)
- Two-sample t-test for statistical validation

---

## 📊 Visualization & Reporting
- Python-based exploratory visualizations for analysis
- Final dataset exported for **Power BI**
- Power BI dashboards built for:
  - Vendor performance
  - Purchase contribution
  - Inventory risk
  - Profitability comparison

---

## 📁 Repository Contents
- `notebooks/` – End-to-end analysis notebook
- `sql/` – SQL used for data aggregation
- `data/processed/` – Final dataset used for visualization
- `powerbi/` – Power BI dashboard file
- `presentation/` – Business presentation deck

---

## 🚀 Key Takeaways
This project demonstrates:
- End-to-end analytical thinking
- Strong data modeling and feature engineering
- Business-focused insights backed by statistics
- Readiness for real-world data analysis workflows

---
## 📄 requirements.txt (Minimal & Clean)
```
pandas
numpy
scipy
sqlalchemy
matplotlib
seaborn
```
---

## 📌 Future Enhancements
- Automated data refresh pipeline
- Vendor scorecard system
- Predictive inventory risk modeling
- Scenario-based pricing simulations
