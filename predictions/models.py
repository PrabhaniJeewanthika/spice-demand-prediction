from django.db import models


class SalesHistory(models.Model):
    product_name = models.CharField(max_length=255)
    quantity_sold = models.IntegerField()
    sales_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sales_history"
        ordering = ["sales_date"]
        verbose_name = "Sales History"
        verbose_name_plural = "Sales Histories"

    def __str__(self):
        return f"{self.product_name} - {self.sales_date}"


class DemandPrediction(models.Model):
    product_name = models.CharField(max_length=255)
    prediction_date = models.DateField()
    predicted_quantity = models.FloatField()

    confidence_score = models.FloatField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "demand_predictions"
        ordering = ["-prediction_date"]
        verbose_name = "Demand Prediction"
        verbose_name_plural = "Demand Predictions"

    def __str__(self):
        return f"{self.product_name} - {self.predicted_quantity}"


class ModelTrainingLog(models.Model):
    model_name = models.CharField(max_length=100)

    training_date = models.DateTimeField(
        auto_now_add=True
    )

    dataset_size = models.IntegerField()

    accuracy = models.FloatField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    class Meta:
        db_table = "model_training_logs"
        verbose_name = "Model Training Log"
        verbose_name_plural = "Model Training Logs"

    def __str__(self):
        return self.model_name