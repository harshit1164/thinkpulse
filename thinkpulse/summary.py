import pandas as pd
from .explainer import explain_summary_data

def summary(data, language="en"):
    """
    Generate a column-wise summary of the dataset.

    Parameters:
    - data (str or pd.DataFrame): CSV file path or DataFrame
    - language (str): 'en' (default) or 'hi' for Hindi output

    Outputs:
    - Prints column-wise info: name, dtype, missing, unique, mean, median
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

        stats = []
        for col in df.columns:
            col_data = df[col]
            info = {
                "name": col,
                "dtype": str(col_data.dtype),
                "missing": int(col_data.isnull().sum()),
                "unique": int(col_data.nunique())
            }

            if pd.api.types.is_numeric_dtype(col_data):
                info["mean"] = round(col_data.mean(), 2)
                info["median"] = round(col_data.median(), 2)
            else:
                info["mean"] = "-"
                info["median"] = "-"

            stats.append(info)

        explain_summary_data(stats, language)

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except pd.errors.EmptyDataError:
        print("❌ File is empty or not a valid CSV.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
