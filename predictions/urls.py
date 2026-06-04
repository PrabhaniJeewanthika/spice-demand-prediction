from django.urls import path

from .views import (
    get_predictions,
    dashboard_summary
)

urlpatterns = [

    path(
        'predictions/',
        get_predictions
    ),

    path(
        'dashboard-summary/',
        dashboard_summary
    ),

]