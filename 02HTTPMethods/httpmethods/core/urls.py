from django.urls import path
from .views import httpmethod

urlpatterns = [
    path("httpmethod/", httpmethod)
]
