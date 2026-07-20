import pandas as pd


def load_data(uploaded_file):
    """
    Load CSV or Excel file into a pandas DataFrame.
    """
    if uploaded_file is None:
        return None

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif file_name.endswith(".xlsx") or file_name.endswith(".xls"):
        df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload CSV or Excel file.")

    return df


def basic_cleaning(df):
    """
    Basic cleaning:
    - remove duplicates
    - trim column names
    """
    cleaned_df = df.copy()
    cleaned_df.columns = cleaned_df.columns.str.strip()
    cleaned_df = cleaned_df.drop_duplicates()
    return cleaned_df


def fill_missing_values(df):
    """
    Fill missing values:
    - numeric columns -> median
    - categorical columns -> mode
    """
    filled_df = df.copy()

    for col in filled_df.columns:
        if filled_df[col].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(filled_df[col]):
                filled_df[col] = filled_df[col].fillna(filled_df[col].median())
            else:
                mode_value = filled_df[col].mode()
                if not mode_value.empty:
                    filled_df[col] = filled_df[col].fillna(mode_value[0])
                else:
                    filled_df[col] = filled_df[col].fillna("Unknown")

    return filled_df


def get_summary(df):
    """
    Return useful summary details.
    """
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }
    return summary


def split_columns(df):
    """
    Return numeric and categorical columns.
    """
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()
    return numeric_cols, categorical_cols