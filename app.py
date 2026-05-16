import os
import io
import json
import textwrap
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Optional OpenAI support
try:
    from openai import OpenAI
except Exception:
    OpenAI = None

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="AI Data Analyst Assistant",
    layout="wide",
    page_icon="📊"
)

st.title("AI Data Analyst Assistant")
st.write("Upload a CSV or Excel file to begin.")

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.header("Settings")

api_key = st.sidebar.text_input(
    "OpenAI API Key (optional)",
    type="password",
    value=os.getenv("OPENAI_API_KEY", "")
)

gpt_model = st.sidebar.text_input(
    "GPT Model",
    value="gpt-4o-mini"
)

use_gpt = bool(api_key and OpenAI is not None)

st.sidebar.markdown(
    """
    ### What this app does
    - Upload CSV / Excel
    - Data preview
    - KPI dashboard
    - Interactive charts
    - AI-generated insights
    - Ask questions in natural language
    - Business recommendations
    - AI report generation
    """
)

# ---------------------------
# Helper Functions
# ---------------------------
@st.cache_data(show_spinner=False)
def load_dataframe(file_name: str, file_bytes: bytes) -> pd.DataFrame:
    """
    Load CSV or Excel with multiple encoding fallbacks.
    Uses comma as the primary separator because most analytics datasets are comma-separated.
    """
    lower = file_name.lower()

    if lower.endswith((".xlsx", ".xls")):
        return pd.read_excel(io.BytesIO(file_bytes))

    # Primary attempts for CSV
    encodings = ["utf-8-sig", "utf-8", "cp1252", "latin1"]

    for enc in encodings:
        try:
            df = pd.read_csv(io.BytesIO(file_bytes), encoding=enc, sep=",")
            if df.shape[1] > 1:
                return df
        except Exception:
            pass

    # Fallback: try other separators
    for enc in encodings:
        try:
            text = file_bytes.decode(enc, errors="strict")
            for sep in [",", ";", "\t", "|"]:
                try:
                    df = pd.read_csv(io.StringIO(text), sep=sep)
                    if df.shape[1] > 1:
                        return df
                except Exception:
                    pass

            try:
                df = pd.read_csv(io.StringIO(text), sep=None, engine="python")
                if df.shape[1] > 1:
                    return df
            except Exception:
                pass
        except Exception:
            pass

    raise ValueError("Unable to read the file. Please check encoding or file format.")


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [
        str(c).strip().replace("\n", " ").replace("\r", " ")
        for c in df.columns
    ]
    return df


