"""
====================================================
DecisionAI Export Utilities
====================================================

Handles exporting data, reports, and AI outputs.

Part A
-------
✓ CSV Export
✓ Excel Export
✓ Text Export
✓ JSON Export
"""

import json
from io import BytesIO

import pandas as pd


# ====================================================
# Export DataFrame as CSV
# ====================================================

def export_csv(df):
    """
    Returns CSV bytes for download.
    """

    return df.to_csv(index=False).encode("utf-8")


# ====================================================
# Export DataFrame as Excel
# ====================================================

def export_excel(df, sheet_name="DecisionAI"):
    """
    Returns an Excel workbook as bytes.
    """

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name=sheet_name
        )

    output.seek(0)

    return output.getvalue()


# ====================================================
# Export Text Report
# ====================================================

def export_text(text):
    """
    Returns UTF-8 encoded text.
    """

    if text is None:
        text = ""

    return text.encode("utf-8")


# ====================================================
# Export Dictionary as JSON
# ====================================================

def export_json(data):
    """
    Returns formatted JSON bytes.
    """

    json_data = json.dumps(
        data,
        indent=4,
        default=str
    )

    return json_data.encode("utf-8")
# ====================================================
# Imports
# ====================================================

from .analytics import calculate_kpis
from .business_recommendations_v2 import (
    generate_business_recommendations
)


# ====================================================
# Export KPI Report
# ====================================================

def export_kpi_report(df):
    """
    Export KPIs as JSON bytes.
    """

    kpis = calculate_kpis(df)

    return export_json(kpis)


# ====================================================
# Export AI Report
# ====================================================

def export_ai_report(
    executive_summary="",
    recommendations="",
    chat_history=""
):
    """
    Combines AI outputs into one report.
    """

    report = f"""
===============================
DecisionAI Report
===============================

EXECUTIVE SUMMARY

{executive_summary}


===============================
BUSINESS RECOMMENDATIONS
===============================

{recommendations}


===============================
AI CHAT
===============================

{chat_history}
"""

    return export_text(report)


# ====================================================
# Export Recommendation Report
# ====================================================

def export_recommendation_report(df):
    """
    Export recommendations as JSON.
    """

    recommendations = generate_business_recommendations(df)

    return export_json(recommendations)


# ====================================================
# Export Complete Excel Workbook
# ====================================================

def export_complete_workbook(
    cleaned_df,
    sheet_name="Cleaned Data"
):
    """
    Creates a multi-sheet Excel workbook.

    Sheets
    ------
    1. Cleaned Data
    2. KPIs
    3. Recommendations
    """

    output = BytesIO()

    kpis = calculate_kpis(cleaned_df)

    recommendations = generate_business_recommendations(
        cleaned_df
    )

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        # ---------------------------
        # Cleaned Data
        # ---------------------------

        cleaned_df.to_excel(
            writer,
            sheet_name=sheet_name,
            index=False
        )

        # ---------------------------
        # KPI Sheet
        # ---------------------------

        pd.DataFrame(
            list(kpis.items()),
            columns=["KPI", "Value"]
        ).to_excel(
            writer,
            sheet_name="KPIs",
            index=False
        )

        # ---------------------------
        # Recommendation Sheet
        # ---------------------------

        pd.DataFrame({
            "Recommendation":
            recommendations
        }).to_excel(
            writer,
            sheet_name="Recommendations",
            index=False
        )

    output.seek(0)

    return output.getvalue()


# ====================================================
# Export Everything
# ====================================================

def export_everything(
    cleaned_df,
    executive_summary="",
    recommendations="",
    chat_history=""
):
    """
    Returns all downloadable exports.
    """

    return {

        "csv":
            export_csv(cleaned_df),

        "excel":
            export_complete_workbook(cleaned_df),

        "json":
            export_json(
                calculate_kpis(cleaned_df)
            ),

        "report":
            export_ai_report(
                executive_summary,
                recommendations,
                chat_history
            )

    }