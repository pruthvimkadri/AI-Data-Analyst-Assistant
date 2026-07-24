"""
=========================================================
DecisionAI Gemini Engine
=========================================================

Responsible only for communicating with Gemini.

Author: DecisionAI
"""

import os
import re
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# ---------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------------------------------------------------
# Ask Gemini
# ---------------------------------------------------------

def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns a cleaned response.
    """

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        text = response.text or ""
        # -------------------------------------------------
        # Cleanup Formatting
        # -------------------------------------------------

        # Remove excessive blank lines
        # Remove trailing spaces
        text = re.sub(r"[ \t]+\n", "\n", text)

# Fix escaped Markdown
        text = text.replace("\\*", "*")
        text = text.replace("\\_", "_")

# -------------------------------
# Fix Markdown Bold Formatting
# -------------------------------

# Remove spaces after opening **
# Example: ** Consumer -> **Consumer
        text = re.sub(r"\*\*\s+", "**", text)

# Remove spaces before closing **
# Example: Consumer ** -> Consumer**
        text = re.sub(r"\s+\*\*", "**", text)

# Remove unmatched bold markers
        if text.count("**") % 2 != 0:
           text = text.replace("**", "")

# Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Add space after common articles
        text = re.sub(r"\b(the|The)([A-Z][a-z])", r"\1 \2", text)

# Add space after a bold section if immediately followed by a word
        text = re.sub(r"(\*\*[^\*]+\*\*)([A-Za-z])", r"\1 \2", text)

# Add space between lowercase and uppercase letters
# Example: WestRegion -> West Region
        text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
        # Add space after bold text if Gemini omits it
        text = re.sub(r"(\*\*[^\*]+\*\*)(?=[A-Za-z])", r"\1 ", text)
        return text.strip()
        
    except Exception as e:

     error = str(e)

     if "RESOURCE_EXHAUSTED" in error or "429" in error:
        return """
## ⚠️ Gemini API Quota Exceeded

Your Gemini API project has reached its current free-tier request limit.

Possible solutions:

- Wait for the daily quota to reset
- Enable billing for your Google AI Studio project
- Use another Gemini API key

Your application is working correctly. Only the API quota has been exhausted.
"""

     elif "API_KEY" in error or "API key" in error:
        return """
## ❌ Invalid Gemini API Key

Please check your GEMINI_API_KEY in Streamlit Secrets or your .env file.
"""

     else:
        return f"""
## ❌ Gemini Error

{error}

Please verify:

- Internet connection
- Gemini API Key
- Model availability
"""

# ---------------------------------------------------------
# KPI Explanation
# ---------------------------------------------------------

def explain_kpis(kpis_text: str) -> str:

    prompt = f"""
You are an experienced Business Intelligence Analyst.

Explain the following KPIs in simple business language.

KPIs:

{kpis_text}
"""

    return ask_llm(prompt)


# ---------------------------------------------------------
# Executive Summary
# ---------------------------------------------------------

def generate_executive_summary(summary_text: str) -> str:

    prompt = f"""
You are an Executive Business Consultant.

Write a concise executive summary for the following analysis.

Analysis:

{summary_text}

Requirements:

- Maximum 200 words
- Professional tone
- Highlight key business insights
- Mention opportunities and risks
- End with one actionable recommendation
"""

    return ask_llm(prompt)