def parse_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert likely date columns into datetime.
    """
    df = df.copy()
    for col in df.columns:
        if "date" in col.lower():
            converted = pd.to_datetime(df[col], errors="coerce")
            if converted.notna().sum() >= len(df) * 0.6:
                df[col] = converted
    return df


def get_numeric_and_categorical_cols(df: pd.DataFrame):
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = [
        c for c in df.columns
        if c not in numeric_cols and not pd.api.types.is_datetime64_any_dtype(df[c])
    ]
    date_cols = [
        c for c in df.columns
        if pd.api.types.is_datetime64_any_dtype(df[c])
    ]
    return numeric_cols, categorical_cols, date_cols


def missing_value_table(df: pd.DataFrame) -> pd.DataFrame:
    missing_counts = df.isnull().sum()
    missing_pct = (missing_counts / len(df) * 100).round(2)
    report = pd.DataFrame({
        "missing_count": missing_counts,
        "missing_pct": missing_pct
    })
    report = report[report["missing_count"] > 0].sort_values(
        by="missing_count", ascending=False
    )
    return report


def outlier_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    for col in numeric_cols:
        s = df[col].dropna()
        if s.empty:
            continue
        q1 = s.quantile(0.25)
        q3 = s.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers = ((s < lower) | (s > upper)).sum()

        rows.append({
            "column": col,
            "outlier_count": int(outliers),
            "outlier_pct": round((outliers / len(s)) * 100, 2)
        })

    if not rows:
        return pd.DataFrame(columns=["column", "outlier_count", "outlier_pct"])

    return pd.DataFrame(rows).sort_values("outlier_count", ascending=False)


def top_correlations(df: pd.DataFrame, threshold: float = 0.6):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] < 2:
        return []

    corr = numeric_df.corr(numeric_only=True)
    pairs = []

    cols = corr.columns.tolist()
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            val = corr.iloc[i, j]
            if abs(val) >= threshold:
                pairs.append((cols[i], cols[j], float(val)))

    pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    return pairs[:10]


def find_column(df: pd.DataFrame, keywords):
    for col in df.columns:
        low = col.lower()
        if any(k in low for k in keywords):
            return col
    return None


def build_rule_based_insights(df: pd.DataFrame):
    insights = []

    miss = missing_value_table(df)
    if not miss.empty:
        top_missing = miss.head(3).index.tolist()
        insights.append(
            f"The columns with the most missing values are: {', '.join(top_missing)}."
        )

    corr_pairs = top_correlations(df, threshold=0.6)
    if corr_pairs:
        a, b, val = corr_pairs[0]
        direction = "positive" if val > 0 else "negative"
        insights.append(
            f"Strong {direction} relationship detected between '{a}' and '{b}' (correlation {val:.2f})."
        )

    outliers = outlier_summary(df)
    if not outliers.empty:
        top_out = outliers.iloc[0]
        if top_out["outlier_count"] > 0:
            insights.append(
                f"'{top_out['column']}' shows the highest number of outliers ({int(top_out['outlier_count'])})."
            )

    numeric_cols, categorical_cols, date_cols = get_numeric_and_categorical_cols(df)

    if categorical_cols:
        top_cat = categorical_cols[0]
        top_values = df[top_cat].astype(str).value_counts().head(3)
        items = ", ".join([f"{idx} ({val})" for idx, val in top_values.items()])
        insights.append(
            f"Top categories in '{top_cat}' are: {items}."
        )

    if date_cols:
        dcol = date_cols[0]
        insights.append(
            f"Date-based analysis is possible using '{dcol}'."
        )

    if not insights:
        insights.append("No strong automatic insight found for this dataset.")

    return insights


def build_business_recommendations(df: pd.DataFrame, insights):
    recs = []

    miss = missing_value_table(df)
    if not miss.empty:
        recs.append("Prioritize data cleaning for columns with missing values before deeper analysis or reporting.")

    outliers = outlier_summary(df)
    if not outliers.empty and outliers["outlier_count"].max() > 0:
        recs.append("Investigate outliers in key numeric columns to confirm whether they are valid business cases or data quality issues.")

    corr_pairs = top_correlations(df, threshold=0.6)
    if corr_pairs:
        a, b, val = corr_pairs[0]
        recs.append(
            f"Explore the relationship between '{a}' and '{b}' further because a strong correlation may indicate an important business pattern."
        )

    numeric_cols, categorical_cols, date_cols = get_numeric_and_categorical_cols(df)

    if categorical_cols and numeric_cols:
        cat = categorical_cols[0]
        num = numeric_cols[0]
        recs.append(
            f"Compare {num} across the major segments in '{cat}' to identify top-performing and underperforming groups."
        )

    if date_cols and numeric_cols:
        recs.append(
            "Use time-based trend analysis to monitor how the main numeric metrics change over time."
        )

    if not recs:
        recs.append("Expand analysis with more business-specific KPIs and segment-level comparisons.")

    return recs[:5]


def build_dataset_context(df: pd.DataFrame, max_rows: int = 8) -> str:
    sample_csv = df.head(max_rows).to_csv(index=False)
    dtype_summary = {col: str(dtype) for col, dtype in df.dtypes.items()}
    missing_summary = df.isnull().sum().to_dict()

    context = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist()[:60],
        "dtypes": dtype_summary,
        "missing_values": missing_summary,
        "sample_rows_csv": sample_csv
    }
    return json.dumps(context, indent=2, default=str)


def get_openai_client(api_key: str):
    if not api_key or OpenAI is None:
        return None
    try:
        return OpenAI(api_key=api_key)
    except Exception:
        return None


def call_gpt(api_key: str, model: str, system_prompt: str, user_prompt: str):
    client = get_openai_client(api_key)
    if client is None:
        return None

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return None


def answer_question_rule_based(question: str, df: pd.DataFrame):
    q = question.lower().strip()
    numeric_cols, categorical_cols, date_cols = get_numeric_and_categorical_cols(df)

    # Dataset size
    if any(word in q for word in ["how many rows", "row count", "records"]):
        return f"The dataset contains {df.shape[0]:,} rows."

    if any(word in q for word in ["how many columns", "column count"]):
        return f"The dataset contains {df.shape[1]:,} columns."

    # Missing values
    if "missing" in q:
        miss = missing_value_table(df)
        if miss.empty:
            return "No missing values were found in the dataset."
        top = miss.head(3)
        return "Top missing columns: " + ", ".join(
            [f"{idx} ({int(row['missing_count'])})" for idx, row in top.iterrows()]
        )

    # Highest sales / profit / revenue / quantity type questions
    metric_col = None
    if any(k in q for k in ["sales", "revenue"]):
        metric_col = find_column(df, ["sales", "revenue"])
    elif "profit" in q:
        metric_col = find_column(df, ["profit"])
    elif "quantity" in q:
        metric_col = find_column(df, ["quantity"])
    elif "discount" in q:
        metric_col = find_column(df, ["discount"])

    group_col = None
    if any(k in q for k in ["category", "segment", "region", "state", "city"]):
        for key_group in [["category"], ["segment"], ["region"], ["state"], ["city"]]:
            cand = find_column(df, key_group)
            if cand:
                group_col = cand
                break
    else:
        # Try common grouping columns
        for key_group in [["category"], ["region"], ["segment"], ["state"], ["city"]]:
            cand = find_column(df, key_group)
            if cand:
                group_col = cand
                break

    if metric_col and group_col and any(k in q for k in ["highest", "top", "most"]):
        temp = df[[group_col, metric_col]].copy()
        temp[metric_col] = pd.to_numeric(temp[metric_col], errors="coerce")
        result = temp.groupby(group_col, dropna=True)[metric_col].sum().sort_values(ascending=False)
        if not result.empty:
            top_name = result.index[0]
            top_value = result.iloc[0]
            return f"The highest {metric_col} is in '{top_name}' with a total of {top_value:,.2f}."

    if metric_col and "average" in q:
        series = pd.to_numeric(df[metric_col], errors="coerce")
        return f"The average {metric_col} is {series.mean():,.2f}."

    if metric_col and "total" in q:
        series = pd.to_numeric(df[metric_col], errors="coerce")
        return f"The total {metric_col} is {series.sum():,.2f}."

    if any(k in q for k in ["chart", "visual", "visualize"]):
        return "Use the Charts tab to create an interactive chart based on the selected columns."

    if date_cols and any(k in q for k in ["trend", "over time", "month", "date"]):
        return f"You can use '{date_cols[0]}' as the time column for trend analysis."

    return "I could not answer that directly with rules. Try enabling GPT or rephrasing the question with a metric and group, like: 'Which category has highest sales?'"


def generate_ai_report(df: pd.DataFrame, insights, recommendations, ai_summary="", question_answer=""):
    report = []
    report.append("# AI Data Analyst Assistant Report")
    report.append("")
    report.append("## 1. Dataset Overview")
    report.append(f"- Rows: {df.shape[0]:,}")
    report.append(f"- Columns: {df.shape[1]:,}")
    report.append(f"- Numeric columns: {len(df.select_dtypes(include='number').columns.tolist())}")
    report.append(f"- Categorical columns: {len([c for c in df.columns if c not in df.select_dtypes(include='number').columns])}")
    report.append("")

    report.append("## 2. Key Findings")
    for item in insights[:5]:
        report.append(f"- {item}")
    report.append("")

    report.append("## 3. Business Recommendations")
    for item in recommendations[:5]:
        report.append(f"- {item}")
    report.append("")

    if ai_summary:
        report.append("## 4. AI Summary")
        report.append(ai_summary)
        report.append("")

    if question_answer:
        report.append("## 5. Sample Natural Language Query")
        report.append(question_answer)
        report.append("")

    report.append("## 6. Notes")
    report.append("- This report is automatically generated from the uploaded dataset.")
    report.append("- GPT output, if enabled, should be validated by the user before decision-making.")
    return "\n".join(report)


def format_float(x):
    try:
        return f"{x:,.2f}"
    except Exception:
        return str(x)


# ---------------------------
# File Upload
# ---------------------------
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])

if uploaded_file is None:
    st.info("Upload a CSV or Excel file to begin.")
    st.stop()

# ---------------------------
# Load Data
# ---------------------------
try:
    file_bytes = uploaded_file.getvalue()
    df = load_dataframe(uploaded_file.name, file_bytes)
    df = clean_column_names(df)
    df = parse_date_columns(df)
except Exception as e:
    st.error(f"Could not load dataset: {e}")
    st.stop()

# ---------------------------
# Main Dashboard KPIs
# ---------------------------
numeric_cols, categorical_cols, date_cols = get_numeric_and_categorical_cols(df)

total_missing = int(df.isnull().sum().sum())
duplicate_rows = int(df.duplicated().sum())

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Rows", f"{df.shape[0]:,}")
k2.metric("Columns", f"{df.shape[1]:,}")
k3.metric("Missing Cells", f"{total_missing:,}")
k4.metric("Duplicate Rows", f"{duplicate_rows:,}")
k5.metric("Numeric Columns", f"{len(numeric_cols):,}")

# ---------------------------
# Tabs
# ---------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Interactive Charts",
    "AI Insights",
    "Ask Your Data",
    "AI Report"
])

# ---------------------------
# TAB 1: Overview
# ---------------------------
with tab1:
    st.subheader("Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Data Types")
        dtype_df = pd.DataFrame({
            "column": df.columns,
            "dtype": [str(t) for t in df.dtypes]
        })
        st.dataframe(dtype_df, use_container_width=True)

    with c2:
        st.subheader("Statistical Summary")
        if not df.select_dtypes(include="number").empty:
            st.dataframe(df.describe(), use_container_width=True)
        else:
            st.info("No numeric columns available for summary statistics.")

    st.subheader("Missing Values")
    miss_df = missing_value_table(df)
    if miss_df.empty:
        st.success("No missing values found.")
    else:
        st.dataframe(miss_df, use_container_width=True)

    st.subheader("Outlier Summary")
    out_df = outlier_summary(df)
    if out_df.empty:
        st.info("No numeric columns available for outlier analysis.")
    else:
        st.dataframe(out_df, use_container_width=True)

    st.subheader("Correlation Matrix")
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] > 1:
        corr = numeric_df.corr(numeric_only=True)
        fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Correlation Heatmap"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Not enough numeric columns for correlation analysis.")

# ---------------------------
# TAB 2: Charts
# ---------------------------
with tab2:
    st.subheader("Build Interactive Charts")

    chart_type = st.selectbox(
        "Choose chart type",
        ["Histogram", "Bar Chart", "Line Chart", "Scatter Plot", "Box Plot", "Pie Chart"]
    )

    if chart_type == "Histogram":
        if numeric_cols:
            col = st.selectbox("Select numeric column", numeric_cols)
            fig = px.histogram(df, x=col, nbins=30, title=f"Distribution of {col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns found for histogram.")

    elif chart_type == "Bar Chart":
        if categorical_cols:
            x_col = st.selectbox("Select category column", categorical_cols)
            y_choice = st.radio("Bar mode", ["Count", "Sum of numeric column"], horizontal=True)

            if y_choice == "Count":
                chart_data = df[x_col].astype(str).value_counts().reset_index()
                chart_data.columns = [x_col, "count"]
                fig = px.bar(chart_data.head(15), x=x_col, y="count", title=f"Top categories in {x_col}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                if numeric_cols:
                    y_col = st.selectbox("Select numeric value column", numeric_cols)
                    chart_data = df.groupby(x_col, dropna=True)[y_col].sum().sort_values(ascending=False).reset_index()
                    fig = px.bar(chart_data.head(15), x=x_col, y=y_col, title=f"{y_col} by {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No numeric columns found for sum-based bar chart.")
        else:
            st.info("No categorical columns found for bar chart.")

    elif chart_type == "Line Chart":
        if numeric_cols:
            x_options = date_cols + categorical_cols + numeric_cols
            x_col = st.selectbox("Select X-axis", x_options)
            y_col = st.selectbox("Select Y-axis", numeric_cols)

            temp = df[[x_col, y_col]].copy()
            temp[y_col] = pd.to_numeric(temp[y_col], errors="coerce")
            temp = temp.dropna(subset=[y_col])

            if x_col in date_cols:
                temp = temp.sort_values(x_col)
                agg = temp.groupby(x_col, as_index=False)[y_col].sum()
                fig = px.line(agg, x=x_col, y=y_col, title=f"{y_col} over {x_col}")
            else:
                if temp[x_col].dtype == "object":
                    agg = temp.groupby(x_col, dropna=True)[y_col].sum().reset_index()
                    fig = px.line(agg, x=x_col, y=y_col, title=f"{y_col} over {x_col}")
                else:
                    fig = px.line(temp.sort_values(x_col), x=x_col, y=y_col, title=f"{y_col} over {x_col}")

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns found for line chart.")

    elif chart_type == "Scatter Plot":
        if len(numeric_cols) >= 2:
            x_col = st.selectbox("Select X-axis", numeric_cols, index=0)
            y_col = st.selectbox("Select Y-axis", numeric_cols, index=1)
            color_col = st.selectbox(
                "Optional color column",
                ["None"] + categorical_cols
            )

            color_arg = None if color_col == "None" else color_col
            fig = px.scatter(df, x=x_col, y=y_col, color=color_arg, title=f"{x_col} vs {y_col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need at least two numeric columns for scatter plot.")

    elif chart_type == "Box Plot":
        if numeric_cols:
            y_col = st.selectbox("Select numeric column", numeric_cols)
            if categorical_cols:
                x_col = st.selectbox("Optional grouping column", ["None"] + categorical_cols)
            else:
                x_col = "None"
            if x_col == "None":
                fig = px.box(df, y=y_col, title=f"Box Plot of {y_col}")
            else:
                fig = px.box(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns found for box plot.")

    elif chart_type == "Pie Chart":
        if categorical_cols:
            label_col = st.selectbox("Select category column", categorical_cols)
            if numeric_cols:
                value_choice = st.radio("Pie source", ["Count", "Sum of numeric column"], horizontal=True)
                if value_choice == "Count":
                    pie_df = df[label_col].astype(str).value_counts().reset_index()
                    pie_df.columns = [label_col, "count"]
                    fig = px.pie(pie_df.head(10), names=label_col, values="count", title=f"{label_col} Share")
                else:
                    value_col = st.selectbox("Select numeric column", numeric_cols)
                    pie_df = df.groupby(label_col, dropna=True)[value_col].sum().reset_index()
                    fig = px.pie(pie_df.head(10), names=label_col, values=value_col, title=f"{value_col} Share by {label_col}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                pie_df = df[label_col].astype(str).value_counts().reset_index()
                pie_df.columns = [label_col, "count"]
                fig = px.pie(pie_df.head(10), names=label_col, values="count", title=f"{label_col} Share")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No categorical columns found for pie chart.")

# ---------------------------
# TAB 3: AI Insights
# ---------------------------
with tab3:
    st.subheader("AI-Generated Insights")

    rule_insights = build_rule_based_insights(df)
    rule_recs = build_business_recommendations(df, rule_insights)

    ai_summary = ""

    if use_gpt:
        with st.spinner("Generating AI summary..."):
            context = build_dataset_context(df)
            system_prompt = (
                "You are a senior data analyst. "
                "Use only the dataset context provided. "
                "Summarize important patterns, risks, and business implications in plain professional language. "
                "Do not invent columns or numbers."
            )
            user_prompt = f"""
