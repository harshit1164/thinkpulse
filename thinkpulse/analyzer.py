import pandas as pd
from .explainer import explain_summary

def analyze(data, language="en"):
    """
    Analyze a dataset and print basic structural information.

    Parameters:
    - data (str or pd.DataFrame): File path to CSV or a Pandas DataFrame
    - language (str): 'en' for English (default), 'hi' for Hindi

    Output:
    - Prints the number of rows, columns, column names, and missing values.
    """
    try:
        if isinstance(data, str):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise TypeError("Input must be a CSV file path or a Pandas DataFrame.")

        if df.empty:
            print("⚠️ The dataset is empty.")
            return

        num_rows, num_cols = df.shape
        columns = list(df.columns)
        missing = df.isnull().sum().sum()

        summary = {
            "rows": num_rows,
            "columns": num_cols,
            "column_names": columns,
            "missing_values": missing
        }

        explain_summary(summary, language)

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except pd.errors.EmptyDataError:
        print("❌ File is empty or not a valid CSV.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
