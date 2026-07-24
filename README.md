# 🚀 DecisionAI – AI-Powered Business Intelligence Platform

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge&logo=google)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?style=for-the-badge&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>
---
## 🌐 Live Demo

🚀 **Try DecisionAI here**

**https://ai-data-analyst-assistant-dihdjusjw4ciry6rcv5bhf.streamlit.app/**
---

## 📊 Overview

DecisionAI is an **AI-powered Business Intelligence platform** that transforms raw business datasets into interactive dashboards, automated KPI reports, executive summaries, and AI-generated strategic recommendations.

Instead of manually analyzing spreadsheets, users can simply upload a CSV or Excel file and let DecisionAI automatically:

- Clean and validate data
- Perform Exploratory Data Analysis (EDA)
- Build interactive dashboards
- Generate KPIs
- Produce executive reports
- Answer business questions using Google Gemini AI

---

## ✨ Features

### 📂 Smart Data Upload
- CSV & Excel support
- Automatic dataset preview
- Pagination for large datasets
- Download filtered datasets

---

### 🧹 Automated Data Cleaning

- Missing value detection
- Duplicate removal
- Data type validation
- Dataset quality scoring
- Column standardization

---

### 📈 Interactive Business Dashboard

Generate interactive dashboards with:

- 📈 Monthly Sales Trend
- 💰 Monthly Revenue
- 🌍 Sales by Region
- 📦 Sales by Category
- 👥 Customer Segmentation
- 🏆 Top Customers
- 📦 Top Products
- 📊 Quantity Sold
- 💹 Profit Margin
- 📉 Sales vs Profit Analysis
- 🔥 Correlation Heatmap
- 📊 Customer Distribution

Built using Plotly for interactive exploration.

---

### 🤖 AI Business Assistant

Powered by **Google Gemini**, DecisionAI can answer business questions such as:

- Explain this dashboard
- Generate executive summary
- Identify business risks
- Financial analysis
- Marketing strategy
- Growth opportunities
- CEO reports

Example:

> "Explain the dashboard and summarize the most important findings."

---

### 📑 AI Report Generator

Automatically generates professional reports including:

- Executive Summary
- KPI Analysis
- Business Insights
- Opportunities
- Challenges
- Risks
- Recommendations
- Conclusion

Perfect for business stakeholders and executives.

---

### 📤 Export Center

Export results in multiple formats:

- CSV
- Excel
- JSON KPI Report
- AI Generated Report

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| AI | Google Gemini API |
| Data Analysis | Pandas, NumPy |
| Visualization | Plotly |
| Excel Support | OpenPyXL |
| Configuration | dotenv |
| Others | Regex, JSON |

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
git clone https://github.com/yourusername/DecisionAI.git

cd DecisionAI
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
DecisionAI/
│
├── app.py
├── requirements.txt
├── .env
│
├── pages/
│   ├── overview.py
│   ├── dashboard.py
│   ├── reports.py
│   ├── export.py
│
├── utils/
│   ├── ai_context.py
│   ├── analytics.py
│   ├── dashboard.py
│   ├── data_cleaning.py
│   ├── export.py
│   ├── gpt_engine.py
│   ├── prompt_builder.py
│   └── report_generator.py
│
├── assets/
│
├── images/
│
└── README.md
```

---

# 📊 Workflow

```
Upload Dataset
        │
        ▼
Automatic Data Cleaning
        │
        ▼
Dataset Validation
        │
        ▼
Interactive Dashboard
        │
        ▼
KPI Generation
        │
        ▼
AI Business Analysis
        │
        ▼
Executive Reports
        │
        ▼
Export Reports
```

---

# 🎯 Key Highlights

- End-to-End Business Intelligence Platform
- AI-Powered Executive Reporting
- Interactive Plotly Dashboards
- Automated KPI Generation
- Natural Language Business Analysis
- Exportable Reports
- Business Recommendations using Google Gemini

---

# 🌟 Future Improvements

- PDF Report Export
- Multi-language Support
- Database Connectivity
- User Authentication
- Cloud Deployment
- Role-based Dashboards
- Forecasting & Predictive Analytics
- Real-time Data Streaming

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Pruthvi M**

Data Science & AI Enthusiast

GitHub: https://github.com/pruthvimkadri



