"""
====================================================
DecisionAI Prompt Builder
====================================================

Creates structured prompts for the LLM.

Part A
-------
✓ System Prompt
✓ Dataset Summary
✓ KPI Summary
✓ Recommendation Summary
"""

import json

from .analytics import (
    calculate_kpis,
    dataset_overview
)

from .business_recommendations_v2 import (
    generate_business_recommendations
)


# ====================================================
# DecisionAI System Prompt
# ====================================================

SYSTEM_PROMPT = """
You are DecisionAI, an expert Business Intelligence,
Data Analytics and AI Consultant.

Your responsibilities:

1. Analyze uploaded business datasets.

2. Explain KPIs clearly.

3. Identify trends.

4. Detect business risks.

5. Recommend actionable improvements.

6. Never invent numbers.

7. Base every answer only on the provided dataset.

8. If information is unavailable, clearly state that.

9. Give concise but business-oriented answers.

10. Prefer bullet points whenever possible.
"""


# ====================================================
# Dataset Context
# ====================================================

def build_dataset_context(df):
    """
    Creates a concise dataset summary.
    """

    overview = dataset_overview(df)

    context = {

        "Rows":
            overview["Rows"],

        "Columns":
            overview["Columns"],

        "Numeric Columns":
            overview["Numeric Columns"],

        "Categorical Columns":
            overview["Categorical Columns"],

        "Columns List":
            list(df.columns)

    }

    return context


# ====================================================
# KPI Context
# ====================================================

def build_kpi_context(df):
    """
    Returns calculated KPIs.
    """

    return calculate_kpis(df)


# ====================================================
# Recommendation Context
# ====================================================

def build_recommendation_context(df):
    """
    Returns recommendation dictionary.
    """

    return generate_business_recommendations(df)


# ====================================================
# Convert Context to JSON
# ====================================================

def context_to_json(context):
    """
    Converts dictionaries into readable JSON.
    """

    return json.dumps(
        context,
        indent=4,
        default=str
    )
# ====================================================
# General Question Prompt
# ====================================================

def build_question_prompt(df, user_question):
    """
    Builds a prompt for answering user questions
    about the uploaded dataset.
    """

    dataset = context_to_json(
        build_dataset_context(df)
    )

    kpis = context_to_json(
        build_kpi_context(df)
    )

    recommendations = context_to_json(
        build_recommendation_context(df)
    )

    prompt = f"""
Dataset Information
-------------------
{dataset}

Business KPIs
-------------
{kpis}

Business Recommendations
------------------------
{recommendations}

User Question
-------------
{user_question}

Instructions
------------
1. Answer ONLY using the dataset context above.
2. Never invent values.
3. If information is unavailable, clearly say so.
4. Explain in simple business language.
5. Give actionable insights whenever possible.
"""

    return prompt


# ====================================================
# Executive Summary Prompt
# ====================================================

def build_executive_summary_prompt(df):
    """
    Prompt for generating an executive report.
    """

    dataset = context_to_json(
        build_dataset_context(df)
    )

    kpis = context_to_json(
        build_kpi_context(df)
    )

    prompt = f"""
Dataset Summary
---------------
{dataset}

KPIs
----
{kpis}

Prepare an Executive Summary.

Include:

1. Overall business performance

2. Revenue overview

3. Profit overview

4. Customer overview

5. Product overview

6. Business risks

7. Growth opportunities

8. Final recommendations

Use professional business language.
"""

    return prompt


# ====================================================
# KPI Explanation Prompt
# ====================================================

def build_kpi_prompt(df):
    """
    Prompt for KPI explanation.
    """

    kpis = context_to_json(
        build_kpi_context(df)
    )

    return f"""
Business KPIs

{kpis}

Explain:

1. What each KPI means.

2. Why it is important.

3. Whether the KPI is good or bad.

4. How management can improve it.

Keep explanations concise.
"""


# ====================================================
# Recommendation Prompt
# ====================================================

def build_recommendation_prompt(df):
    """
    Prompt for AI business recommendations.
    """

    recommendations = context_to_json(
        build_recommendation_context(df)
    )

    return f"""
Business Recommendations

{recommendations}

Create a structured management report.

Include:

• Priority actions

• Revenue improvements

• Customer strategy

• Product strategy

• Cost reduction ideas

• Long-term growth suggestions
"""


# ====================================================
# Chart Explanation Prompt
# ====================================================

def build_chart_prompt(chart_name):
    """
    Prompt for chart interpretation.
    """

    return f"""
Explain the business meaning of the chart:

{chart_name}

Include:

1. What the chart shows

2. Important trends

3. Risks

4. Opportunities

5. Recommended actions
"""