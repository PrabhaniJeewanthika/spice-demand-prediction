import pandas as pd

file1 = "datasets/raw/sales_history_2023.csv"
file2 = "datasets/raw/sales_history_2024.csv"
file3 = "datasets/raw/sales_history_2025.csv"

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

combined = pd.concat(
    [df1, df2, df3],
    ignore_index=True
)

combined.to_csv(
    "datasets/processed/combined_sales.csv",
    index=False
)

print("Dataset Combined Successfully")
print(combined.head())