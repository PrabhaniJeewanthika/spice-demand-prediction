import pandas as pd

df = pd.read_csv(
    "datasets/processed/combined_sales.csv"
)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())