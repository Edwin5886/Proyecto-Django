from django import forms
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion

class EstudiantePublicadorForm(forms.ModelForm):
    class Meta:
        model = EstudiantePublicador
        fields = ['nombre', 'apellido', 'correo']

class EstudianteAutorizadorForm(forms.ModelForm):
    class Meta:
        model = EstudianteAutorizador
        fields = ['nombre', 'apellido', 'correo']


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'publicador', 'autorizador']
