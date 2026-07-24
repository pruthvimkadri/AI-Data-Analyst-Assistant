"""
====================================================
Finance KPI Generator
====================================================

Generates KPIs for:
- Financial Statements
- Revenue Analysis
- Expense Reports
- Profit & Loss
"""

import pandas as pd


def get_finance_kpis(df):
    """
    Generate Finance KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Records
    # =====================================

    kpis["📊 Total Records"] = len(df)

    # =====================================
    # Revenue
    # =====================================

    revenue_col = get_column("revenue")

    if revenue_col:

        revenue = pd.to_numeric(
            df[revenue_col],
            errors="coerce"
        ).sum()

        kpis["💰 Total Revenue"] = f"${revenue:,.2f}"

    # =====================================
    # Expenses
    # =====================================

    expense_col = get_column("expense")

    if expense_col is None:
        expense_col = get_column("expenses")

    if expense_col:

        expenses = pd.to_numeric(
            df[expense_col],
            errors="coerce"
        ).sum()

        kpis["💸 Total Expenses"] = f"${expenses:,.2f}"

    # =====================================
    # Profit
    # =====================================

    profit_col = get_column("profit")

    if profit_col:

        profit = pd.to_numeric(
            df[profit_col],
            errors="coerce"
        ).sum()

        kpis["📈 Total Profit"] = f"${profit:,.2f}"

    # =====================================
    # Average Transaction
    # =====================================

    transaction_col = get_column("transaction")

    if transaction_col:

        avg_transaction = pd.to_numeric(
            df[transaction_col],
            errors="coerce"
        ).mean()

        kpis["💳 Avg Transaction"] = f"${avg_transaction:,.2f}"

    # =====================================
    # Profit Margin
    # =====================================

    if revenue_col and profit_col:

        revenue = pd.to_numeric(
            df[revenue_col],
            errors="coerce"
        ).sum()

        profit = pd.to_numeric(
            df[profit_col],
            errors="coerce"
        ).sum()

        if revenue != 0:

            margin = (profit / revenue) * 100

            kpis["📊 Profit Margin"] = f"{margin:.2f}%"

    # =====================================
    # Average Cost
    # =====================================

    cost_col = get_column("cost")

    if cost_col:

        avg_cost = pd.to_numeric(
            df[cost_col],
            errors="coerce"
        ).mean()

        kpis["🏷 Avg Cost"] = f"${avg_cost:,.2f}"

    return kpis