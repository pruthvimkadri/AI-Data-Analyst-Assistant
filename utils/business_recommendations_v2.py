"""
====================================================
DecisionAI Business Recommendation Engine
====================================================

Generates intelligent business recommendations
based on uploaded datasets.

Part A
-------
✓ Executive Summary
✓ Revenue Analysis
"""
from recommendations.retail_recommendations import RETAIL_RECOMMENDATIONS
from recommendations.banking_recommendations import BANKING_RECOMMENDATIONS
from recommendations.finance_recommendation import FINANCE_RECOMMENDATIONS
from recommendations.healthcare_recommendation import HEALTHCARE_RECOMMENDATIONS
from recommendations.hr_recommendation import HR_RECOMMENDATIONS
from recommendations.education_recommendation import EDUCATION_RECOMMENDATIONS
from recommendations.ecommerce_recommendation import ECOMMERCE_RECOMMENDATIONS
from recommendations.entertainment_recommendations import ENTERTAINMENT_RECOMMENDATIONS
from recommendations.fashion_recommendations import FASHION_RECOMMENDATIONS
from .analytics import (
    calculate_kpis,
    trend_analysis,
    region_analysis,
    category_analysis,
    customer_analysis,
    analyze_missing_values,
    detect_outliers,
    business_health_score
)


# ====================================================
# Executive Summary
# ====================================================

def executive_summary_recommendations(df):
    """
    Generates high-level executive insights.
    """

    recommendations = []

    kpis = calculate_kpis(df)

    total_sales = kpis.get("Total Sales", 0)
    total_profit = kpis.get("Total Profit", 0)
    margin = kpis.get("Profit Margin", 0)

    recommendations.append(
        f"Total Sales: ₹{total_sales:,.2f}"
    )

    recommendations.append(
        f"Total Profit: ₹{total_profit:,.2f}"
    )

    recommendations.append(
        f"Profit Margin: {margin:.2f}%"
    )

    health = business_health_score(kpis)

    if health >= 90:

        recommendations.append(
            "Business health is excellent."
        )

    elif health >= 75:

        recommendations.append(
            "Business performance is healthy with room for optimization."
        )

    elif health >= 60:

        recommendations.append(
            "Business performance is average. Focus on improving profitability."
        )

    else:

        recommendations.append(
            "Business health is poor. Immediate strategic action is recommended."
        )

    return recommendations


# ====================================================
# Revenue Recommendations
# ====================================================

def revenue_recommendations(df):
    """
    Revenue-related recommendations.
    """

    recommendations = []

    kpis = calculate_kpis(df)

    sales = kpis.get("Total Sales", 0)

    avg_sale = kpis.get("Average Sale", 0)

    max_sale = kpis.get("Maximum Sale", 0)

    if sales == 0:

        recommendations.append(
            "No sales information available."
        )

        return recommendations

    recommendations.append(
        f"Average sale value is ₹{avg_sale:,.2f}."
    )

    recommendations.append(
        f"Highest transaction value is ₹{max_sale:,.2f}."
    )

    trend = trend_analysis(df)

    if trend is not None and len(trend) >= 2:

        sales_column = trend.columns[1]

        latest = trend.iloc[-1][sales_column]

        previous = trend.iloc[-2][sales_column]

        if latest > previous:

            growth = (
                (latest - previous)
                / previous
            ) * 100 if previous != 0 else 0

            recommendations.append(
                f"Revenue increased by {growth:.1f}% compared to the previous month."
            )

        elif latest < previous:

            decline = (
                (previous - latest)
                / previous
            ) * 100 if previous != 0 else 0

            recommendations.append(
                f"Revenue declined by {decline:.1f}% compared to the previous month."
            )

            recommendations.append(
                "Investigate pricing, marketing campaigns, and seasonal demand."
            )

        else:

            recommendations.append(
                "Revenue remained stable compared to the previous month."
            )

    recommendations.append(
        "Monitor monthly revenue trends to identify seasonal patterns."
    )

    recommendations.append(
        "Track average order value and encourage bundle purchases."
    )

    return recommendations


# ====================================================
# Revenue Opportunity Detection
# ====================================================

