import pandas as pd

df = pd.read_csv(
    "datasets/processed/combined_sales.csv"
)

print("Before Cleaning")
print(df.shape)

# remove duplicates
df = df.drop_duplicates()

# remove null values
df = df.dropna()

# remove negative sales
df = df[df['quantity_sold'] >= 0]

print("After Cleaning")
print(df.shape)

df.to_csv(
    "datasets/cleaned/clean_sales.csv",
    index=False
)

print("Cleaning Complete")