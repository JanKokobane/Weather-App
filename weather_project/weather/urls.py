from django.urls import path
from .views import get_weather, home

urlpatterns = [
    path('', home, name='home'),
    path('api/weather/', get_weather, name='get_weather'),
]