def revenue_opportunities(df):
    """
    Identifies opportunities to increase revenue.
    """

    opportunities = []

    region = region_analysis(df)

    if region is not None and not region.empty:

        best_region = region.iloc[0]

        opportunities.append(

            f"Highest revenue region: {best_region.iloc[0]}."

        )

    category = category_analysis(df)

    if category is not None and not category.empty:

        best_category = category.iloc[0]

        opportunities.append(

            f"Best-performing category: {best_category.iloc[0]}."

        )

    customer = customer_analysis(df)

    if customer is not None and not customer.empty:

        top_customer = customer.iloc[0]

        opportunities.append(

            f"Top customer contributes the highest revenue: {top_customer.iloc[0]}."

        )

    opportunities.append(
        "Focus marketing efforts on high-performing regions and categories."
    )

    opportunities.append(
        "Increase cross-selling and upselling for repeat customers."
    )

    return opportunities
# ====================================================
# Profit Recommendations
# ====================================================

def profit_recommendations(df):
    """
    Generates profit-related business recommendations.
    """

    recommendations = []

    kpis = calculate_kpis(df)

    total_profit = kpis.get("Total Profit", 0)
    margin = kpis.get("Profit Margin", 0)

    recommendations.append(
        f"Total Profit: ₹{total_profit:,.2f}"
    )

    recommendations.append(
        f"Overall Profit Margin: {margin:.2f}%"
    )

    if margin >= 20:

        recommendations.append(
            "Excellent profit margin. Maintain current pricing strategy."
        )

    elif margin >= 10:

        recommendations.append(
            "Healthy profit margin. Look for opportunities to improve operational efficiency."
        )

    elif margin >= 5:

        recommendations.append(
            "Profit margin is moderate. Review discounts and operating costs."
        )

    else:

        recommendations.append(
            "Profit margin is critically low. Review pricing strategy and reduce unnecessary expenses."
        )

    recommendations.append(
        "Track profit margin regularly instead of focusing only on revenue."
    )

    return recommendations


# ====================================================
# Region Recommendations
# ====================================================

def region_recommendations(df):
    """
    Region-wise business recommendations.
    """

    recommendations = []

    region = region_analysis(df)

    if region is None or region.empty:

        recommendations.append(
            "Region information is unavailable."
        )

        return recommendations

    best = region.iloc[0]
    worst = region.iloc[-1]

    recommendations.append(
        f"Top-performing region: {best.iloc[0]}"
    )

    recommendations.append(
        f"Lowest-performing region: {worst.iloc[0]}"
    )

    recommendations.append(
        "Increase marketing investment in high-performing regions."
    )

    recommendations.append(
        "Investigate the causes of poor performance in low-performing regions."
    )

    recommendations.append(
        "Compare customer preferences across regions before expanding inventory."
    )

    return recommendations


# ====================================================
# Category Recommendations
# ====================================================

def category_recommendations(df):
    """
    Category-level recommendations.
    """

    recommendations = []

    category = category_analysis(df)

    if category is None or category.empty:

        recommendations.append(
            "Category information is unavailable."
        )

        return recommendations

    best = category.iloc[0]
    worst = category.iloc[-1]

    recommendations.append(
        f"Best-selling category: {best.iloc[0]}"
    )

    recommendations.append(
        f"Lowest-selling category: {worst.iloc[0]}"
    )

    recommendations.append(
        "Promote high-performing categories using premium placements."
    )

    recommendations.append(
        "Review pricing and demand for low-performing categories."
    )

    recommendations.append(
        "Bundle slow-moving products with best-selling categories."
    )

    return recommendations


# ====================================================
# Regional Risk Detection
# ====================================================

def regional_risks(df):
    """
    Detects business risks across regions.
    """

    risks = []

    region = region_analysis(df)

    if region is None or region.empty:
        return risks

    average_sales = region["Total Sales"].mean()

    low_regions = region[
        region["Total Sales"] < average_sales
    ]

    if low_regions.empty:

        risks.append(
            "All regions are performing above the average sales level."
        )

    else:

        risks.append(
            f"{len(low_regions)} region(s) are performing below the average sales level."
        )

        for _, row in low_regions.iterrows():

            risks.append(
                f"{row.iloc[0]} is below average sales."
            )

    return risks


# ====================================================
# Category Growth Opportunities
# ====================================================

