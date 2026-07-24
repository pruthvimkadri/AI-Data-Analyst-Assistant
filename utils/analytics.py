"""
====================================================
DecisionAI Analytics Engine
====================================================

This module contains reusable analytical functions.

Functions:
- find_column()
- get_numeric_columns()
- calculate_kpis()
"""

import pandas as pd
import numpy as np


# ====================================================
# Column Detection
# ====================================================

def find_column(df, possible_names):
    """
    Finds the first matching column from a list of
    possible names.

    Example:
        find_column(df, ["sales","revenue"])
    """

    columns = {
        c.lower().strip(): c
        for c in df.columns
    }

    # Exact match
    for name in possible_names:
        if name.lower() in columns:
            return columns[name.lower()]

    # Partial match
    for lower_name, original in columns.items():
        for name in possible_names:
            if name.lower() in lower_name:
                return original

    return None


# ====================================================
# Numeric Columns
# ====================================================

def get_numeric_columns(df):
    """
    Returns all numeric columns.
    """

    return df.select_dtypes(
        include=np.number
    ).columns.tolist()


# ====================================================
# KPI Calculation
# ====================================================

def calculate_kpis(df):
    """
    Automatically calculate KPIs based on
    available columns.
    """

    sales = find_column(
        df,
        [
            "sales",
            "sales amount",
            "revenue",
            "total sales",
            "sales_value"
        ]
    )

    profit = find_column(
        df,
        [
            "profit",
            "net profit",
            "gross profit",
            "margin"
        ]
    )

    customer = find_column(
        df,
        [
            "customer",
            "customer id",
            "customer name",
            "client"
        ]
    )

    order = find_column(
        df,
        [
            "order",
            "order id"
        ]
    )

    product = find_column(
        df,
        [
            "product",
            "product name"
        ]
    )

    quantity = find_column(
        df,
        [
            "quantity",
            "qty"
        ]
    )

    discount = find_column(
        df,
        [
            "discount"
        ]
    )

    kpis = {}

    # ----------------------------------------
    # Sales KPIs
    # ----------------------------------------

    if sales:

        kpis["Total Sales"] = round(
            df[sales].sum(),
            2
        )

        kpis["Average Sale"] = round(
            df[sales].mean(),
            2
        )

        kpis["Maximum Sale"] = round(
            df[sales].max(),
            2
        )

        kpis["Minimum Sale"] = round(
            df[sales].min(),
            2
        )

    # ----------------------------------------
    # Profit KPIs
    # ----------------------------------------

    if profit:

        kpis["Total Profit"] = round(
            df[profit].sum(),
            2
        )

    if sales and profit:

        total_sales = df[sales].sum()

        if total_sales != 0:

            kpis["Profit Margin"] = round(
                (df[profit].sum() / total_sales) * 100,
                2
            )

    # ----------------------------------------
    # Customer KPIs
    # ----------------------------------------

    if customer:

        kpis["Unique Customers"] = (
            df[customer].nunique()
        )

    # ----------------------------------------
    # Order KPIs
    # ----------------------------------------

    if order:

        total_orders = df[order].nunique()

        kpis["Total Orders"] = total_orders

        if sales and total_orders > 0:

            kpis["Average Order Value"] = round(
                df[sales].sum() / total_orders,
                2
            )

    # ----------------------------------------
    # Product KPIs
    # ----------------------------------------

    if product:

        kpis["Unique Products"] = (
            df[product].nunique()
        )

    # ----------------------------------------
    # Quantity KPIs
    # ----------------------------------------

    if quantity:

        kpis["Total Quantity"] = round(
            df[quantity].sum(),
            2
        )

    # ----------------------------------------
    # Customer Value
    # ----------------------------------------

    if sales and customer:

        total_customers = df[customer].nunique()

        if total_customers > 0:

            kpis["Average Customer Value"] = round(
                df[sales].sum() / total_customers,
                2
            )

    # ----------------------------------------
    # Discount
    # ----------------------------------------

    if discount:

        kpis["Average Discount"] = round(
            df[discount].mean(),
            2
        )

        kpis["Maximum Discount"] = round(
            df[discount].max(),
            2
        )

    return kpis
# ====================================================
# Trend Analysis
# ====================================================

def trend_analysis(df):
    """
    Returns monthly sales trend.
    """

    date_col = find_column(
        df,
        [
            "order date",
            "date",
            "invoice date",
            "purchase date"
        ]
    )

    sales_col = find_column(
        df,
        [
            "sales",
            "sales amount",
            "revenue",
            "total sales"
        ]
    )

    if not date_col or not sales_col:
        return None

    temp = df.copy()

    temp[date_col] = pd.to_datetime(
        temp[date_col],
        errors="coerce"
    )

    temp = temp.dropna(subset=[date_col])

    if temp.empty:
        return None

    trend = (
        temp.groupby(
            temp[date_col].dt.to_period("M")
        )[sales_col]
        .sum()
        .reset_index()
    )

    trend[date_col] = trend[date_col].astype(str)

    return trend


# ====================================================
# Region Analysis
# ====================================================

def region_analysis(df):
    """
    Sales grouped by region.
    """

    region_col = find_column(
        df,
        [
            "region",
            "state",
            "zone",
            "location"
        ]
    )

    sales_col = find_column(
        df,
        [
            "sales",
            "sales amount",
            "revenue"
        ]
    )

    if not region_col or not sales_col:
        return None

    summary = (
        df.groupby(region_col)[sales_col]
        .agg(["sum", "mean", "count"])
        .reset_index()
    )

    summary.columns = [
        region_col,
        "Total Sales",
        "Average Sales",
        "Orders"
    ]

    summary = summary.sort_values(
        "Total Sales",
        ascending=False
    )

    return summary


