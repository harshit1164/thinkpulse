import pandas as pd
import re
from .explainer import explain_cleaned_columns

def clean_column_names(data, case="snake", language="en"):
    """
    Clean column names by removing symbols, spaces, and formatting to snake_case or camelCase.

    Parameters:
    - data (str or pd.DataFrame): CSV file path or DataFrame
    - case (str): 'snake' (default) or 'camel'
    - language (str): 'en' (default) or 'hi' for Hindi output

    Returns:
    - pd.DataFrame: DataFrame with cleaned column names
    """
    try:
        if isinstance(data, str):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise TypeError("Input must be a file path or a DataFrame.")

        old_cols = df.columns.tolist()
        new_cols = []

        for col in old_cols:
            cleaned = re.sub(r'[^a-zA-Z0-9]+', '_', col).strip('_')
            if case == "snake":
                cleaned = cleaned.lower()
            elif case == "camel":
                parts = cleaned.lower().split('_')
                cleaned = parts[0] + ''.join(word.capitalize() for word in parts[1:])
            new_cols.append(cleaned)

        df.columns = new_cols

        explain_cleaned_columns(old_cols, new_cols, language)
        return df

    except Exception as e:
        print(f"❌ Error: {e}")
        return None
