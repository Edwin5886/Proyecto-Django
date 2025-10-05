from django.urls import path
from . import views
from .views import DetalleEstudianteView, EditarEstudianteView, DetallePublicacionView, EditarPublicacionView

urlpatterns = [
    path('publicadores/', views.lista_publicadores, name='lista_publicadores'),
    path('autorizadores/', views.lista_autorizadores, name='lista_autorizadores'),
    path('publicaciones/', views.lista_publicaciones, name='lista_publicaciones'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante_publicador, name='crear_estudiante_publicador'),
    path('publicaciones/crear/', views.crear_publicacion, name='crear_publicacion'),
    path('estudiante/<int:pk>/', DetalleEstudianteView.as_view(), name='detalle_estudiante'),
    path('estudiante/<int:pk>/editar/', EditarEstudianteView.as_view(), name='editar_estudiante'),
    path('publicacion/<int:pk>/', DetallePublicacionView.as_view(), name='detalle_publicacion'),
    path('publicacion/<int:pk>/editar/', EditarPublicacionView.as_view(), name='editar_publicacion'),
]