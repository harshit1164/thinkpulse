import pandas as pd
import scipy.stats as stats
from .explainer import explain_bias_result

def detect_bias(data, target, by, language="en"):
    """
    Detects bias in a dataset using a Chi-square test.

    Parameters:
    - data (str or pd.DataFrame): CSV file path or DataFrame
    - target (str): Target column (e.g., Hired, Passed)
    - by (str): Group column to check bias on (e.g., Gender, Region)
    - language (str): 'en' (default) or 'hi' for Hindi output

    Output:
    - Prints whether bias exists, along with statistical interpretation.
    """
    try:
        if isinstance(data, str):
            df = pd.read_csv(data)
        elif isinstance(data, pd.DataFrame):
            df = data.copy()
        else:
            raise TypeError("Input must be CSV path or DataFrame")

        if df.empty:
            print("Dataset is empty.")
            return

        if target not in df.columns or by not in df.columns:
            print(f"Columns '{target}' or '{by}' not found in data.")
            return

        contingency = pd.crosstab(df[by], df[target])

        if contingency.shape[0] < 2 or contingency.shape[1] < 2:
            print("Not enough categories for bias test.")
            return

        chi2, p, dof, _ = stats.chi2_contingency(contingency)
        result = {
            "by": by,
            "target": target,
            "p_value": round(p, 5),
            "significant": p < 0.05
        }

        explain_bias_result(result, language)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error: {e}")
