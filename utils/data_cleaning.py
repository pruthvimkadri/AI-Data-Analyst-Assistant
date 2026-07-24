"""
====================================================
DecisionAI Data Cleaning Engine
====================================================

Part A
-------
✓ Imports
✓ Cleaning Report
✓ Dataset Summary
✓ Column Standardization
✓ Column Detection Helpers
✓ Data Quality Report
"""

import pandas as pd
import numpy as np
import re


# ====================================================
# Cleaning Report
# ====================================================

def initialize_report():
    """
    Creates an empty cleaning report that gets
    updated throughout the cleaning pipeline.
    """

    return {

        "Rows Before": 0,
        "Rows After": 0,

        "Columns Before": 0,
        "Columns After": 0,

        "Duplicates Removed": 0,

        "Columns Renamed": {},

        "Numeric Columns Cleaned": [],

        "Date Columns Converted": [],

        "Missing Values Filled": {},

        "Errors": []

    }


# ====================================================
# Dataset Summary
# ====================================================

def dataset_summary(df, report=None):
    """
    Stores initial dataset information.
    """

    if report is None:
        report = initialize_report()

    report["Rows Before"] = len(df)
    report["Columns Before"] = len(df.columns)

    return report


# ====================================================
# Standardize Column Names
# ====================================================

def standardize_column_names(df, report=None):
    """
    Example

    Sales Amount
        ↓

    sales_amount
    """

    df = df.copy()

    mapping = {}

    for column in df.columns:

        new_name = (
            str(column)
            .strip()
            .lower()
        )

        new_name = re.sub(
            r"[^\w]+",
            "_",
            new_name
        )

        new_name = re.sub(
            "_+",
            "_",
            new_name
        )

        new_name = new_name.strip("_")

        mapping[column] = new_name

    df.rename(
        columns=mapping,
        inplace=True
    )

    if report is not None:
        report["Columns Renamed"] = mapping

    return df


# ====================================================
# Detect Numeric Columns
# ====================================================

def detect_numeric_columns(df):

    return df.select_dtypes(
        include=np.number
    ).columns.tolist()


# ====================================================
# Detect Text Columns
# ====================================================

def detect_text_columns(df):

    return df.select_dtypes(
        include=["object", "string"]
    ).columns.tolist()


# ====================================================
# Detect Boolean Columns
# ====================================================

def detect_boolean_columns(df):

    return df.select_dtypes(
        include=["bool"]
    ).columns.tolist()


# ====================================================
# Detect Date Columns
# ====================================================


    ...
def detect_date_columns(df):
    
    """
    Detect likely date columns based on names.
    """

    keywords = [

    "date",
    "time",

    "order_date",
    "ship_date",
    "invoice_date",
    "purchase_date",
    "delivery_date",
    "join_date",
    "hire_date",
    "birth_date",
    "transaction_date"

]

    detected = []

    for column in df.columns:

        lower = column.lower()

        if any(
            keyword in lower
            for keyword in keywords
        ):
            detected.append(column)

    return detected


    ...

# ====================================================
# Data Quality Report
# ====================================================

def generate_data_quality_report(df):
    """
    Generates an advanced data quality report.
    """

    if df is None:
        raise ValueError(
            "generate_data_quality_report() received None instead of a DataFrame."
        )

    rows = len(df)
    columns = len(df.columns)

    missing = int(df.isna().sum().sum())
    duplicates = int(df.duplicated().sum())

    numeric = len(detect_numeric_columns(df))
    text = len(detect_text_columns(df))
    dates = len(detect_date_columns(df))

    memory = round(
        df.memory_usage(deep=True).sum() / 1024**2,
        2
    )

    total_cells = rows * columns

    missing_pct = round(
        (missing / total_cells) * 100,
        2
    ) if total_cells else 0

    duplicate_pct = round(
        (duplicates / rows) * 100,
        2
    ) if rows else 0

    # -------------------------
    # Quality Score
    # -------------------------

    score = 100

    score -= min(40, missing_pct)

    score -= min(20, duplicate_pct)

    score = max(0, round(score))

    if score >= 95:
        status = "Excellent"
    elif score >= 80:
        status = "Good"
    elif score >= 60:
        status = "Fair"
    else:
        status = "Poor"

    return {

        "Rows": rows,

        "Columns": columns,

        "Missing Values": missing,

        "Missing %": missing_pct,

        "Duplicate Rows": duplicates,

        "Duplicate %": duplicate_pct,

        "Numeric Columns": numeric,

        "Text Columns": text,

        "Date Columns": dates,

        "Memory (MB)": memory,

        "Quality Score": score,

        "Status": status

    }
# ====================================================
# Part B
# Cleaning Functions
# ====================================================


# ====================================================
# Remove Empty Rows
# ====================================================

