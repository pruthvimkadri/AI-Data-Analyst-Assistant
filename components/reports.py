"""
====================================================
DecisionAI Reports Page
====================================================

AI-generated reports and business insights.
"""

import streamlit as st

from utils.gpt_engine import (
    create_client,
    generate_executive_summary,
    explain_kpis,
    generate_ai_recommendations,
    safe_chat
)


def render_reports(df, api_key):
    """
    Render the Reports page.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned dataset.

    api_key : str
        OpenAI API Key.
    """

    st.header("📄 AI Reports")

    if not api_key:

        st.warning(
            "Please enter your OpenAI API Key in the sidebar."
        )

        return

    client = create_client(api_key)

    tab1, tab2, tab3 = st.tabs(
        [
            "📊 Executive Summary",
            "📈 KPI Analysis",
            "💡 Recommendations"
        ]
    )

    # ====================================================
    # Executive Summary
    # ====================================================

    with tab1:

        st.subheader("Executive Summary")

        if st.button(
            "Generate Executive Summary",
            key="executive_summary_btn"
        ):

            with st.spinner(
                "Generating executive summary..."
            ):

                summary = safe_chat(
                    generate_executive_summary,
                    client,
                    df
                )

                st.session_state[
                    "executive_summary"
                ] = summary

        if st.session_state.get(
            "executive_summary"
        ):

            st.write(
                st.session_state[
                    "executive_summary"
                ]
            )

    # ====================================================
    # KPI Analysis
    # ====================================================

    with tab2:

        st.subheader("KPI Analysis")

        if st.button(
            "Explain KPIs",
            key="kpi_btn"
        ):

            with st.spinner(
                "Analyzing KPIs..."
            ):

                explanation = safe_chat(
                    explain_kpis,
                    client,
                    df
                )

                st.session_state[
                    "kpi_analysis"
                ] = explanation

        if st.session_state.get(
            "kpi_analysis"
        ):

            st.write(
                st.session_state[
                    "kpi_analysis"
                ]
            )

    # ====================================================
    # Recommendations
    # ====================================================

    with tab3:

        st.subheader(
            "AI Business Recommendations"
        )

        if st.button(
            "Generate Recommendations",
            key="recommendation_btn"
        ):

            with st.spinner(
                "Generating recommendations..."
            ):

                recommendations = safe_chat(
                    generate_ai_recommendations,
                    client,
                    df
                )

                st.session_state[
                    "ai_recommendations"
                ] = recommendations

        if st.session_state.get(
            "ai_recommendations"
        ):

            st.write(
                st.session_state[
                    "ai_recommendations"
                ]
            )