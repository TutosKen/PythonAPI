from django.urls import path
from . import views

urlpatterns = [
    path('getBalance', views.get_balance)
]
