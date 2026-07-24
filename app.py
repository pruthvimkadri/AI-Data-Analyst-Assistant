"""
====================================================
DecisionAI
AI-Powered Business Intelligence Platform
====================================================
"""

import streamlit as st
import pandas as pd
import csv
# ====================================================
# Components
# ====================================================
from components.theme import load_css
from components.sidebar import render_sidebar
from components.overview import render_overview
from components.dashboard import render_dashboard
from components.ai_assistant import render_ai_assistant
from components.reports import render_reports
from components.export_page import render_export
from components.footer import render_footer
from utils.executive_summary import generate_executive_summary
# ====================================================
# Utilities
# ====================================================

from utils.data_cleaning import (
    clean_dataset,
    generate_data_quality_report
)

from utils.analytics import (
    dataset_overview
)


# ====================================================
# Page Configuration
# ====================================================

st.set_page_config(
    page_title="DecisionAI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ====================================================
# Load Theme
# ====================================================

load_css()
# ====================================================
# Session State
# ====================================================

DEFAULT_STATE = {

    "raw_df": None,

    "clean_df": None,

    "cleaning_report": None,

    "executive_summary": "",

    "kpi_analysis": "",

    "ai_recommendations": "",

    "chat_history": []

}

for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ====================================================
# Title
# ====================================================

st.title("📊 DecisionAI")

st.markdown(
    """
AI-Powered Business Intelligence Platform

Upload your dataset and let DecisionAI clean,
analyze, visualize and generate AI-powered
business insights.
"""
)

# ====================================================
# Sidebar
# ====================================================

uploaded_file, page = render_sidebar()
# ====================================================
# Load and Clean Dataset
# ====================================================

# ====================================================
# Load and Clean Dataset
# ====================================================

if uploaded_file is not None:
    
    try:

        filename = uploaded_file.name.lower()

        if filename.endswith(".csv"):

            try:
                uploaded_file.seek(0)

                raw_df = pd.read_csv(
                    uploaded_file,
                    sep=None,
                    engine="python",
                    encoding="utf-8"
                )

            except UnicodeDecodeError:

                uploaded_file.seek(0)

                try:
                    raw_df = pd.read_csv(
                        uploaded_file,
                        sep=None,
                        engine="python",
                        encoding="cp1252"
                    )

                except UnicodeDecodeError:

                    uploaded_file.seek(0)

                    raw_df = pd.read_csv(
                        uploaded_file,
                        sep=None,
                        engine="python",
                        encoding="latin1"
                    )

        elif filename.endswith((".xlsx", ".xls")):

            raw_df = pd.read_excel(uploaded_file)

        else:

            st.error("Unsupported file type.")
            st.stop()

        # Continue with clean_dataset(raw_df)...

        # ==============================
        # CLEAN DATASET
        # ==============================

        clean_df, report = clean_dataset(raw_df)

        # TERMINAL DEBUG
        print("\n========== DEBUG ==========")
        print("raw_df type :", type(raw_df))
        print("clean_df type :", type(clean_df))
        print("report type :", type(report))
        print("===========================\n")

        # STOP HERE IF clean_df IS NONE
        if clean_df is None:
            st.error("clean_dataset() returned None")
            st.stop()

        st.session_state["raw_df"] = raw_df
        st.session_state["clean_df"] = clean_df
        st.session_state["cleaning_report"] = report

        st.success("✅ Dataset uploaded successfully!")

    except Exception as e:

       import traceback

       st.exception(e)

       traceback.print_exc()

       raise

# ====================================================
# Shortcut Variables
# ====================================================

raw_df = st.session_state["raw_df"]

clean_df = st.session_state["clean_df"]

cleaning_report = st.session_state["cleaning_report"]

# ====================================================
# Wait until a dataset is uploaded
# ====================================================

if clean_df is None:

    st.info("📂 Please upload a CSV or Excel file from the sidebar to begin analysis.")

    st.stop()
from utils.dataset_detector import detect_dataset_type
from utils.executive_summary import generate_executive_summary

# Detect domain
detected_domain = detect_dataset_type(clean_df)

# Generate AI Executive Summary
executive_summary = generate_executive_summary(
    clean_df,
    detected_domain["domain"]
)   
# ===================================
# DEBUG SESSION STATE
# ===================================

print("\n========== SESSION ==========")
print("raw_df :", type(raw_df))
print("clean_df :", type(clean_df))
print("report :", type(cleaning_report))
print("=============================\n")

if clean_df is None:
    st.error("clean_df became None after Session State")
    st.stop()

# ====================================================
# Cleaning Report
# ====================================================
# Pages
# ====================================================
st.subheader("🧠 AI Executive Summary")

st.success(executive_summary["headline"])

# ==========================
# Business Performance
# ==========================
if executive_summary["performance"]:
    st.markdown("### 📈 Business Performance")

    for item in executive_summary["performance"]:
        st.success(item)

# ==========================
# Opportunities
# ==========================
if executive_summary["opportunities"]:
    st.markdown("### ⚠️ Key Opportunities")

    for item in executive_summary["opportunities"]:
        st.warning(item)

# ==========================
# Data Quality
# ==========================
# ==========================
# Data Quality
# ==========================
if executive_summary["quality"]:
    st.markdown("### 🧹 Data Quality")

    for item in executive_summary["quality"]:
        st.info(item)
if page == "Overview":
    render_overview(clean_df)




elif page == "Dashboard":

    render_dashboard(clean_df)

elif page == "AI Assistant":

    render_ai_assistant(
        clean_df,
        
    )

# Reports and Export will be added in Part 4.
# ====================================================
# Pages
# ====================================================



elif page == "Reports":

    render_reports(
        clean_df,
        )

elif page == "Export":

    render_export(clean_df)

# ====================================================
# Footer
# ====================================================

render_footer()
# ====================================================
# Data Cleaning Report
# ====================================================

with st.expander("🧹 Data Cleaning Report", expanded=False):

    quality_report = generate_data_quality_report(clean_df)

    st.subheader("📊 Data Quality Summary")

    # -----------------------------
    # Summary Metrics
    # -----------------------------
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", quality_report["Rows"])
    col2.metric("Columns", quality_report["Columns"])
    col3.metric("Missing", quality_report["Missing Values"])
    col4.metric("Duplicates", quality_report["Duplicate Rows"])
    col5.metric(
        "Quality",
        f'{quality_report["Quality Score"]}%'
    )

    st.divider()

    # -----------------------------
    # Quality Status
    # -----------------------------
    score = quality_report["Quality Score"]
    status = quality_report["Status"]

    if status == "Excellent":
        st.success(
            f"🟢 {status} dataset quality ({score}%). Ready for analysis."
        )

    elif status == "Good":
        st.info(
            f"🔵 {status} dataset quality ({score}%). Minor cleaning recommended."
        )

    elif status == "Fair":
        st.warning(
            f"🟡 {status} dataset quality ({score}%). Some cleaning recommended."
        )

    else:
        st.error(
            f"🔴 {status} dataset quality ({score}%). Significant cleaning required."
        )

    # -----------------------------
    # Advanced Details
    # -----------------------------
    with st.expander("📄 Show Details"):

        row1_col1, row1_col2, row1_col3 = st.columns(3)

        row1_col1.metric(
            "Numeric Columns",
            quality_report["Numeric Columns"]
        )

        row1_col2.metric(
            "Text Columns",
            quality_report["Text Columns"]
        )

        row1_col3.metric(
            "Date Columns",
            quality_report["Date Columns"]
        )

        row2_col1, row2_col2, row2_col3 = st.columns(3)

        row2_col1.metric(
            "Memory (MB)",
            quality_report["Memory (MB)"]
        )

        row2_col2.metric(
            "Missing %",
            f'{quality_report["Missing %"]}%'
        )

        row2_col3.metric(
            "Duplicate %",
            f'{quality_report["Duplicate %"]}%'
        )


# ====================================================
# Dataset Preview
# ====================================================

# ====================================================
# Dataset Preview
# ====================================================

with st.expander(
    "👀 Preview Cleaned Dataset",
    expanded=False
):

    st.subheader("📋 Dataset Preview")

    # --------------------------------------------------
    # Controls
    # --------------------------------------------------

    control_col1, control_col2 = st.columns(2)

    with control_col1:

        rows_per_page = st.selectbox(
            "Rows per page",
            [10, 25, 50, 100],
            index=1
        )

    with control_col2:

        with control_col2:

          selected_columns = st.multiselect(
               "Select Columns",
               options=clean_df.columns.tolist(),
               default=clean_df.columns[:6].tolist(),
               placeholder="Select columns...",
               key="preview_columns"
           )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    search_text = st.text_input(
        "🔍 Search",
        placeholder="Search across selected columns..."
    )

    # --------------------------------------------------
    # Prepare Dataset
    # --------------------------------------------------

    preview_df = clean_df.copy()

    if selected_columns:
        preview_df = preview_df[selected_columns]

    if search_text:

        mask = preview_df.astype(str).apply(
            lambda column: column.str.contains(
                search_text,
                case=False,
                na=False
            )
        ).any(axis=1)

        preview_df = preview_df[mask]

    # --------------------------------------------------
    # Pagination
    # --------------------------------------------------

    total_rows = len(preview_df)

    total_pages = max(
        1,
        (total_rows + rows_per_page - 1) // rows_per_page
    )

    if "preview_page" not in st.session_state:
        st.session_state.preview_page = 1

    # Reset page if it exceeds available pages
    if st.session_state.preview_page > total_pages:
        st.session_state.preview_page = 1




    # --------------------------------------------------
    # Dataset Summary
    # --------------------------------------------------

    summary_col1, summary_col2, summary_col3 = st.columns(3)

summary_col1.metric(
    "Total Rows",
    f"{len(clean_df):,}"
)

summary_col2.metric(
    "Filtered Rows",
    f"{total_rows:,}"
)

summary_col3.metric(
    "Columns",
    len(selected_columns)
)
st.divider()

# --------------------------------------------------
# Page Controls
# --------------------------------------------------

page_col1, page_col2, page_col3 = st.columns([1, 2, 1])

# Previous Button
with page_col1:

    st.write("")

    if st.button(
        "⬅ Previous",
        disabled=st.session_state.preview_page == 1,
        use_container_width=True,
        key="preview_previous"
    ):
        st.session_state.preview_page -= 1
        st.rerun()

# Page Number & Slider
with page_col2:

    st.markdown(
        f"<h4 style='text-align:center;'>Page {st.session_state.preview_page} of {total_pages}</h4>",
        unsafe_allow_html=True
    )

    page = st.slider(
        "Go to Page",
        min_value=1,
        max_value=total_pages,
        value=st.session_state.preview_page,
        key="preview_slider",
        label_visibility="collapsed"
    )

    st.session_state.preview_page = page

# Next Button
with page_col3:

    st.write("")

    if st.button(
        "Next ➡",
        disabled=st.session_state.preview_page == total_pages,
        use_container_width=True,
        key="preview_next"
    ):
        st.session_state.preview_page += 1
        st.rerun()

# --------------------------------------------------
# Slice Data
# --------------------------------------------------

start = (st.session_state.preview_page - 1) * rows_per_page
end = start + rows_per_page

page_df = preview_df.iloc[start:end]

# --------------------------------------------------
# Data Preview
# --------------------------------------------------

st.dataframe(
    page_df,
    use_container_width=True
)

st.caption(
    f"Showing rows {start + 1:,} - {min(end, total_rows):,} "
    f"of {total_rows:,}"
)

# --------------------------------------------------
# Download Filtered Dataset
# --------------------------------------------------

csv = preview_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv",
    use_container_width=True,
    key="download_filtered_dataset"
)