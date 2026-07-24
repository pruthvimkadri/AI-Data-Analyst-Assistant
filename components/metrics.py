"""
====================================================
DecisionAI Metrics Components
====================================================

Reusable KPI metric cards and metric grids.
"""

import streamlit as st


# ====================================================
# Single Metric Card
# ====================================================

def metric_card(
    title,
    value,
    delta=None,
    help_text=None
):
    """
    Display a single KPI metric.

    Parameters
    ----------
    title : str
        Metric title.

    value : Any
        Metric value.

    delta : str, optional
        Change indicator.

    help_text : str, optional
        Tooltip.
    """

    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text
    )


# ====================================================
# Metric Grid
# ====================================================

def metric_grid(
    metrics,
    columns=4
):
    """
    Display KPI metrics in a responsive grid.

    Parameters
    ----------
    metrics : dict

    columns : int
    """

    if not metrics:
        st.info("No metrics available.")
        return

    cols = st.columns(columns)

    for index, (name, value) in enumerate(metrics.items()):

        with cols[index % columns]:

            metric_card(
                title=name,
                value=value
            )


# ====================================================
# Colored Status Metric
# ====================================================

def status_metric(
    title,
    value,
    status
):
    """
    Display status using color indicators.

    status:
        good
        warning
        danger
        neutral
    """

    colors = {

        "good": "🟢",

        "warning": "🟡",

        "danger": "🔴",

        "neutral": "🔵"

    }

    icon = colors.get(
        status,
        "⚪"
    )

    st.metric(

        label=f"{icon} {title}",

        value=value

    )


# ====================================================
# KPI Section
# ====================================================

def metric_section(
    title,
    metrics,
    columns=4
):
    """
    Display an entire KPI section.
    """

    st.subheader(title)

    metric_grid(
        metrics,
        columns
    )