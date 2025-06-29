import pandas as pd
from .explainer import explain_comparison

def compare_datasets(file1, file2, language="en"):
    """
    Compare two datasets and print a summary of differences.

    Parameters:
    - file1 (str): Path to first CSV file
    - file2 (str): Path to second CSV file
    - language (str): 'en' (default) or 'hi' for Hindi output

    Output:
    - Prints shape difference, column changes, row count diff,
      and missing value differences.
    """
    try:
        df1 = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
    except FileNotFoundError:
        print("❌ One or both files not found.")
        return
    except Exception as e:
        print(f"❌ Error reading files: {e}")
        return

    report = []

    # Shape difference
    if df1.shape != df2.shape:
        report.append({
            "type": "shape",
            "file1": df1.shape,
            "file2": df2.shape
        })

    # Columns added/removed
    cols1 = set(df1.columns)
    cols2 = set(df2.columns)
    added = list(cols2 - cols1)
    removed = list(cols1 - cols2)

    if added:
        report.append({"type": "columns_added", "columns": added})
    if removed:
        report.append({"type": "columns_removed", "columns": removed})

    # Compare missing value changes
    for col in cols1 & cols2:
        m1 = df1[col].isnull().sum()
        m2 = df2[col].isnull().sum()
        if m1 != m2:
            report.append({
                "type": "missing_changed",
                "column": col,
                "file1": m1,
                "file2": m2
            })

    # Compare row count
    if len(df1) != len(df2):
        report.append({
            "type": "rows_diff",
            "file1": len(df1),
            "file2": len(df2)
        })

    explain_comparison(report, language)