def category_growth_opportunities(df):
    """
    Identifies categories with the highest revenue potential.
    """

    opportunities = []

    category = category_analysis(df)

    if category is None or category.empty:
        return opportunities

    top3 = category.head(3)

    opportunities.append(
        "Highest revenue categories:"
    )

    for _, row in top3.iterrows():

        opportunities.append(
            f"• {row.iloc[0]}"
        )

    opportunities.append(
        "Introduce complementary products within these categories."
    )

    opportunities.append(
        "Run seasonal campaigns for top-performing categories."
    )

    return opportunities
# ====================================================
# Customer Recommendations
# ====================================================

def customer_recommendations(df):
    """
    Generates recommendations based on customer performance.
    """

    recommendations = []

    customer = customer_analysis(df)

    if customer is None or customer.empty:

        recommendations.append(
            "Customer information is unavailable."
        )

        return recommendations

    total_customers = len(customer)

    recommendations.append(
        f"Total Active Customers: {total_customers}"
    )

    top_customer = customer.iloc[0]

    customer_name_col = customer.columns[0]

    recommendations.append(
        f"Top Customer: {top_customer[customer_name_col]}"
    )

    recommendations.append(
        "Reward high-value customers with loyalty programs."
    )

    recommendations.append(
        "Identify inactive customers and run re-engagement campaigns."
    )

    recommendations.append(
        "Use personalized offers for repeat customers."
    )

    return recommendations


# ====================================================
# Product Recommendations
# ====================================================

def product_recommendations(df):
    """
    Generates product-related recommendations.
    """

    recommendations = []

    category = category_analysis(df)

    if category is None or category.empty:

        recommendations.append(
            "Product information unavailable."
        )

        return recommendations

    category_name = category.columns[0]

    best = category.iloc[0]

    worst = category.iloc[-1]

    recommendations.append(
        f"Highest-selling category: {best[category_name]}"
    )

    recommendations.append(
        f"Lowest-selling category: {worst[category_name]}"
    )

    recommendations.append(
        "Increase inventory for high-demand products."
    )

    recommendations.append(
        "Review pricing of slow-moving products."
    )

    recommendations.append(
        "Bundle slow-moving products with best sellers."
    )

    recommendations.append(
        "Analyze seasonal demand before procurement."
    )

    return recommendations


# ====================================================
# Missing Value Recommendations
# ====================================================

def missing_value_recommendations(df):
    """
    Generates recommendations based on missing values.
    """

    recommendations = []

    missing = analyze_missing_values(df)

    if missing["total_missing"] == 0:

        recommendations.append(
            "No missing values detected."
        )

        return recommendations

    recommendations.append(
        f"Dataset contains {missing['total_missing']} missing values."
    )

    for column, info in missing["columns"].items():

        recommendations.append(
            f"{column}: {info['percentage']}% missing."
        )

    recommendations.append(
        "Fill missing numerical values using mean or median."
    )

    recommendations.append(
        "Fill categorical values using mode or business rules."
    )

    return recommendations


# ====================================================
# Outlier Recommendations
# ====================================================

def outlier_recommendations(df):
    """
    Generates recommendations based on detected outliers.
    """

    recommendations = []

    outliers = detect_outliers(df)

    if outliers.empty:

        recommendations.append(
            "No numeric columns available."
        )

        return recommendations

    significant = outliers[
        outliers["Outliers"] > 0
    ]

    if significant.empty:

        recommendations.append(
            "No significant outliers detected."
        )

        return recommendations

    recommendations.append(
        f"{len(significant)} column(s) contain outliers."
    )

    for _, row in significant.iterrows():

        recommendations.append(
            f"{row['Column']} has {row['Outliers']} outliers."
        )

    recommendations.append(
        "Review outliers before model training."
    )

    recommendations.append(
        "Validate whether extreme values are genuine business events."
    )

    return recommendations


# ====================================================
# Data Quality Recommendations
# ====================================================

def data_quality_recommendations(df):
    """
    Combines all data-quality related recommendations.
    """

    recommendations = []

    recommendations.extend(
        missing_value_recommendations(df)
    )

    recommendations.extend(
        outlier_recommendations(df)
    )

    return recommendations


