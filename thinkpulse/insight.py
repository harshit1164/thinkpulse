import pandas as pd
from .explainer import explain_insights

def insight(data, language="en"):
    """
    Generate human-like insights from a dataset.

    Parameters:
    - data (str or pd.DataFrame): CSV file path or DataFrame
    - language (str): 'en' (default) or 'hi' for Hindi output

    Output:
    - Prints interesting facts about missing values, max values, and categories
    """
    try:
        if isinstance(data, str):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise TypeError("Input must be a CSV path or DataFrame.")

        if df.empty:
            print("Dataset is empty.")
            return

        insights = []

        # Missing value insights
        for col in df.columns:
            nulls = df[col].isnull().sum()
            if nulls > 0:
                insights.append({
                    "type": "missing",
                    "column": col,
                    "value": nulls
                })

        # Peak values for numeric columns
        for col in df.select_dtypes(include="number").columns:
            max_val = df[col].max()
            max_row = df[df[col] == max_val]
            if not max_row.empty:
                context = ", ".join(str(v) for v in max_row.iloc[0].values if pd.notna(v))
                insights.append({
                    "type": "peak",
                    "column": col,
                    "value": max_val,
                    "context": context
                })

        # Unique category counts
        for col in df.select_dtypes(include="object").columns:
            unique = df[col].nunique()
            insights.append({
                "type": "category",
                "column": col,
                "value": unique
            })

        explain_insights(insights, language)

    except FileNotFoundError:
        print("File not found.")
