from django.urls import path
from . import views

urlpatterns = [
    path('validateCredentials', views.validate_credentials),
    path('dummyEndpoint', views.dummyEndpoint)
]