# ====================================================
# Category Analysis
# ====================================================

def category_analysis(df):
    """
    Sales grouped by category.
    """

    category_col = find_column(
        df,
        [
            "category",
            "product category",
            "segment"
        ]
    )

    sales_col = find_column(
        df,
        [
            "sales",
            "sales amount",
            "revenue"
        ]
    )

    if not category_col or not sales_col:
        return None

    summary = (
        df.groupby(category_col)[sales_col]
        .agg(["sum", "mean", "count"])
        .reset_index()
    )

    summary.columns = [
        category_col,
        "Total Sales",
        "Average Sales",
        "Orders"
    ]

    summary = summary.sort_values(
        "Total Sales",
        ascending=False
    )

    return summary


# ====================================================
# Customer Analysis
# ====================================================

def customer_analysis(df):
    """
    Top customers by sales.
    """

    customer_col = find_column(
        df,
        [
            "customer",
            "customer id",
            "customer name",
            "client"
        ]
    )

    sales_col = find_column(
        df,
        [
            "sales",
            "sales amount",
            "revenue"
        ]
    )

    if not customer_col or not sales_col:
        return None

    summary = (
        df.groupby(customer_col)[sales_col]
        .agg(["sum", "mean", "count"])
        .reset_index()
    )

    summary.columns = [
        customer_col,
        "Total Sales",
        "Average Sales",
        "Orders"
    ]

    summary = summary.sort_values(
        "Total Sales",
        ascending=False
    )

    return summary


# ====================================================
# Top Customers
# ====================================================

def top_customers(df, n=10):
    """
    Returns top N customers.
    """

    customer_df = customer_analysis(df)

    if customer_df is None:
        return None

    return customer_df.head(n)
# ====================================================
# Missing Value Analysis
# ====================================================

def analyze_missing_values(df):
    """
    Analyze missing values in the dataset.
    Returns a dictionary containing summary statistics.
    """

    missing = df.isnull().sum()

    total_missing = int(missing.sum())

    if total_missing == 0:

        return {
            "total_missing": 0,
            "columns": {},
            "summary": ["✅ No missing values found."]
        }

    columns = {}

    summary = [
        f"🧹 Total Missing Values: {total_missing}"
    ]

    for col, count in missing.items():

        if count > 0:

            percentage = round(
                (count / len(df)) * 100,
                2
            )

            columns[col] = {
                "count": int(count),
                "percentage": percentage
            }

            summary.append(
                f"{col}: {count} ({percentage}%)"
            )

    return {
        "total_missing": total_missing,
        "columns": columns,
        "summary": summary
    }


# ====================================================
# Outlier Detection
# ====================================================

def detect_outliers(df):
    """
    Detect outliers using the IQR method.
    Returns a DataFrame.
    """

    results = []

    numeric_columns = get_numeric_columns(df)

    for column in numeric_columns:

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - (1.5 * iqr)
        upper = q3 + (1.5 * iqr)

        count = (
            (df[column] < lower) |
            (df[column] > upper)
        ).sum()

        results.append({

            "Column": column,

            "Outliers": int(count),

            "Lower Bound": round(lower,2),

            "Upper Bound": round(upper,2)

        })

    return pd.DataFrame(results)


# ====================================================
# Correlation Analysis
# ====================================================

def correlation_analysis(df):
    """
    Returns correlation matrix.
    """

    numeric = df.select_dtypes(
        include=np.number
    )

    if numeric.shape[1] < 2:

        return None

    return numeric.corr()


# ====================================================
# Data Quality Score
# ====================================================

def data_quality_score(df):
    """
    Calculates a simple data quality score.
    """

    score = 100

    missing = int(df.isnull().sum().sum())

    duplicates = int(df.duplicated().sum())

    if len(df) > 0:

        score -= min(
            (missing / len(df)) * 10,
            30
        )

    score -= min(
        duplicates,
        20
    )

    score = max(
        0,
        round(score)
    )

    return score


# ====================================================
# Business Health Score
# ====================================================

def business_health_score(kpis):
    """
    Calculates business health based on KPIs.
    """

    score = 100

    margin = kpis.get(
        "Profit Margin",
        0
    )

    if margin < 5:

        score -= 40

    elif margin < 10:

        score -= 25

    elif margin < 20:

        score -= 10

    return max(
        score,
        0
    )


# ====================================================
# Dataset Overview
# ====================================================

def dataset_overview(df):
    """
    Returns dataset metadata.
    """

    return {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Numeric Columns":
            len(get_numeric_columns(df)),

        "Categorical Columns":
            len(
                df.select_dtypes(
                    exclude=np.number
                ).columns
            ),

        "Memory Usage (MB)":
            round(
                df.memory_usage(
                    deep=True
                ).sum() / (1024 * 1024),
                2
            )

    }


# ====================================================
# Executive Summary
# ====================================================

def executive_summary(df):
    """
    Creates a quick summary dictionary
    for the dashboard.
    """

    return {

        "overview": dataset_overview(df),

        "kpis": calculate_kpis(df),

        "quality_score": data_quality_score(df),

        "missing": analyze_missing_values(df),

        "outliers": detect_outliers(df)

    }