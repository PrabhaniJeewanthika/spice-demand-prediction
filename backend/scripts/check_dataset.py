import pandas as pd

df = pd.read_csv(
    "../../datasets/raw/sales_history_2023.csv"
)

print(df.head())

print(df.info())

print(df.isnull().sum())