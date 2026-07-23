import streamlit as st

from utils.dynamic_recommendation import generate_recommendations
from utils.dataset_detector import (
    detect_dataset_type,
    get_dataset_icon
)
from utils.domain_router import get_domain_kpis
from utils.analytics import executive_summary


def render_overview(df):

    st.header("📊 Executive Overview")

    # ==========================================
    # Dataset Summary
    # ==========================================

    summary = executive_summary(df)
    overview = summary.get("overview", {})

    st.subheader("📋 Dataset Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", overview.get("Rows", "-"))
    col2.metric("Columns", overview.get("Columns", "-"))
    col3.metric("Numeric", overview.get("Numeric Columns", "-"))
    col4.metric("Categorical", overview.get("Categorical Columns", "-"))
    col5.metric("Memory (MB)", overview.get("Memory Usage (MB)", "-"))

    st.divider()

    # ==========================================
    # AI Dataset Detection
    # ==========================================

    dataset = detect_dataset_type(df)

    domain = dataset["domain"]

    icon = get_dataset_icon(domain)

    st.subheader("🤖 AI Dataset Detection")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Detected Dataset",
            f"{icon} {domain}"
        )

    with col2:
        st.metric(
            "Confidence",
            f"{dataset['confidence']}%"
        )

    st.divider()

    # ==========================================
    # KPIs
    # ==========================================

    st.subheader("📈 Key Performance Indicators")

    kpis = get_domain_kpis(df, domain)

    if isinstance(kpis, dict) and kpis:

        items = list(kpis.items())

        for i in range(0, len(items), 4):

            cols = st.columns(4)

            for col, (name, value) in zip(cols, items[i:i + 4]):

                with col:

                    display_value = value

                    if isinstance(value, str):

                        display_value = value.strip()

                        if len(display_value) > 18:
                            display_value = display_value[:18] + "..."

                    st.metric(
                        label=name,
                        value=display_value,
                        help=str(value)
                    )

    else:
        st.warning("No KPIs available for this dataset.")

    st.divider()

    # ==========================================
    # Business Recommendations
    # ==========================================

    recommendations = generate_recommendations(df, domain)

    st.subheader("📌 Recommended KPIs")

    if recommendations["kpis"]:
        for kpi in recommendations["kpis"]:
            st.write(f"✅ {kpi}")
    else:
        st.info("No KPI recommendations available.")

    st.subheader("📊 Recommended Charts")

    if recommendations["charts"]:
        for chart in recommendations["charts"]:
            st.write(f"📈 {chart}")
    else:
        st.info("No chart recommendations available.")

    st.subheader("💡 Business Insights")

    if recommendations["insights"]:
        for insight in recommendations["insights"]:
            st.write(f"• {insight}")
    else:
        st.info("No business insights available.")
