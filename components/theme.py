"""
====================================================
DecisionAI Theme Loader
====================================================

Loads the global CSS stylesheet.
"""

import streamlit as st


def load_css():
    """
    Load the application's global CSS.
    """

    try:

        with open(
            "styles/style.css",
            encoding="utf-8"
        ) as css:

            st.markdown(

                f"""
                <style>
                {css.read()}
                </style>
                """,

                unsafe_allow_html=True

            )

    except FileNotFoundError:

        st.warning(
            "styles/style.css not found."
        )