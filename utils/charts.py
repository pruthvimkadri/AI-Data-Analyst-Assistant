"""
====================================================
DecisionAI Charts Engine
====================================================

Professional Plotly charts for DecisionAI.

Part A
-------
✓ Sales Trend
✓ Sales by Region
✓ Sales by Category
✓ Monthly Revenue
"""

import pandas as pd
import plotly.express as px

from .analytics import find_column


# ====================================================
# Sales Trend Chart
# ====================================================

def sales_trend_chart(df):
    """
    Creates a monthly sales trend line chart.
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

    fig = px.line(
        trend,
        x=date_col,
        y=sales_col,
        title="Monthly Sales Trend",
        markers=True
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Month",
        yaxis_title="Sales"
    )

    return fig


# ====================================================
# Monthly Revenue Chart
# ====================================================

def monthly_revenue_chart(df):
    """
    Monthly revenue bar chart.
    """

    date_col = find_column(
        df,
        [
            "order date",
            "date",
            "invoice date"
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

    if not date_col or not sales_col:
        return None

    temp = df.copy()

    temp[date_col] = pd.to_datetime(
        temp[date_col],
        errors="coerce"
    )

    temp = temp.dropna(subset=[date_col])

    revenue = (
        temp.groupby(
            temp[date_col].dt.to_period("M")
        )[sales_col]
        .sum()
        .reset_index()
    )

    revenue[date_col] = revenue[date_col].astype(str)

    fig = px.bar(
        revenue,
        x=date_col,
        y=sales_col,
        title="Monthly Revenue"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Month",
        yaxis_title="Revenue"
    )

    return fig


# ====================================================
# Region Sales Chart
# ====================================================

def region_sales_chart(df):
    """
    Sales by region.
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
        .sum()
        .reset_index()
        .sort_values(
            sales_col,
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x=region_col,
        y=sales_col,
        title="Sales by Region",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Region",
        yaxis_title="Sales"
    )

    return fig


# ====================================================
# Category Sales Chart
# ====================================================

def category_sales_chart(df):
    """
    Sales by category.
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
        .sum()
        .reset_index()
        .sort_values(
            sales_col,
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x=category_col,
        y=sales_col,
        title="Sales by Category",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Category",
        yaxis_title="Sales"
    )

    return fig


# ====================================================
# Segment Sales Chart
# ====================================================

def segment_sales_chart(df):
    """
    Sales by customer segment.
    """

    segment_col = find_column(
        df,
        [
            "segment",
            "customer segment"
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

    if not segment_col or not sales_col:
        return None

    summary = (
        df.groupby(segment_col)[sales_col]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        summary,
        names=segment_col,
        values=sales_col,
        title="Sales by Segment"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig
# ====================================================
# Top Customers Chart
# ====================================================

def top_customers_chart(df, top_n=10):
    """
    Bar chart showing the top N customers by sales.
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
        .sum()
        .reset_index()
        .sort_values(
            sales_col,
            ascending=False
        )
        .head(top_n)
    )

    fig = px.bar(
        summary,
        x=customer_col,
        y=sales_col,
        title=f"Top {top_n} Customers",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Customer",
        yaxis_title="Sales"
    )

    return fig


# ====================================================
# Customer Distribution Chart
# ====================================================

