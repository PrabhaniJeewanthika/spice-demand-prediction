import pandas as pd
import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from predictions.models import SalesHistory

df = pd.read_csv(
    "datasets/processed/combined_sales.csv"
)

for _, row in df.iterrows():

    SalesHistory.objects.create(
        product_name=row['product_name'],
        quantity_sold=row['quantity_sold'],
        sales_date=row['date']
    )

print("Data Imported Successfully")