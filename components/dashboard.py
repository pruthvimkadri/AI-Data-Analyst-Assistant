"""
====================================================
DecisionAI Dashboard Page
====================================================
"""

import streamlit as st

from utils.charts import (
    sales_trend_chart,
    region_sales_chart,
    category_sales_chart,
    top_customers_chart,
    sales_profit_scatter,
    correlation_heatmap,
    monthly_revenue_chart,
    segment_sales_chart,
    top_products_chart,
    customer_distribution_chart,
    quantity_chart,
    product_performance_chart,
    profit_margin_chart,
    missing_values_chart
)


def render_dashboard(df):

    st.header("📈 Business Dashboard")

    charts = [

        ("📈 Sales Trend", sales_trend_chart(df)),

        ("🌍 Sales by Region", region_sales_chart(df)),

        ("📦 Sales by Category", category_sales_chart(df)),

        ("🏆 Top Customers", top_customers_chart(df)),

        ("💰 Sales vs Profit", scatter_sales_profit(df)),

        ("📊 Category Distribution", category_pie_chart(df)),

        ("📉 Histogram", histogram(df)),

        ("📦 Box Plot", boxplot(df)),

        ("🔥 Correlation Heatmap", correlation_heatmap(df))

    ]

    for title, fig in charts:

        if fig is not None:

            st.subheader(title)

            st.plotly_chart(
                fig,
                use_container_width=True
            )