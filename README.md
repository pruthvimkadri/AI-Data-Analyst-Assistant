# 🚀 DecisionAI – AI-Powered Business Intelligence Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analytics-black?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Dashboards-3F4F75?style=for-the-badge&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 🌐 Live Demo

### 🚀 Try DecisionAI

https://ai-data-analyst-assistant-dihdjusjw4ciry6rcv5bhf.streamlit.app/

---

# 📖 Overview

DecisionAI is an **AI-powered Business Intelligence Platform** that transforms raw business datasets into actionable insights through automated data cleaning, interactive dashboards, deterministic KPI generation, executive reporting, and conversational AI.

Unlike traditional dashboard tools, DecisionAI combines a **deterministic analytics engine** with **Google Gemini** to generate reliable business insights while minimizing AI hallucinations.

Simply upload a CSV or Excel dataset and DecisionAI will automatically:

- Clean and validate data
- Detect dataset characteristics
- Perform business analytics
- Build interactive dashboards
- Generate KPIs
- Produce executive reports
- Answer business questions using AI
- Export professional reports

---

# 🏗️ Architecture

DecisionAI follows a **hybrid AI architecture**.

Instead of allowing the LLM to calculate business metrics, all KPIs are first computed using deterministic Pandas operations and business rules.

Only verified metrics are sent to Google Gemini for executive-level reasoning and report generation.

```
Dataset
    │
    ▼
Data Cleaning & Validation
    │
    ▼
Dataset Profiling
    │
    ▼
Business KPI Engine (Pandas)
    │
    ▼
Verified Metrics
    │
    ▼
Prompt Builder
    │
    ▼
Google Gemini
    │
    ▼
Executive Reports
Business Insights
AI Assistant
```

### Why this architecture?

✅ Prevents incorrect KPI calculations

✅ Keeps business metrics deterministic

✅ Reduces hallucination risk

✅ Produces explainable AI-generated reports

---

# ✨ Features

## 📂 Smart Dataset Upload

- CSV Support
- Excel Support
- Automatic preview
- Dataset pagination
- Download cleaned datasets

---

## 🧹 Automated Data Cleaning

DecisionAI automatically performs:

- Missing value detection
- Duplicate detection
- Data type validation
- Column standardization
- Data quality scoring
- Outlier detection
- Dataset profiling

---

## 🧠 Intelligent Dataset Analysis

Automatically generates:

- Dataset Summary
- Dataset Quality Score
- Dataset Completeness
- Dataset Type Detection
- Confidence Score
- Recommended KPIs
- Recommended Charts
- Business Opportunities

---

## 📊 Interactive Business Dashboard

Interactive Plotly dashboards include:

- Monthly Sales Trend
- Revenue Trend
- Profit Analysis
- Sales by Region
- Sales by Category
- Sales vs Profit
- Profit Margin
- Customer Distribution
- Top Customers
- Top Products
- Correlation Heatmap
- Quantity Analysis

---

## 📈 Business KPI Engine

DecisionAI automatically computes verified business metrics including:

- Total Revenue
- Total Profit
- Profit Margin
- Total Orders
- Total Customers
- Units Sold
- Average Discount
- Top Category
- Top Region
- Best-selling Products
- High Discount Products
- Negative Profit Transactions

All KPIs are calculated using deterministic Pandas operations before AI analysis.

---

## 🤖 AI Business Assistant

Powered by Google Gemini.

Ask natural language business questions such as:

- Explain this dashboard
- Generate Executive Summary
- Financial Analysis
- Marketing Strategy
- Risk Analysis
- CEO Report
- Business Opportunities
- Growth Recommendations

Example:

> Explain the dashboard and summarize the most important findings.

---

## 📑 AI Executive Report Generator

Automatically generates professional reports including:

- Executive Summary
- KPI Analysis
- Key Findings
- Business Insights
- Opportunities
- Challenges
- Risks
- Strategic Recommendations
- Conclusion

Designed for business stakeholders and executive management.

---

## 📤 Export Center

Export reports in multiple formats.

Supported exports:

- CSV
- Excel
- JSON KPI Report
- AI Executive Report

---

# 🛡️ AI Reliability

DecisionAI follows a hybrid analytics architecture to improve reliability.

Instead of relying on the language model to compute business metrics:

- KPIs are calculated using deterministic Pandas operations.
- Business rules are evaluated before AI reasoning.
- Verified metrics are passed to Google Gemini.
- Gemini focuses only on explanation, summarization, and strategic recommendations.

This approach significantly reduces hallucination risk while preserving the flexibility of natural language AI.

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Frontend | Streamlit |
| AI | Google Gemini API |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly |
| Excel Support | OpenPyXL |
| Configuration | Python-dotenv |
| Utilities | Regex, JSON |