def remove_empty_rows(df):
    """
    Removes rows where every column is missing.
    """

    df = df.copy()

    df = df.dropna(how="all")

    return df


# ====================================================
# Clean Text Columns
# ====================================================

def clean_text_columns(df):
    """
    Cleans text columns by:
    • trimming spaces
    • replacing blank values with NaN
    """

    df = df.copy()

    missing_tokens = {
        "",
        " ",
        "na",
        "n/a",
        "null",
        "none",
        "-",
        "--"
    }

    for column in detect_text_columns(df):

        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
        )

        df[column] = df[column].replace(
            list(missing_tokens),
            np.nan
        )

    return df


# ====================================================
# Clean Numeric Columns
# ====================================================

def clean_numeric_columns(
    df,
    report=None,
    min_success_rate=0.80
):
    """
    Converts numeric-looking text columns into numbers.

    Example:
        ₹12,500
        $99
        25%
    """

    df = df.copy()

    currency_pattern = r"[₹$€£,%]"

    for column in df.columns:

        if pd.api.types.is_numeric_dtype(df[column]):
            continue

        try:

            cleaned = (
                df[column]
                .astype(str)
                .str.replace(currency_pattern, "", regex=True)
                .str.replace(",", "", regex=False)
                .str.strip()
            )

            converted = pd.to_numeric(
                cleaned,
                errors="coerce"
            )

            success_rate = converted.notna().mean()

            if success_rate >= min_success_rate:

                df[column] = converted

                if report is not None:

                    report["Numeric Columns Cleaned"].append(column)

        except Exception as e:

            if report is not None:

                report["Errors"].append(
                    f"Numeric cleaning failed for '{column}': {e}"
                )

    return df


# ====================================================
# Clean Date Columns
# ====================================================

def clean_date_columns(
    df,
    report=None
):
    """
    Converts detected date columns to datetime.
    """

    df = df.copy()

    for column in detect_date_columns(df):

        # Skip year-only columns
        if column.lower().endswith("_year"):
            continue

        try:

            converted = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            success_rate = converted.notna().mean()

            if success_rate >= 0.70:

                df[column] = converted

                if report is not None:

                    report["Date Columns Converted"].append(column)

        except Exception as e:

            if report is not None:

                report["Errors"].append(
                    f"Date conversion failed for '{column}': {e}"
                )

    return df

# ====================================================
# Clean Boolean Columns
# ====================================================

def clean_boolean_columns(df):
    """
    Converts Yes/No, True/False, 1/0 columns
    into boolean values.
    """

    df = df.copy()

    true_values = {
        "yes",
        "y",
        "true",
        "1"
    }

    false_values = {
        "no",
        "n",
        "false",
        "0"
    }

    for column in detect_text_columns(df):

        values = (
            df[column]
            .dropna()
            .astype(str)
            .str.lower()
            .unique()
        )

        unique_values = set(values)

        if unique_values and unique_values.issubset(
            true_values.union(false_values)
        ):

            df[column] = (
                df[column]
                .astype(str)
                .str.lower()
                .map(
                    lambda x:
                    True if x in true_values
                    else False if x in false_values
                    else np.nan
                )
            )

    return df
# ====================================================
# Part C
# Missing Values, Duplicates & Cleaning Pipeline
# ====================================================


# ====================================================
# Fill Missing Values
# ====================================================

def fill_missing_values(
    df,
    report=None,
    strategy=None
):
    """
    Fill missing values.

    Numeric -> Median
    Text -> Mode
    Boolean -> Mode
    """

    df = df.copy()

    if strategy is None:
        strategy = {
            "numeric": "median",
            "categorical": "mode"
        }

    for column in df.columns:

        missing_before = int(df[column].isna().sum())

        if missing_before == 0:
            continue

        try:

            # ------------------------
            # Numeric columns
            # ------------------------

            if pd.api.types.is_numeric_dtype(df[column]):

                if strategy["numeric"] == "mean":
                    value = df[column].mean()

                elif strategy["numeric"] == "zero":
                    value = 0

                else:
                    value = df[column].median()

                df[column] = df[column].fillna(value)

            # ------------------------
            # Text / Category
            # ------------------------

            else:

                mode = df[column].mode()

                if not mode.empty:
                    df[column] = df[column].fillna(
                        mode.iloc[0]
                    )

            if report is not None:

                report["Missing Values Filled"][column] = (
                    missing_before
                )

        except Exception as e:

            if report is not None:

                report["Errors"].append(
                    f"Missing value filling failed for '{column}': {e}"
                )

    return df


# ====================================================
# Remove Duplicates
# ====================================================

def remove_duplicates(
    df,
    report=None
):
    """
    Removes duplicate rows.
    """

    df = df.copy()

    duplicates = int(df.duplicated().sum())

    df = df.drop_duplicates()

    if report is not None:

        report["Duplicates Removed"] = duplicates

    return df


