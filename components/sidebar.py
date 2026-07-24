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
    uploaded_file : UploadedFile
    page : str
    """

    with st.sidebar:

        st.title("📊 DecisionAI")

        st.caption("AI-Powered Business Intelligence")

        st.divider()

        # ------------------------------------
        # Dataset Upload
        # ------------------------------------

        st.subheader("📁 Dataset")

        uploaded_file = st.file_uploader(
            "Upload CSV Dataset",
            type=["csv"],
            help="Upload a business dataset in CSV format."
        )

        st.divider()

        # ------------------------------------
        # AI Status
        # ------------------------------------

        st.subheader("🤖 AI")

        st.success("✅ Gemini Connected")
        st.caption("Model: Gemini Flash Latest")

        st.divider()

        # ------------------------------------
        # Navigation
        # ------------------------------------

        st.subheader("🧭 Navigation")

        page = st.radio(
            "Select Page",
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

        st.caption("DecisionAI v1.0")
        st.caption("Built with ❤️ using Streamlit + Gemini")

    return uploaded_file, page