def customer_distribution_chart(df):
    """
    Distribution of orders across customers.
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

    if not customer_col:
        return None

    summary = (
        df[customer_col]
        .value_counts()
        .reset_index()
    )

    summary.columns = [
        customer_col,
        "Orders"
    ]

    fig = px.histogram(
        summary,
        x="Orders",
        nbins=20,
        title="Customer Order Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Orders",
        yaxis_title="Number of Customers"
    )

    return fig


# ====================================================
# Top Products Chart
# ====================================================

def top_products_chart(df, top_n=10):
    """
    Top-selling products.
    """

    product_col = find_column(
        df,
        [
            "product",
            "product name",
            "item"
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

    if not product_col or not sales_col:
        return None

    summary = (
        df.groupby(product_col)[sales_col]
        .sum()
        .reset_index()
        .sort_values(
            sales_col,
            ascending=False
        )
        .head(top_n)
    )

    fig = px.bar(
        summary,
        x=product_col,
        y=sales_col,
        title=f"Top {top_n} Products",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Product",
        yaxis_title="Sales"
    )

    return fig


# ====================================================
# Quantity by Category Chart
# ====================================================

def quantity_chart(df):
    """
    Quantity sold by category.
    """

    category_col = find_column(
        df,
        [
            "category",
            "product category",
            "segment"
        ]
    )

    quantity_col = find_column(
        df,
        [
            "quantity",
            "qty"
        ]
    )

    if not category_col or not quantity_col:
        return None

    summary = (
        df.groupby(category_col)[quantity_col]
        .sum()
        .reset_index()
        .sort_values(
            quantity_col,
            ascending=False
        )
    )

    fig = px.bar(
        summary,
        x=category_col,
        y=quantity_col,
        title="Quantity Sold by Category",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Category",
        yaxis_title="Quantity"
    )

    return fig


# ====================================================
# Product Performance Chart
# ====================================================

def product_performance_chart(df, top_n=15):
    """
    Product performance based on total sales.
    """

    product_col = find_column(
        df,
        [
            "product",
            "product name",
            "item"
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

    if not product_col or not sales_col:
        return None

    summary = (
        df.groupby(product_col)[sales_col]
        .sum()
        .reset_index()
        .sort_values(
            sales_col,
            ascending=False
        )
        .head(top_n)
    )

    fig = px.bar(
        summary,
        x=sales_col,
        y=product_col,
        orientation="h",
        title=f"Top {top_n} Products by Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Sales",
        yaxis_title="Product"
    )

    return fig
# ====================================================
# Sales vs Profit Scatter Chart
# ====================================================

def sales_profit_scatter(df):
    """
    Scatter plot comparing Sales and Profit.
    """

    sales_col = find_column(
        df,
        [
            "sales",
            "sales amount",
            "revenue"
        ]
    )

    profit_col = find_column(
        df,
        [
            "profit",
            "net profit",
            "gross profit"
        ]
    )

    if not sales_col or not profit_col:
        return None

    fig = px.scatter(
        df,
        x=sales_col,
        y=profit_col,
        title="Sales vs Profit",
        opacity=0.75,
        trendline="ols"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Sales",
        yaxis_title="Profit"
    )

    return fig


# ====================================================
# Profit Margin Chart
# ====================================================

def profit_margin_chart(df):
    """
    Profit margin by category.
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

    profit_col = find_column(
        df,
        [
            "profit",
            "net profit",
            "gross profit"
        ]
    )

    if not category_col or not sales_col or not profit_col:
        return None

    summary = (
        df.groupby(category_col)
        .agg(
            Sales=(sales_col, "sum"),
            Profit=(profit_col, "sum")
        )
        .reset_index()
    )

    summary["Profit Margin (%)"] = (
        summary["Profit"] / summary["Sales"] * 100
    ).round(2)

    fig = px.bar(
        summary,
        x=category_col,
        y="Profit Margin (%)",
        title="Profit Margin by Category",
        text_auto=".2f"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Category",
        yaxis_title="Profit Margin (%)"
    )

    return fig


# ====================================================
# Missing Values Chart
# ====================================================

def missing_values_chart(df):
    """
    Bar chart showing missing values.
    """

    missing = (
        df.isnull()
        .sum()
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing Values"
    ]

    missing = missing[
        missing["Missing Values"] > 0
    ]

    if missing.empty:
        return None

    fig = px.bar(
        missing,
        x="Column",
        y="Missing Values",
        title="Missing Values by Column",
        text_auto=True
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


# ====================================================
# Correlation Heatmap
# ====================================================

def correlation_heatmap(df):
    """
    Correlation heatmap.
    """

    numeric = df.select_dtypes(
        include="number"
    )

    if numeric.shape[1] < 2:
        return None

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="Correlation Heatmap",
        color_continuous_scale="RdBu_r"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


# ====================================================
# Dashboard Charts
# ====================================================

def dashboard_charts(df):
    """
    Returns all dashboard charts in a dictionary.
    """

    return {

        "sales_trend":
            sales_trend_chart(df),

        "monthly_revenue":
            monthly_revenue_chart(df),

        "region_sales":
            region_sales_chart(df),

        "category_sales":
            category_sales_chart(df),

        "segment_sales":
            segment_sales_chart(df),

        "top_customers":
            top_customers_chart(df),

        "top_products":
            top_products_chart(df),

        "quantity":
            quantity_chart(df),

        "sales_profit":
            sales_profit_scatter(df),

        "profit_margin":
            profit_margin_chart(df),

        "missing_values":
            missing_values_chart(df),

        "correlation":
            correlation_heatmap(df)

    }
