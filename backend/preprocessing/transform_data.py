import pandas as pd

df = pd.read_csv(
    "datasets/cleaned/clean_sales.csv"
)

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values('date')

df.to_csv(
    "datasets/processed/transformed_sales.csv",
    index=False
)

print(df.head())
print(df.dtypes)