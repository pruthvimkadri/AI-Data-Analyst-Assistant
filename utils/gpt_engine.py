"""
====================================================
DecisionAI GPT Engine
====================================================

Handles communication with OpenAI.

Part A
-------
✓ OpenAI Client
✓ API Validation
✓ Chat Completion
"""

import os

from openai import OpenAI

from dotenv import load_dotenv


# ====================================================
# Load Environment Variables
# ====================================================

load_dotenv()


# ====================================================
# Default Model
# ====================================================

DEFAULT_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.5"
)


# ====================================================
# Create OpenAI Client
# ====================================================

def create_client(api_key=None):
    """
    Creates an OpenAI client.

    Parameters
    ----------
    api_key : str, optional

    Returns
    -------
    OpenAI Client
    """

    if api_key is None:

        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:

        raise ValueError(
            "OpenAI API Key not found."
        )

    return OpenAI(api_key=api_key)


# ====================================================
# Validate API Key
# ====================================================

def validate_api_key(api_key):
    """
    Returns True if an API key exists.
    """

    return (
        api_key is not None
        and len(api_key.strip()) > 20
    )


# ====================================================
# Chat Completion
# ====================================================

def chat_completion(
    client,
    system_prompt,
    user_prompt,
    model=DEFAULT_MODEL,
    temperature=0.3,
    max_tokens=1000
):
    """
    Sends a prompt to OpenAI and
    returns the generated response.
    """

    response = client.chat.completions.create(

        model=model,

        messages=[

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ],

        temperature=temperature,

        max_completion_tokens=max_tokens

    )

    return response.choices[0].message.content
# ====================================================
# Imports
# ====================================================

from .prompt_builder import (
    SYSTEM_PROMPT,
    build_question_prompt,
    build_executive_summary_prompt,
    build_kpi_prompt,
    build_recommendation_prompt
)


# ====================================================
# Ask DecisionAI
# ====================================================

def ask_decision_ai(
    client,
    df,
    question,
    model=DEFAULT_MODEL
):
    """
    Answers a user question using the dataset.
    """

    prompt = build_question_prompt(
        df,
        question
    )

    return chat_completion(
        client=client,
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt,
        model=model
    )


# ====================================================
# Executive Summary
# ====================================================

def generate_executive_summary(
    client,
    df,
    model=DEFAULT_MODEL
):
    """
    Generates an executive summary.
    """

    prompt = build_executive_summary_prompt(df)

    return chat_completion(
        client=client,
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt,
        model=model
    )
def explain_kpis(
    client,
    df,
    model=DEFAULT_MODEL
):
    """
    Explains all KPIs.
    """

    prompt = build_kpi_prompt(df)

    return chat_completion(
        client=client,
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt,
        model=model
    )


# ====================================================
# Business Recommendations
# ====================================================

def generate_ai_recommendations(
    client,
    df,
    model=DEFAULT_MODEL
):
    """
    Generates AI-powered recommendations.
    """

    prompt = build_recommendation_prompt(df)

    return chat_completion(
        client=client,
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt,
        model=model
    )


# ====================================================
# Safe GPT Call
# ====================================================

def safe_chat(
    func,
    *args,
    **kwargs
):
    """
    Executes GPT functions safely.
    Returns readable errors instead of crashing.
    """

    try:

        return func(
            *args,
            **kwargs
        )

    except Exception as e:

        return f"❌ AI Error:\n\n{str(e)}"
