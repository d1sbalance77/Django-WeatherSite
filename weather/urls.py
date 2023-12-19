from django.urls import path
from . import views
from weather.views import MyLoginView
import weather.views


urlpatterns = [
    path('', views.index, name='WeatherMainPage'),
]
