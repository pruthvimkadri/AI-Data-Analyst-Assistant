import pandas as pd


def missing_value_report(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    return missing


def top_numeric_correlations(df, target_col=None, threshold=0.5):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] < 2:
        return []

    corr_matrix = numeric_df.corr(numeric_only=True)
    pairs = []

    cols = corr_matrix.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            corr_val = corr_matrix.iloc[i, j]
            if abs(corr_val) >= threshold:
                pairs.append((cols[i], cols[j], corr_val))

    pairs = sorted(pairs, key=lambda x: abs(x[2]), reverse=True)
    return pairs[:10]


def simple_insights(df):
    """
    Generate simple business-friendly insights from dataframe.
    This is rule-based, so it works without GenAI/API keys.
    """
    insights = []

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()

    if numeric_cols:
        missing_numeric = df[numeric_cols].isnull().sum().sort_values(ascending=False)
        top_missing = missing_numeric[missing_numeric > 0]
        if not top_missing.empty:
            insights.append(
                f"Numeric columns with missing values: {', '.join(top_missing.index[:3].tolist())}."
            )

    if cat_cols:
        top_cat = cat_cols[0]
        top_counts = df[top_cat].value_counts(dropna=True).head(3)
        if not top_counts.empty:
            top_text = ", ".join([f"{idx} ({val})" for idx, val in top_counts.items()])
            insights.append(
                f"Most common categories in '{top_cat}': {top_text}."
            )

    if len(numeric_cols) >= 2:
        corr_pairs = top_numeric_correlations(df, threshold=0.6)
        if corr_pairs:
            c1, c2, corr = corr_pairs[0]
            insights.append(
                f"Strong relationship observed between '{c1}' and '{c2}' (correlation: {corr:.2f})."
            )

    if not insights:
        insights.append("No strong automatic insight found. Try selecting a different dataset or more columns.")

    return insights