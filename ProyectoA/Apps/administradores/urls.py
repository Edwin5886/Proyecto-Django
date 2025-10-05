from django.urls import path
from . import views

urlpatterns = [
    path('', views.administradores, name='lista_administradores'),
    path('crear/', views.crear_administrador, name='crear_administrador'),
]