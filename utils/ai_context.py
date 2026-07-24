"""
=========================================================
DecisionAI AI Context Builder
=========================================================

Collects all business context required by the AI Assistant.

This module DOES NOT call OpenAI.

It gathers:
- Dataset information
- Domain
- KPIs
- Executive summary
- Business insights

Author: DecisionAI
"""

import pandas as pd

from utils.dataset_detector import detect_dataset_scores
from utils.dynamic_recommendation import generate_recommendations


def build_ai_context(df: pd.DataFrame) -> dict:
    """
    Build complete business context for the LLM.
    """

    # -----------------------------
    # Detect Dataset Domain
    # -----------------------------
    scores = detect_dataset_scores(df)

    if scores:
        domain = max(
           scores,
           key=lambda x: scores[x]["matched_keywords"]
        )
    else:
        domain = "Generic"

    # -----------------------------
    # Generate Recommendations
    # -----------------------------
    recommendations = generate_recommendations(
       df,
       domain
    )

    # -----------------------------
    # Dataset Information
    # -----------------------------
    dataset_info = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

    # -----------------------------
    # KPIs
    # -----------------------------
    kpis = recommendations.get("kpis", {})

    # -----------------------------
    # Executive Summary
    # -----------------------------
    # Executive Summary
    executive_summary = recommendations.get("executive_summary", "")

    # -----------------------------
    # Business Insights
    # -----------------------------
    insights = recommendations.get("insights", [])

    # -----------------------------
    # Charts
    # -----------------------------
    charts = recommendations.get("charts", [])
    
    # -----------------------------
    # Return Context
    # -----------------------------
    return {
        "domain": domain,
        "dataset_info": dataset_info,
        "kpis": kpis,
        "executive_summary": executive_summary,
        "insights": insights,
        "charts": charts
    }