Dataset context:
{context}

Please provide:
1. A concise summary of the key findings
2. Top 3 insights
3. Business implications
4. One short caution about data quality or bias
"""
            ai_summary = call_gpt(api_key, gpt_model, system_prompt, user_prompt) or ""

    if ai_summary:
        st.success("GPT summary generated successfully.")
        st.markdown(ai_summary)
    else:
        st.info("Using rule-based insights because GPT is not enabled or the API call was not available.")

    st.markdown("### Key Insights")
    for item in rule_insights:
        st.write(f"- {item}")

    st.markdown("### Business Recommendations")
    for item in rule_recs:
        st.write(f"- {item}")

    st.markdown("### Ethical Reminder")
    st.write(
        "Always validate automated insights with business context and data quality checks before taking action."
    )

# ---------------------------
# TAB 4: Ask Your Data
# ---------------------------
with tab4:
    st.subheader("Natural Language Analytics")

    question = st.text_input(
        "Ask a question about the dataset",
        placeholder="Example: Which category has the highest sales?"
    )

    if question:
        # First try rule-based answer
        answer = answer_question_rule_based(question, df)

        # If the rule-based answer is generic and GPT is enabled, use GPT
        if use_gpt and (
            "could not answer" in answer.lower()
            or "try enabling gpt" in answer.lower()
            or "rephrase" in answer.lower()
        ):
            with st.spinner("Thinking with GPT..."):
                context = build_dataset_context(df)
                system_prompt = (
                    "You are an expert data analyst. "
                    "Answer the user's question using only the dataset context. "
                    "If the answer requires calculation, explain the result briefly. "
                    "Do not invent data."
                )
                user_prompt = f"""
