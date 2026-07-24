"""
====================================================
DecisionAI Reports Page
====================================================

AI-generated reports powered by Gemini.

Author: DecisionAI
"""

import streamlit as st

from utils.ai_context import build_ai_context
from utils.prompt_builder import build_business_prompt
from utils.gpt_engine import ask_llm


def render_reports(df):
    """
    Render the AI Reports page.
    """

    st.header("📄 AI Reports")

    if df is None or df.empty:
        st.warning("Please upload a dataset first.")
        return

    # ------------------------------------------------
    # Build AI Context (used by all reports)
    # ------------------------------------------------

    context = build_ai_context(df)

    tab1, tab2, tab3 = st.tabs(
        [
            "📊 Executive Summary",
            "📈 KPI Analysis",
            "💡 Recommendations",
        ]
    )

    # ====================================================
    # Executive Summary
    # ====================================================

    with tab1:

        st.subheader("Executive Summary")

        if st.button(
            "Generate Executive Summary",
            key="executive_summary_btn",
        ):

            prompt = build_business_prompt(
                context=context,
                user_question="""
Generate a professional Executive Summary.

Include:

- Dataset overview
- Important business observations
- Major trends
- Risks
- Opportunities

Do not use ASCII tables.
Use Markdown headings and bullet points.
"""
            )

            with st.spinner("Generating executive summary..."):

                summary = ask_llm(prompt)

                st.session_state["executive_summary"] = summary

        if "executive_summary" in st.session_state:
            st.markdown(st.session_state["executive_summary"])

    # ====================================================
    # KPI Analysis
    # ====================================================

    with tab2:

        st.subheader("KPI Analysis")

        if st.button(
            "Explain KPIs",
            key="kpi_btn",
        ):

            prompt = build_business_prompt(
                context=context,
                user_question="""
Explain the important KPIs.

Include:

- Revenue performance
- Profitability
- Growth trends
- Customer behaviour
- Operational insights

Do not use ASCII tables.
Use Markdown headings and bullet points.
"""
            )

            with st.spinner("Analysing KPIs..."):

                kpis = ask_llm(prompt)

                st.session_state["kpi_analysis"] = kpis

        if "kpi_analysis" in st.session_state:
            st.markdown(st.session_state["kpi_analysis"])

    # ====================================================
    # Recommendations
    # ====================================================

    with tab3:

        st.subheader("Business Recommendations")

        if st.button(
            "Generate Recommendations",
            key="recommendation_btn",
        ):

            prompt = build_business_prompt(
                context=context,
                user_question="""
Generate strategic business recommendations.

Include:

- Top business opportunities
- Cost reduction ideas
- Revenue improvement suggestions
- Risks
- Action plan
- Next steps

Do not use ASCII tables.
Use Markdown headings and bullet points.
"""
            )

            with st.spinner("Generating recommendations..."):

                recommendations = ask_llm(prompt)

                st.session_state["ai_recommendations"] = recommendations

        if "ai_recommendations" in st.session_state:
            st.markdown(st.session_state["ai_recommendations"])