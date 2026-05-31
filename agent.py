import pandas as pd
import matplotlib.pyplot as plt
import os

print("=== Data Analysis Agent Started ===")
print("Goal: Analyze a CSV dataset and generate useful insights.")

# --------------------
# Perception
# --------------------
print("\n[Perception]")
print("Reading dataset from sample_data.csv ...")

df = pd.read_csv("sample_data.csv")

print("\nDataset preview:")
print(df.head())

# --------------------
# Planning
# --------------------
print("\n[Planning]")

plan = [
    "Detect column types",
    "Choose suitable analysis methods",
    "Generate visualizations",
    "Create a written report"
]

for step in plan:
    print("->", step)

# --------------------
# Tool preparation
# --------------------
os.makedirs("output/charts", exist_ok=True)

report = []

report.append("# Data Analysis Report\n")
report.append("## Agent Goal")
report.append("The goal of this agent is to automatically analyze a CSV dataset and generate useful insights.\n")

report.append("## Agent Workflow")
report.append("1. Perception: read the CSV file.")
report.append("2. Planning: decide which analysis steps are needed.")
report.append("3. Tool Use: use pandas for data analysis and matplotlib for visualization.")
report.append("4. Action: generate charts and a markdown report.\n")

report.append("## Dataset Overview")
report.append(f"Rows: {len(df)}")
report.append(f"Columns: {len(df.columns)}\n")

# --------------------
# Reasoning + Decision Making
# --------------------
print("\n[Reasoning and Decision Making]")

for column in df.columns:

    print(f"\nEvaluating column: {column}")

    if pd.api.types.is_numeric_dtype(df[column]):

        print("Decision: Numeric column detected -> generate summary statistics and histogram.")

        report.append(f"\n## Numeric Column: {column}")
        report.append(f"Mean = {df[column].mean():.2f}")
        report.append(f"Max = {df[column].max()}")
        report.append(f"Min = {df[column].min()}")

        plt.figure()
        df[column].hist()
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        chart_path = f"output/charts/{column}_hist.png"
        plt.savefig(chart_path)
        plt.close()

        report.append(f"Chart generated: {chart_path}")

    else:

        print("Decision: Categorical column detected -> generate frequency analysis.")

        report.append(f"\n## Categorical Column: {column}")

        counts = df[column].value_counts()

        report.append("Frequency count:")
        report.append(str(counts))

# --------------------
# Additional agent insight
# --------------------
report.append("\n## Agent Summary")
report.append("The agent inspected the dataset, identified numeric and categorical columns, selected appropriate analysis actions, generated charts for numeric columns, and produced this report automatically.")

# --------------------
# Action
# --------------------
print("\n[Action]")
print("Generating report and charts...")

with open(
    "output/report.md",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(report))

print("Analysis complete!")
print("Report saved to output/report.md")
print("Charts saved to output/charts/")