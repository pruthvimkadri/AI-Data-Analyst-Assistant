import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd


def plot_histogram(df, column):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df[column].dropna(), kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    return fig


def plot_bar_chart(df, column):
    counts = df[column].value_counts().head(10).reset_index()
    counts.columns = [column, "Count"]
    fig = px.bar(counts, x=column, y="Count", title=f"Top Categories in {column}")
    return fig


def plot_scatter(df, x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
    return fig


def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.shape[1] < 2:
        return None

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    return fig