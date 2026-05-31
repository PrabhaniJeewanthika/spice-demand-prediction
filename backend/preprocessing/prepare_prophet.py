import pandas as pd

df = pd.read_csv(
    "datasets/processed/transformed_sales.csv"
)

prophet_df = df[
    ['date', 'quantity_sold']
]

prophet_df = prophet_df.rename(
    columns={
        'date': 'ds',
        'quantity_sold': 'y'
    }
)

prophet_df.to_csv(
    "datasets/processed/prophet_dataset.csv",
    index=False
)

print(prophet_df.head())