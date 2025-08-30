from django.apps import AppConfig
from django.urls import path
from . import views 

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.home'
