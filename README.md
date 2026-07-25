# 🚀  AI Project Health Reporting Agent

> **An AI-powered Project Health Reporting System built using LangChain, Groq Llama 3.3, and Pydantic to automate enterprise project health assessment through a custom RAG (Red–Amber–Green) framework.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agent-success?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Llama--3.3-orange?style=for-the-badge)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</p>

---

# 📌 Overview

Professional Services teams often manage multiple enterprise implementations simultaneously. Monitoring project health manually becomes increasingly difficult as project complexity grows.

This project automates project health assessment by leveraging **Large Language Models (LLMs)** to analyze raw project data, evaluate project health using a custom **RAG (Red–Amber–Green)** framework, identify missing information, and generate executive-ready reports.

The solution also includes an automated scheduler capable of periodically scanning project files and generating updated health reports.

---

# 🎯 Problem Statement

Leadership requires a centralized system capable of:

* Monitoring multiple ongoing projects
* Detecting project risks automatically
* Explaining project health in plain English
* Handling incomplete or inconsistent project data
* Producing executive-ready reports without manual intervention

This project addresses these challenges using AI-driven project analysis and automated reporting.

---

# ✨ Features

* 🤖 AI-powered Project Health Assessment
* 📊 Custom Weighted RAG Scoring Framework
* 🛡 Graceful Handling of Missing Data
* 📝 Executive-Level Reasoning Generation
* 📁 Structured JSON Report Generation
* ⏰ Automated Weekly Scheduler
* 🔒 Secure API Key Management using `.env`
* ⚡ Fast LLM Inference using Groq Llama 3.3
* 📈 Executive Summary Generation

---

# 🏗️ System Architecture

```text
                Project JSON Files
                        │
                        ▼
               Data Validation Layer
                        │
                        ▼
        AI Project Health Reporting Agent
                        │
                        ▼
        Weighted RAG Evaluation Framework
                        │
                        ▼
        Missing Data Detection & Recovery
                        │
                        ▼
        Executive Reasoning Generation
                        │
                        ▼
        Structured JSON Health Report
                        │
                        ▼
          Automated Weekly Scheduler
```

---

# 📂 Project Structure

```text
zycus-project-health-agent/
│
├── data/
│   ├── project_alpha.json
│   └── project_beta.json
│
├── outputs/
│   ├── report_project_alpha.json
│   └── report_project_beta.json
│
├── presentation/
│   └── Executive_Project_Health_Report.pptx
│
├── docs/
│   └── RAG_Methodology.pdf
│
├── .env.example
├── .gitignore
├── requirements.txt
├── agent.py
├── scheduler.py
└── README.md
```

---

# ⚙️ Technology Stack

| Category               | Technology              |
| ---------------------- | ----------------------- |
| Programming Language   | Python 3.11             |
| AI Framework           | LangChain               |
| Large Language Model   | Llama-3.3-70B-Versatile |
| API Provider           | Groq                    |
| Data Validation        | Pydantic v2             |
| Environment Management | python-dotenv           |
| Data Format            | JSON                    |
| Automation             | Python Scheduler        |

---

# 🧠 RAG Health Evaluation Framework

Each project is evaluated using a weighted scoring matrix.

## Health Score

| Score | Meaning  |
| ----- | -------- |
| 🟢 0  | On Track |
| 🟠 1  | At Risk  |
| 🔴 2  | Critical |

---

## Evaluation Parameters

| Metric                     | Weight |
| -------------------------- | -----: |
| 📅 Schedule Slippage       |    25% |
| 💰 Budget Burn Rate        |    25% |
| 🎯 Milestone Health        |    20% |
| 🚧 Blockers & Dependencies |    15% |
| 😊 Stakeholder Sentiment   |    15% |

---

## 🚨 Fail-Safe Business Rule

To ensure critical issues are never hidden by weighted averages, the following rule is enforced:

> **If any evaluation parameter receives a score of 2 (Critical), the overall project status is automatically classified as RED regardless of the final weighted score.**

---

# 🛡 Handling Incomplete Data

Real-world project data is often inconsistent or incomplete.

Instead of failing during execution, the agent automatically:

* Detects missing values
* Applies safe default scores
* Logs all missing fields
* Continues processing without interruption
* Includes identified data gaps in the final report

This approach makes the solution resilient and production-friendly.

---

# ⚡ Workflow

```text
Project JSON Files
        │
        ▼
Validate Input Data
        │
        ▼
LLM Analysis (Groq Llama 3.3)
        │
        ▼
Weighted RAG Evaluation
        │
        ▼
Executive Reasoning
        │
        ▼
Generate Structured JSON Report
        │
        ▼
Store Output
        │
        ▼
Repeat via Scheduler
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <repository-url>

cd zycus-project-health-agent
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```text
GROQ_API_KEY=your_groq_api_key_here
```

---

## 5. Execute the Scheduler

```bash
python scheduler.py
```

The scheduler will:

* Scan all project JSON files inside the `data/` directory.
* Analyze each project using the AI agent.
* Generate structured health reports.
* Store reports in the `outputs/` directory.
* Continue running in the background.

Stop execution anytime using:

```text
Ctrl + C
```

---

# 📄 Sample Output

```json
{
  "project_name": "Project Alpha",
  "overall_rag_status": "RED",
  "dimension_scores": {
    "schedule": 2,
    "budget": 0,
    "milestones": 1,
    "blockers": 2,
    "sentiment": 1
  },
  "executive_reasoning": "Critical schedule delays and unresolved blockers require immediate leadership attention.",
  "data_gaps_identified": [
    "Budget information unavailable"
  ]
}
```

---

# 📊 Example Findings

| Project          | Status | Executive Insight                                                                      |
| ---------------- | ------ | -------------------------------------------------------------------------------------- |
| 🔴 Project Alpha | RED    | Critical operational risks due to environment downtime and missing budget information. |
| 🟠 Project Beta  | AMBER  | Early-stage budget overburn indicates a need for closer financial monitoring.          |

---

---

# 📦 Dependencies

```text
langchain==0.1.20
langchain-groq==0.1.3
pydantic==2.7.1
pandas==2.2.2
openpyxl==3.1.2
python-dotenv==1.0.1
```

---

# 🔮 Future Enhancements

* 📊 Interactive Dashboard (Streamlit)
* ☁️ Cloud Deployment
* 📈 Historical Trend Analysis
* 📧 Automated Email Reporting
* 🔔 Slack / Microsoft Teams Notifications
* 📅 CRON-Based Scheduling
* 📉 Portfolio-Level Risk Analytics
* 📂 Excel & CSV Data Support
* 📊 Power BI Integration

---

# 👨‍💻 Author

**Ankush Yadav**



