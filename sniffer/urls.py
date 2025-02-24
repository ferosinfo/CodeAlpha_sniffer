from django.urls import path
from . import views

urlpatterns = [
    path('', views.sniff_traffic, name='sniff_traffic'),
]