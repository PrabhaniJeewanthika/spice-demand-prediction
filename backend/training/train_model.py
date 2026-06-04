import pandas as pd
import joblib
from prophet import Prophet

df = pd.read_csv(
    "datasets/processed/prophet_dataset.csv"
)

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model.fit(df)

joblib.dump(
    model,
    "backend/models/demand_model.pkl"
)

print("Model trained successfully")