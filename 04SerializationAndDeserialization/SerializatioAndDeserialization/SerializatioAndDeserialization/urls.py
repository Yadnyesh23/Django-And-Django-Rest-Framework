from django.contrib import admin
from django.urls import path
from .views import healthcheck
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/healthcheck', healthcheck)
]
