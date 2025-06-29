# import thinkpulse as tp

# # CSV file input (default English)
# tp.analyze("sales.csv")

# # Hindi output
# tp.analyze("sales.csv", language="hi")

# ############# Example usage of the summary function   ###################

# import thinkpulse as tp

# tp.summary("sales.csv")                      # English (default)
# tp.summary("sales.csv", language="hi")       # Hindi

# ############# Example usage of the highlight_outliers function   ###################
# import thinkpulse as tp

# tp.highlight_outliers("sales.csv", column="Sales")
# tp.highlight_outliers("sales.csv", column="Sales", language="hi")

# ############# Example usage of the insight function   ###################
# import thinkpulse as tp

# tp.insight("sales.csv")
# tp.insight("sales.csv", language="hi")


# ############# Example usage of the compare_datasets function   ###################
# import thinkpulse as tp

# tp.compare_datasets("sales.csv", "sales_v2.csv")
# tp.compare_datasets("sales.csv", "sales_v2.csv", language="hi")


# ############# Example usage of the explain_column function   ###################
# import thinkpulse as tp

# tp.explain_column("sales.csv", column="Sales")
# tp.explain_column("sales.csv", column="Sales", language="hi")


# ############# Example usage of the clean_column_names function   ###################
# # This function cleans column names in a CSV file and can also handle Hindi language.
# import thinkpulse as tp

# # Test CSV input
# df_cleaned = tp.clean_column_names("dirty.csv", case="snake", language="en")
# print(df_cleaned.head())

# # Hindi version
# tp.clean_column_names("dirty.csv", case="camel", language="hi")



############# Example usage of the detect_bias function   ###################
# This function detects bias in a dataset based on specified columns.
# It can handle both English and Hindi languages.


import thinkpulse as tp

# English
tp.detect_bias("hiring.csv", target="Hired", by="Gender")

# Hindi
tp.detect_bias("hiring.csv", target="Hired", by="Region", language="hi")
