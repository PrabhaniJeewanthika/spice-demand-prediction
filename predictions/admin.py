from django.contrib import admin
from .models import (
    SalesHistory,
    DemandPrediction,
    ModelTrainingLog
)


@admin.register(SalesHistory)
class SalesHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "quantity_sold",
        "sales_date"
    )

    search_fields = (
        "product_name",
    )

    list_filter = (
        "sales_date",
    )


@admin.register(DemandPrediction)
class DemandPredictionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_name",
        "prediction_date",
        "predicted_quantity",
        "confidence_score"
    )

    search_fields = (
        "product_name",
    )

    list_filter = (
        "prediction_date",
    )


@admin.register(ModelTrainingLog)
class ModelTrainingLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "model_name",
        "dataset_size",
        "accuracy",
        "training_date"
    )