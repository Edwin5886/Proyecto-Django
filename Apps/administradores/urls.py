from django.urls import path
from . import views
from .views import DetalleAdministradorView, EditarAdministradorView

urlpatterns = [
    path('', views.administradores, name='lista_administradores'),
    path('crear/', views.crear_administrador, name='crear_administrador'),
    path('administrador/<int:pk>/', DetalleAdministradorView.as_view(), name='detalle_administrador'),
    path('administrador/<int:pk>/editar/', EditarAdministradorView.as_view(), name='editar_administrador'),
]