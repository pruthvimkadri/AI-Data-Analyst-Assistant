"""
====================================================
DecisionAI Footer
====================================================

Reusable application footer.
"""

import streamlit as st


def render_footer():
    """
    Render the application footer.
    """

    st.divider()

    col1, col2, col3 = st.columns([3, 2, 2])

    with col1:

        st.caption(
            "📊 DecisionAI • AI-Powered Business Intelligence Platform"
        )

    with col2:

        st.caption(
            "Version 1.0.0"
        )

    with col3:

        st.caption(
            "Built with ❤️ using Streamlit"
        )