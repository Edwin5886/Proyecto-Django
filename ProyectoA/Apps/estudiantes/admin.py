from django.contrib import admin
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion

# Register your models here.
admin.site.register(EstudiantePublicador)
admin.site.register(EstudianteAutorizador)
admin.site.register(Publicacion)