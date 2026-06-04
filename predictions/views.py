from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DemandPrediction
from .serializers import DemandPredictionSerializer

@api_view(['GET'])
def get_predictions(request):

    predictions = DemandPrediction.objects.all().order_by('-prediction_date')

    serializer = DemandPredictionSerializer(
        predictions,
        many=True
    )

    return Response(serializer.data)