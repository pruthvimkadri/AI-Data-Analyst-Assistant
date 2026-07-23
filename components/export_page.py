"""
====================================================
DecisionAI Export Page
====================================================

Export datasets, KPIs and AI reports.
"""

import streamlit as st

from utils.analytics import calculate_kpis

from utils.export import (
    export_csv,
    export_complete_workbook,
    export_json,
    export_ai_report
)


def render_export(clean_df):
    """
    Render Export page.

    Parameters
    ----------
    clean_df : pandas.DataFrame
        Cleaned dataset.
    """

    st.header("📥 Export Center")

    st.write(
        "Download your cleaned dataset, KPI reports, "
        "and AI-generated reports."
    )

    # ====================================================
    # Dataset Export
    # ====================================================

    st.subheader("📁 Dataset")

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            label="⬇ Download CSV",

            data=export_csv(clean_df),

            file_name="decisionai_dataset.csv",

            mime="text/csv",

            use_container_width=True

        )

    with col2:

        st.download_button(

            label="⬇ Download Excel",

            data=export_complete_workbook(clean_df),

            file_name="decisionai_workbook.xlsx",

            mime=(
                "application/vnd.openxmlformats-"
                "officedocument.spreadsheetml.sheet"
            ),

            use_container_width=True

        )

    st.divider()

    # ====================================================
    # KPI Export
    # ====================================================

    st.subheader("📊 KPI Report")

    st.download_button(

        label="⬇ Download KPI JSON",

        data=export_json(
            calculate_kpis(clean_df)
        ),

        file_name="decisionai_kpis.json",

        mime="application/json",

        use_container_width=True

    )

    st.divider()

    # ====================================================
    # AI Report
    # ====================================================

    st.subheader("🤖 AI Report")

    report = export_ai_report(

        executive_summary=st.session_state.get(
            "executive_summary",
            ""
        ),

        recommendations=st.session_state.get(
            "ai_recommendations",
            ""
        ),

        chat_history=str(

            st.session_state.get(
                "chat_history",
                []
            )

        )

    )

    st.download_button(

        label="⬇ Download AI Report",

        data=report,

        file_name="decisionai_ai_report.txt",

        mime="text/plain",

        use_container_width=True

    )