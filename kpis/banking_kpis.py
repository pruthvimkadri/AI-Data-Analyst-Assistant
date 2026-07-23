"""
====================================================
Banking KPI Generator
====================================================

Generates KPIs for:
- Banking Transactions
- Customer Accounts
- Loan Analytics
- Credit Card Analytics
"""

import pandas as pd


def get_banking_kpis(df):
    """
    Generate Banking KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Customers
    # =====================================

    kpis["🏦 Total Customers"] = len(df)

    # =====================================
    # Total Balance
    # =====================================

    balance_col = get_column("balance")

    if balance_col:

        balance = pd.to_numeric(
            df[balance_col],
            errors="coerce"
        ).sum()

        kpis["💰 Total Balance"] = f"${balance:,.2f}"

    # =====================================
    # Average Balance
    # =====================================

    if balance_col:

        avg_balance = pd.to_numeric(
            df[balance_col],
            errors="coerce"
        ).mean()

        kpis["📈 Average Balance"] = f"${avg_balance:,.2f}"

    # =====================================
    # Total Loan Amount
    # =====================================

    loan_col = get_column("loan_amount")

    if loan_col is None:
        loan_col = get_column("loan")

    if loan_col:

        total_loan = pd.to_numeric(
            df[loan_col],
            errors="coerce"
        ).sum()

        kpis["🏠 Total Loans"] = f"${total_loan:,.2f}"

    # =====================================
    # Account Type
    # =====================================

    account_col = get_column("account_type")

    if account_col:

        account = df[account_col].mode()

        if not account.empty:

            kpis["💳 Popular Account"] = account.iloc[0]

    # =====================================
    # Branch
    # =====================================

    branch_col = get_column("branch")

    if branch_col:

        branch = df[branch_col].mode()

        if not branch.empty:

            kpis["🏢 Largest Branch"] = branch.iloc[0]

    # =====================================
    # Customer Type
    # =====================================

    customer_col = get_column("customer_type")

    if customer_col:

        customer = df[customer_col].mode()

        if not customer.empty:

            kpis["👤 Customer Type"] = customer.iloc[0]

    # =====================================
    # Credit Score
    # =====================================

    score_col = get_column("credit_score")

    if score_col:

        score = pd.to_numeric(
            df[score_col],
            errors="coerce"
        ).mean()

        kpis["⭐ Avg Credit Score"] = f"{score:.1f}"

    return kpis