---

# 📸 Screenshots

## Overview
<img width="1920" height="899" alt="Screenshot (2272)" src="https://github.com/user-attachments/assets/b0314e1c-5780-45e4-8141-6be562ea9e68" />
<img width="1866" height="895" alt="Screenshot (2273)" src="https://github.com/user-attachments/assets/44627a4f-c684-4760-b65b-9265b9a1e738" />
<img width="1894" height="894" alt="Screenshot (2274)" src="https://github.com/user-attachments/assets/43d97e03-b795-4131-b865-2a7d19b5d953" />
<img width="1867" height="914" alt="Screenshot (2275)" src="https://github.com/user-attachments/assets/59f3f365-b1df-414c-9797-bf0a7199f5ab" />
<img width="1887" height="899" alt="Screenshot (2276)" src="https://github.com/user-attachments/assets/bedd91ae-09f4-45d0-b172-2f9da9ac32a1" />
<img width="1900" height="902" alt="Screenshot (2278)" src="https://github.com/user-attachments/assets/4d964f6b-54fb-45ca-bb41-65fe4e00f8ca" />
<img width="1886" height="924" alt="Screenshot (2280)" src="https://github.com/user-attachments/assets/93d812c8-5d61-4f33-8db9-d6dff2deabf9" />

## Dashboard
<img width="1895" height="919" alt="Screenshot (2282)" src="https://github.com/user-attachments/assets/02a7cd28-3561-433c-9210-98d0dfb33a62" />
<img width="1864" height="907" alt="Screenshot (2283)" src="https://github.com/user-attachments/assets/0438def1-cd67-423b-b310-32727bc6889e" />
<img width="1880" height="879" alt="Screenshot (2286)" src="https://github.com/user-attachments/assets/e7eba0e9-752f-477c-a078-27cb508c8f23" />
<img width="1895" height="915" alt="Screenshot (2292)" src="https://github.com/user-attachments/assets/6ee49a2d-8799-42be-ac80-286d7d130fee" />

---

## AI Assistant
<img width="1891" height="907" alt="Screenshot (2293)" src="https://github.com/user-attachments/assets/96e5bfed-c44e-43d1-ac92-3f202b823135" />
<img width="1882" height="892" alt="Screenshot (2294)" src="https://github.com/user-attachments/assets/16795a94-934f-483c-ad1e-c8863a0442f9" />

---
## Export Center

<img width="1874" height="905" alt="Screenshot (2299)" src="https://github.com/user-attachments/assets/34e28735-3820-4dd2-bd0d-e8da9d2b99e2" />



---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/pruthvimkadri/DecisionAI-AI-Powered-Business-Intelligence-Platform.git
```

Navigate to the project

```bash
cd DecisionAI-AI-Powered-Business-Intelligence-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```
DecisionAI
│
├── app.py
├── requirements.txt
├── .env
│
├── components/
│   ├── overview.py
│   ├── dashboard.py
│   ├── reports.py
│   ├── ai_assistant.py
│   ├── export_page.py
│
├── utils/
│   ├── analytics.py
│   ├── ai_context.py
│   ├── dashboard.py
│   ├── data_cleaning.py
│   ├── export.py
│   ├── executive_summary.py
│   ├── dynamic_recommendation.py
│   ├── gpt_engine.py
│   ├── prompt_builder.py
│   └── report_generator.py
│
├── assets/
│
└── README.md
```

---

# 📊 Workflow

```
Upload Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Data Validation
        │
        ▼
Dataset Profiling
        │
        ▼
Business KPI Generation
        │
        ▼
Interactive Dashboard
        │
        ▼
Google Gemini
        │
        ▼
Executive Reports
        │
        ▼
Export Reports
```

---

# 🎯 Key Highlights

- Hybrid AI Architecture
- Deterministic KPI Engine
- AI Executive Reporting
- Interactive Plotly Dashboards
- Automated Data Cleaning
- Business Recommendation Engine
- Conversational AI Assistant
- Multi-format Export Support
- Dataset Profiling
- Data Quality Assessment

---

# 🚀 Roadmap

Future enhancements include:

- PDF Report Export
- Database Connectivity (PostgreSQL, Snowflake)
- Multi-user Authentication
- Role-based Dashboards
- Predictive Analytics
- Forecasting
- Time-series Analysis
- Scheduled Reports
- Cloud Data Warehouse Integration
- Real-time Data Streaming

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Pruthvi M

Computer Science Engineer | Data Science & AI Enthusiast

GitHub:

https://github.com/pruthvimkadri

---
