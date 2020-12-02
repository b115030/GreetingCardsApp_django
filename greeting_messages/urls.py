from django.urls import path
from .views import get_data_from_backend

urlpatterns = [
    path('', get_data_from_backend)
]