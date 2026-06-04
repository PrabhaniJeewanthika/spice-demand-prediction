from rest_framework import serializers
from .models import DemandPrediction

class DemandPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandPrediction
        fields = "__all__"