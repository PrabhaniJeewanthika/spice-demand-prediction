from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg

from .models import DemandPrediction


@api_view(['GET'])
def get_predictions(request):

    predictions = DemandPrediction.objects.all()

    result = []

    for item in predictions:
        result.append({
            "id": item.id,
            "product_name": item.product_name,
            "prediction_date": item.prediction_date,
            "predicted_quantity": item.predicted_quantity,
            "confidence_score": item.confidence_score,
        })

    return Response(result)


@api_view(['GET'])
def dashboard_summary(request):

    total_predictions = DemandPrediction.objects.count()

    avg_prediction = DemandPrediction.objects.aggregate(
        Avg("predicted_quantity")
    )

    return Response({
        "total_predictions": total_predictions,
        "average_prediction":
            avg_prediction["predicted_quantity__avg"] or 0
    })