# ====================================================
# Customer Opportunities
# ====================================================

def customer_growth_opportunities(df):
    """
    Customer growth suggestions.
    """

    opportunities = []

    opportunities.append(
        "Increase customer retention through loyalty rewards."
    )

    opportunities.append(
        "Launch referral programs for existing customers."
    )

    opportunities.append(
        "Segment customers based on purchase behaviour."
    )

    opportunities.append(
        "Identify high-value customers for premium services."
    )

    return opportunities


# ====================================================
# Product Opportunities
# ====================================================

def product_growth_opportunities(df):
    """
    Product growth suggestions.
    """

    opportunities = []

    opportunities.append(
        "Increase visibility of best-selling products."
    )

    opportunities.append(
        "Introduce product bundles."
    )

    opportunities.append(
        "Recommend complementary products."
    )

    opportunities.append(
        "Analyze frequently purchased product combinations."
    )

    return opportunities
# ====================================================
# Executive Report Builder
# ====================================================

def executive_report(df):
    """
    Builds a complete executive report dictionary.
    """

    return {
        "Executive Summary": executive_summary_recommendations(df),
        "Revenue": revenue_recommendations(df),
        "Revenue Opportunities": revenue_opportunities(df),
        "Profit": profit_recommendations(df),
        "Regions": region_recommendations(df),
        "Regional Risks": regional_risks(df),
        "Categories": category_recommendations(df),
        "Category Opportunities": category_growth_opportunities(df),
        "Customers": customer_recommendations(df),
        "Customer Opportunities": customer_growth_opportunities(df),
        "Products": product_recommendations(df),
        "Product Opportunities": product_growth_opportunities(df),
        "Data Quality": data_quality_recommendations(df)
    }


# ====================================================
# Generate Business Recommendations
# ====================================================

def generate_business_recommendations(df):
    """
    Main function used by Streamlit.
    Returns all recommendation sections.
    """

    return executive_report(df)


# ====================================================
# Recommendation Formatter
# ====================================================

import streamlit as st

def format_recommendations(report):
    """
    Display recommendations in a clean Streamlit layout.
    """

    if not report:
        st.info("No recommendations available.")
        return

    icons = {
        "Executive Summary": "📋",
        "Revenue": "💰",
        "Revenue Opportunities": "📈",
        "Profit": "💵",
        "Regions": "🌍",
        "Regional Risks": "⚠️",
        "Categories": "📦",
        "Category Opportunities": "🚀",
        "Customers": "👥",
        "Customer Opportunities": "🎯",
        "Products": "🛒",
        "Product Opportunities": "✨",
        "Data Quality": "🧹"
    }

    for section, recommendations in report.items():

        icon = icons.get(section, "📌")

        with st.expander(f"{icon} {section}", expanded=False):

            if not recommendations:
                st.info("No recommendations available.")
                continue

            for recommendation in recommendations:
    
    # Remove any leading bullet/dash and extra spaces
                clean_recommendation = recommendation.lstrip("-• ").strip()

                st.markdown(f"• {clean_recommendation}")

# ====================================================
# Recommendation Statistics
# ====================================================

def recommendation_statistics(report):
    """
    Returns simple statistics about the generated report.
    """

    stats = {
        "Sections": len(report),
        "Recommendations": 0
    }

    total = 0

    for recommendations in report.values():

        total += len(recommendations)

    stats["Recommendations"] = total

    return stats


# ====================================================
# Recommendation Search
# ====================================================

def search_recommendations(report, keyword):
    """
    Search recommendations containing a keyword.
    """

    keyword = keyword.lower()

    results = {}

    for section, recommendations in report.items():

        matches = []

        for recommendation in recommendations:

            if keyword in recommendation.lower():
                matches.append(recommendation)

        if matches:
            results[section] = matches

    return results


# ====================================================
# Recommendation Categories
# ====================================================

def recommendation_categories():
    """
    Returns all supported recommendation sections.
    """

    return [

        "Executive Summary",

        "Revenue",

        "Revenue Opportunities",

        "Profit",

        "Regions",

        "Regional Risks",

        "Categories",

        "Category Opportunities",

        "Customers",

        "Customer Opportunities",

        "Products",

        "Product Opportunities",

        "Data Quality"

    ]