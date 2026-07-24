"""
====================================================
DecisionAI AI Assistant
====================================================

Interactive AI Business Assistant.

Author: DecisionAI
"""

import streamlit as st

from utils.ai_context import build_ai_context
from utils.prompt_builder import build_business_prompt
from utils.gpt_engine import ask_llm


def render_ai_assistant(df):
    """
    Render DecisionAI AI Assistant.
    """

    st.header("🤖 DecisionAI Business Assistant")

    st.caption(
        "Ask questions about your dataset and receive AI-powered business insights."
    )

    # --------------------------------------------------
    # API Key Validation
    # --------------------------------------------------

   

    # --------------------------------------------------
    # Build Business Context
    # --------------------------------------------------

    context = build_ai_context(df)

    # --------------------------------------------------
    # Initialize Chat History
    # --------------------------------------------------

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # --------------------------------------------------
    # Display Previous Messages
    # --------------------------------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --------------------------------------------------
    # Quick AI Actions
    # --------------------------------------------------

    st.subheader("⚡ Quick AI Actions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📊 Explain Dashboard"):
            st.session_state.quick_prompt = (
                "Explain the dashboard and summarize the most important findings."
            )

        if st.button("📈 Growth Opportunities"):
            st.session_state.quick_prompt = (
                "Identify growth opportunities from this dataset."
            )

        if st.button("⚠ Risk Analysis"):
            st.session_state.quick_prompt = (
                "Identify business risks and suggest mitigation strategies."
            )

    with col2:

        if st.button("📄 CEO Report"):
            st.session_state.quick_prompt = (
                "Generate an executive report for senior management."
            )

        if st.button("💰 Financial Analysis"):
            st.session_state.quick_prompt = (
                "Provide a financial performance analysis."
            )

        if st.button("🎯 Marketing Strategy"):
            st.session_state.quick_prompt = (
                "Suggest marketing recommendations based on this dataset."
            )

    # --------------------------------------------------
    # Chat Input
    # --------------------------------------------------

    prompt = st.chat_input("Ask DecisionAI anything...")

    if "quick_prompt" in st.session_state:
        prompt = st.session_state.pop("quick_prompt")

    if prompt:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing your business data..."):

                business_prompt = build_business_prompt(
                    context=context,
                    user_question=prompt
                )

                response = ask_llm(business_prompt)

                st.markdown(response)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    # --------------------------------------------------
    # Clear Chat
    # --------------------------------------------------

    st.divider()

    if st.button("🗑 Clear Conversation"):

        st.session_state.chat_history = []

        st.rerun()