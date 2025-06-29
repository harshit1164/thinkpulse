import pandas as pd
from .explainer import explain_column_output

def explain_column(data, column, language="en"):
    """
    Provide detailed explanation of a single column.

    Parameters:
    - data (str or pd.DataFrame): CSV file path or DataFrame
    - column (str): Column name to analyze
    - language (str): 'en' (default) or 'hi' for Hindi output

    Output:
    - Prints dtype, missing values, uniqueness, and target suitability
    """
    try:
        if isinstance(data, str):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise TypeError("Input must be a CSV file path or a DataFrame.")

        if df.empty:
            print("⚠️ Dataset is empty.")
            return

        if column not in df.columns:
            print(f"⚠️ Column '{column}' not found.")
            return

        series = df[column]
        info = {
            "column": column,
            "dtype": "numeric" if pd.api.types.is_numeric_dtype(series) else "categorical",
            "missing": int(series.isnull().sum()),
            "unique": int(series.nunique()),
            "total": len(series),
            "language": language
        }

        info["binary_like"] = info["unique"] <= 10

        explain_column_output(info)

    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
