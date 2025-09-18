from django.urls import path
from . import views

urlpatterns = [
    path('publicadores/', views.lista_publicadores, name='lista_publicadores'),
    path('autorizadores/', views.lista_autorizadores, name='lista_autorizadores'),
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
]