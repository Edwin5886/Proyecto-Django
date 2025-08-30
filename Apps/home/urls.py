from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('administradores/', views.administradores, name='administradores'),
]