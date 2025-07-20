import pandas as pd
from .explainer import explain_outliers

def highlight_outliers(data, column, language="en"):
    """
    Detect outliers in a numeric column using the IQR method.

    Parameters:
    - data (str or pd.DataFrame): CSV file path or DataFrame
    - column (str): Name of the numeric column to check
    - language (str): 'en' (default) or 'hi' for Hindi output

    Output:
    - Prints a list of outlier values with their row numbers
    """
    try:
        if isinstance(data, str):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise TypeError("Input must be a CSV path or a DataFrame.")

        if df.empty:
            print("Dataset is empty.")
            return

        if column not in df.columns:
            print(f"Column '{column}' not found.")
            return

        series = df[column].dropna()

        if not pd.api.types.is_numeric_dtype(series):
            print(f"Column '{column}' is not numeric.")
            return

        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outliers = df[(df[column] < lower) | (df[column] > upper)]

        explain_outliers(outliers, column, language)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
