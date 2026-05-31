# Data Analysis Agent

## Project Description

This project is a small intelligent software agent that automatically analyzes a CSV dataset.

The agent demonstrates:

- Perception (reading input data)
- Planning (selecting analysis steps)
- Decision Making (choosing analysis methods)
- Tool Use (Pandas and Matplotlib)
- Action (generating charts and reports)

The goal of the agent is to automatically analyze a dataset and generate useful insights.

---

## Project Structure

```text
AI-Data-Analysis-Agent/
│
├── agent.py
├── sample_data.csv
├── README.md
│
└── output/
    ├── report.md
    └── charts/
```

---

## Requirements

Python 3.10+

Install dependencies:

```bash
pip install pandas matplotlib
```

---

## How to Run

Open a terminal in the project folder and run:

```bash
python agent.py
```

---

## Expected Output

The agent will:

1. Read the CSV file
2. Detect column types
3. Choose analysis methods
4. Generate charts
5. Create a report

Output files:

```text
output/
├── report.md
└── charts/
```

---

## Agent Workflow

Perception

- Read CSV dataset

Planning

- Detect column types
- Select analysis strategy

Decision Making

- Numeric columns → Histogram + Statistics
- Categorical columns → Frequency Analysis

Tool Use

- Pandas
- Matplotlib

Action

- Generate report
- Generate charts

---

## Demo Video

(Insert your video link here)

Example:

https://drive.google.com/your-demo-video-link