# ====================================================
# Finalize Cleaning Report
# ====================================================

def finalize_report(
    df,
    report
):
    """
    Updates final dataset statistics.
    """

    report["Rows After"] = len(df)

    report["Columns After"] = len(df.columns)

    return report


# ====================================================
# Complete Cleaning Pipeline
# ====================================================

def clean_dataset(

    df,

    missing_strategy=None,

    remove_duplicate_rows=True,

    fill_missing=True,

    clean_numeric=True,

    clean_dates=True,

    clean_text=True,

    clean_booleans=True,

    numeric_success_rate=0.80

):
    """
    Complete DecisionAI Cleaning Pipeline.

    Returns
    -------
    cleaned_df
    cleaning_report
    """

    # ------------------------
    # Safety Checks
    # ------------------------

    if df is None:
        raise ValueError(
            "clean_dataset() received None instead of a DataFrame."
        )

    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "clean_dataset() expects a pandas DataFrame."
        )

    if missing_strategy is None:

        missing_strategy = {

            "numeric": "median",

            "categorical": "mode"

        }

    report = initialize_report()

    report = dataset_summary(
        df,
        report
    )

    # ------------------------
    # Standardize columns
    # ------------------------

    df = standardize_column_names(
        df,
        report
    )

    # ------------------------
    # Remove empty rows
    # ------------------------

    df = remove_empty_rows(df)

    # ------------------------
    # Clean text
    # ------------------------

    if clean_text:

        df = clean_text_columns(df)

    # ------------------------
    # Clean numeric
    # ------------------------

    if clean_numeric:

        df = clean_numeric_columns(
            df,
            report,
            min_success_rate=numeric_success_rate
        )

    # ------------------------
    # Clean dates
    # ------------------------

    if clean_dates:

        df = clean_date_columns(
            df,
            report
        )

    # ------------------------
    # Clean booleans
    # ------------------------

    if clean_booleans:

        df = clean_boolean_columns(df)

    # ------------------------
    # Fill Missing Values
    # ------------------------

    if fill_missing:

        df = fill_missing_values(
            df,
            report,
            strategy=missing_strategy
        )

    # ------------------------
    # Remove duplicates
    # ------------------------

    if remove_duplicate_rows:

        df = remove_duplicates(
            df,
            report
        )

    # ------------------------
    # Final validation
    # ------------------------

    if df is None:

        raise RuntimeError(
            "Cleaning pipeline produced None."
        )

    report = finalize_report(
        df,
        report
    )

    return df, report
# ====================================================
# Part D
# Cleaning Report Formatter
# ====================================================

def cleaning_report_text(report):
    """
    Converts the cleaning report into a
    readable text summary.
    """

    lines = []

    lines.append("=" * 50)
    lines.append("DECISIONAI DATA CLEANING REPORT")
    lines.append("=" * 50)

    lines.append(f"Rows Before      : {report['Rows Before']}")
    lines.append(f"Rows After       : {report['Rows After']}")

    lines.append("")

    lines.append(f"Columns Before   : {report['Columns Before']}")
    lines.append(f"Columns After    : {report['Columns After']}")

    lines.append("")

    lines.append(
        f"Duplicates Removed : {report['Duplicates Removed']}"
    )

    lines.append("")

    # --------------------------------------------
    # Renamed Columns
    # --------------------------------------------

    if report["Columns Renamed"]:

        lines.append("Columns Renamed")

        for old_name, new_name in report["Columns Renamed"].items():

            if old_name != new_name:

                lines.append(
                    f" • {old_name}  →  {new_name}"
                )

        lines.append("")

    # --------------------------------------------
    # Numeric Columns
    # --------------------------------------------

    if report["Numeric Columns Cleaned"]:

        lines.append("Numeric Columns Cleaned")

        for column in report["Numeric Columns Cleaned"]:

            lines.append(f" • {column}")

        lines.append("")

    # --------------------------------------------
    # Date Columns
    # --------------------------------------------

    if report["Date Columns Converted"]:

        lines.append("Date Columns Converted")

        for column in report["Date Columns Converted"]:

            lines.append(f" • {column}")

        lines.append("")

    # --------------------------------------------
    # Missing Values
    # --------------------------------------------

    if report["Missing Values Filled"]:

        lines.append("Missing Values Filled")

        for column, count in report["Missing Values Filled"].items():

            lines.append(
                f" • {column}: {count}"
            )

        lines.append("")

    # --------------------------------------------
    # Errors
    # --------------------------------------------

    if report["Errors"]:

        lines.append("Errors")

        for error in report["Errors"]:

            lines.append(f" • {error}")

        lines.append("")

    if not report["Errors"]:

        lines.append("No cleaning errors detected.")

    lines.append("=" * 50)

    return "\n".join(lines)