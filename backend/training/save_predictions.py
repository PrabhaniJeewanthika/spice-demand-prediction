import os
import sys
import django
import joblib

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

django.setup()

from predictions.models import DemandPrediction

model = joblib.load(
    "backend/models/demand_model.pkl"
)

future = model.make_future_dataframe(
    periods=30
)

forecast = model.predict(future)

forecast = forecast[
    ['ds', 'yhat']
].tail(30)

for _, row in forecast.iterrows():
    DemandPrediction.objects.create(
        product_name="All Products",
        prediction_date=row["ds"],
        predicted_quantity=float(row["yhat"])
    )

print("Predictions saved successfully!")