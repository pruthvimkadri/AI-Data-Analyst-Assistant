"""
====================================================
Retail KPI Generator
====================================================

Generates KPIs for:
- Superstore
- Walmart
- Amazon Sales
- E-commerce Sales
- Retail Transactions
"""

import pandas as pd


def get_retail_kpis(df):
    """
    Generate Retail KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Helper function
    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # ============================
    # Total Orders
    # ============================

    kpis["🛒 Total Records"] = len(df)

    # ============================
    # Total Sales
    # ============================

    sales_col = get_column("sales")

    if sales_col:

        sales = pd.to_numeric(df[sales_col], errors="coerce").sum()

        kpis["💰 Total Sales"] = f"${sales:,.2f}"

    # ============================
    # Total Profit
    # ============================

    profit_col = get_column("profit")

    if profit_col:

        profit = pd.to_numeric(df[profit_col], errors="coerce").sum()

        kpis["📈 Total Profit"] = f"${profit:,.2f}"

    # ============================
    # Average Discount
    # ============================

    discount_col = get_column("discount")

    if discount_col:

        discount = pd.to_numeric(df[discount_col], errors="coerce").mean()

        kpis["🏷 Average Discount"] = f"{discount:.2%}"

    # ============================
    # Quantity Sold
    # ============================

    quantity_col = get_column("quantity")

    if quantity_col:

        qty = pd.to_numeric(df[quantity_col], errors="coerce").sum()

        kpis["📦 Units Sold"] = int(qty)

    # ============================
    # Top Category
    # ============================

    category_col = get_column("category")

    if category_col:

        top = df[category_col].mode()

        if not top.empty:

            kpis["🏆 Top Category"] = top.iloc[0]

    # ============================
    # Top Customer
    # ============================

    customer_col = get_column("customer_name")

    if customer_col:

        customer = df[customer_col].mode()

        if not customer.empty:

            kpis["👤 Top Customer"] = customer.iloc[0]

    # ============================
    # Top Region
    # ============================

    region_col = get_column("region")

    if region_col:

        region = df[region_col].mode()

        if not region.empty:

            kpis["🌍 Top Region"] = region.iloc[0]

    return kpis