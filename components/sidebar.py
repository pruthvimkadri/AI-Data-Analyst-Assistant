"""
====================================================
DecisionAI Sidebar
====================================================

Reusable Streamlit sidebar.
"""

import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.

    Returns
    -------
    api_key : str

    uploaded_file : UploadedFile

    page : str
    """

    with st.sidebar:

        st.title("📊 DecisionAI")

        st.caption(
            "AI-Powered Business Intelligence"
        )

        st.divider()

        # ------------------------------------
        # Dataset Upload
        # ------------------------------------

        st.subheader("📁 Dataset")

        uploaded_file = st.file_uploader(
            "Upload CSV Dataset",
            type=["csv"]
        )

        st.divider()

        # ------------------------------------
        # OpenAI
        # ------------------------------------

        st.subheader("🤖 AI Settings")

        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Enter your OpenAI API Key to enable AI features."
        )

        st.divider()

        # ------------------------------------
        # Navigation
        # ------------------------------------

        st.subheader("🧭 Navigation")

        page = st.radio(
            "Go to",
            [
                "Overview",
                "Dashboard",
                "AI Assistant",
                "Reports",
                "Export"
            ]
        )

        st.divider()

        # ------------------------------------
        # Footer
        # ------------------------------------

        st.caption("Version 1.0")

        st.caption(
            "Built with ❤️ using Streamlit"
        )

    return api_key, uploaded_file, page