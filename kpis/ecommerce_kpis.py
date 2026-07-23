"""
====================================================
E-Commerce KPI Generator
====================================================

Generates KPIs for:
- Amazon
- Flipkart
- Shopify
- Online Orders
"""

import pandas as pd


def get_ecommerce_kpis(df):
    """
    Generate E-Commerce KPIs.
    """

    kpis = {}

    columns = [col.lower().replace(" ", "_") for col in df.columns]

    def get_column(name):
        if name in columns:
            return df.columns[columns.index(name)]
        return None

    # =====================================
    # Total Orders
    # =====================================

    kpis["🛒 Total Orders"] = len(df)

    # =====================================
    # Total Revenue
    # =====================================

    revenue_col = get_column("revenue")

    if revenue_col is None:
        revenue_col = get_column("sales")

    if revenue_col:

        revenue = pd.to_numeric(
            df[revenue_col],
            errors="coerce"
        ).sum()

        kpis["💰 Total Revenue"] = f"${revenue:,.2f}"

    # =====================================
    # Average Order Value
    # =====================================

    if revenue_col:

        avg_order = pd.to_numeric(
            df[revenue_col],
            errors="coerce"
        ).mean()

        kpis["🧾 Average Order Value"] = f"${avg_order:,.2f}"

    # =====================================
    # Total Customers
    # =====================================

    customer_col = get_column("customer_name")

    if customer_col is None:
        customer_col = get_column("customer")

    if customer_col:

        total_customers = df[customer_col].nunique()

        kpis["👤 Unique Customers"] = total_customers

    # =====================================
    # Total Quantity
    # =====================================

    quantity_col = get_column("quantity")

    if quantity_col:

        qty = pd.to_numeric(
            df[quantity_col],
            errors="coerce"
        ).sum()

        kpis["📦 Items Sold"] = int(qty)

    # =====================================
    # Top Category
    # =====================================

    category_col = get_column("category")

    if category_col:

        category = df[category_col].mode()

        if not category.empty:

            kpis["🏆 Top Category"] = category.iloc[0]

    # =====================================
    # Payment Method
    # =====================================

    payment_col = get_column("payment_method")

    if payment_col:

        payment = df[payment_col].mode()

        if not payment.empty:

            kpis["💳 Popular Payment"] = payment.iloc[0]

    # =====================================
    # Order Status
    # =====================================

    status_col = get_column("order_status")

    if status_col:

        status = df[status_col].mode()

        if not status.empty:

            kpis["📋 Common Status"] = status.iloc[0]

    return kpis