import joblib

model = joblib.load(
    "backend/models/demand_model.pkl"
)

future = model.make_future_dataframe(
    periods=30
)

forecast = model.predict(future)

print(
    forecast[
        ['ds', 'yhat']
    ].tail(30)
)