"""
====================================================
HR KPI Generator
====================================================

Generates KPIs for:
- Employee datasets
- HR Analytics
- Attrition Analysis
"""

import pandas as pd


def get_hr_kpis(df):
    """
    Generate HR KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Employees
    # =====================================

    kpis["👥 Total Employees"] = len(df)

    # =====================================
    # Average Salary
    # =====================================

    salary_col = get_column("salary")

    if salary_col:

        avg_salary = pd.to_numeric(
            df[salary_col],
            errors="coerce"
        ).mean()

        kpis["💰 Average Salary"] = f"${avg_salary:,.2f}"

    # =====================================
    # Highest Salary
    # =====================================

    if salary_col:

        highest_salary = pd.to_numeric(
            df[salary_col],
            errors="coerce"
        ).max()

        kpis["🏆 Highest Salary"] = f"${highest_salary:,.2f}"

    # =====================================
    # Department
    # =====================================

    dept_col = get_column("department")

    if dept_col:

        top_department = df[dept_col].mode()

        if not top_department.empty:

            kpis["🏢 Largest Department"] = top_department.iloc[0]

    # =====================================
    # Gender
    # =====================================

    gender_col = get_column("gender")

    if gender_col:

        gender = df[gender_col].mode()

        if not gender.empty:

            kpis["👤 Majority Gender"] = gender.iloc[0]

    # =====================================
    # Experience
    # =====================================

    exp_col = get_column("experience")

    if exp_col:

        avg_exp = pd.to_numeric(
            df[exp_col],
            errors="coerce"
        ).mean()

        kpis["📈 Avg Experience"] = f"{avg_exp:.1f} Years"

    # =====================================
    # Attrition
    # =====================================

    attrition_col = get_column("attrition")

    if attrition_col:

        attrition_rate = (
            df[attrition_col]
            .astype(str)
            .str.lower()
            .eq("yes")
            .mean()
            * 100
        )

        kpis["🚪 Attrition Rate"] = f"{attrition_rate:.1f}%"

    return kpis