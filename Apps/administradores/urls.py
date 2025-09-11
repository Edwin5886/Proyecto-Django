from django.urls import path
from . import views

urlpatterns = [
    path('', views.administradores, name='administradores'),
]