Dataset context:
{context}

User question:
{question}

Answer in 3-5 concise sentences. If the data does not contain enough information, say so clearly.
"""
                gpt_answer = call_gpt(api_key, gpt_model, system_prompt, user_prompt)
                if gpt_answer:
                    answer = gpt_answer

        st.info(answer)

        # Show a small computed helper table for common questions
        if any(k in question.lower() for k in ["highest", "top", "most"]):
            metric_guess = find_column(df, ["sales", "revenue", "profit", "quantity", "discount"])
            group_guess = find_column(df, ["category", "region", "segment", "state", "city"])
            if metric_guess and group_guess:
                temp = df[[group_guess, metric_guess]].copy()
                temp[metric_guess] = pd.to_numeric(temp[metric_guess], errors="coerce")
                agg = temp.groupby(group_guess, dropna=True)[metric_guess].sum().sort_values(ascending=False).reset_index()
                st.write("### Supporting Calculation")
                st.dataframe(agg.head(10), use_container_width=True)

# ---------------------------
# TAB 5: AI Report
# ---------------------------
with tab5:
    st.subheader("Generate an AI Report")

    report_ai_summary = ai_summary if ai_summary else ""
    question_answer_text = ""

    # Optional sample Q&A for the report
    sample_question = "Which category has the highest sales?"
    sample_answer = answer_question_rule_based(sample_question, df)
    question_answer_text = f"Q: {sample_question}\nA: {sample_answer}"

    report_text = generate_ai_report(
        df=df,
        insights=rule_insights,
        recommendations=rule_recs,
        ai_summary=report_ai_summary,
        question_answer=question_answer_text
    )

    if use_gpt:
        st.markdown("### GPT Polished Executive Summary")
        with st.spinner("Generating report summary with GPT..."):
            context = build_dataset_context(df)
            system_prompt = (
                "You are a senior business analyst. "
                "Write a concise executive report based only on the dataset context and analytical findings. "
                "Use plain professional language."
            )
            user_prompt = f"""
Dataset context:
{context}

Rule-based insights:
{json.dumps(rule_insights, indent=2)}

Recommendations:
{json.dumps(rule_recs, indent=2)}

Write a short executive summary (6-10 sentences) for a business stakeholder.
"""
            polished = call_gpt(api_key, gpt_model, system_prompt, user_prompt)
            if polished:
                st.write(polished)
                report_text = generate_ai_report(
                    df=df,
                    insights=rule_insights,
                    recommendations=rule_recs,
                    ai_summary=polished,
                    question_answer=question_answer_text
                )
            else:
                st.write("GPT report generation was not available, so the rule-based report is shown below.")

    st.markdown("### Report Preview")
    st.text_area("Report Content", report_text, height=400)

    st.download_button(
        label="Download Report (.md)",
        data=report_text.encode("utf-8"),
        file_name="ai_data_analyst_report.md",
        mime="text/markdown"
    )

    st.download_button(
        label="Download Cleaned Data (.csv)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="cleaned_dataset.csv",
        mime="text/csv"
    )