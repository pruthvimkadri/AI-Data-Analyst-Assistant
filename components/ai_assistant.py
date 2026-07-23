"""
====================================================
DecisionAI AI Assistant
====================================================

Interactive AI chat interface.
"""

import streamlit as st

from utils.gpt_engine import (
    create_client,
    ask_decision_ai,
    safe_chat
)


def render_ai_assistant(df, api_key):
    """
    Render the AI Assistant page.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned dataset.

    api_key : str
        OpenAI API Key.
    """

    st.header("🤖 DecisionAI Assistant")

    st.write(
        "Ask questions about your uploaded dataset."
    )

    # -----------------------------------------
    # API Key Validation
    # -----------------------------------------

    if not api_key:

        st.warning(
            "Please enter your OpenAI API Key in the sidebar."
        )

        return

    # -----------------------------------------
    # Initialize Chat History
    # -----------------------------------------

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    # -----------------------------------------
    # Display Previous Messages
    # -----------------------------------------

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # -----------------------------------------
    # Chat Input
    # -----------------------------------------

    prompt = st.chat_input(
        "Ask DecisionAI..."
    )

    if prompt:

        # User Message

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        # Assistant Response

        with st.chat_message("assistant"):

            with st.spinner(
                "Analyzing dataset..."
            ):

                client = create_client(api_key)

                response = safe_chat(
                    ask_decision_ai,
                    client,
                    df,
                    prompt
                )

                st.markdown(response)

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

    # -----------------------------------------
    # Clear Conversation
    # -----------------------------------------

    st.divider()

    if st.button("🗑 Clear Conversation"):

        st.session_state.chat_history = []

        st.rerun()