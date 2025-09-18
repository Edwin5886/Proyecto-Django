from django.shortcuts import render
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion


def lista_publicadores(request):
    publicadores = EstudiantePublicador.objects.all()
    return render(request, 'estudiantes/lista_publicadores.html', {'publicadores': publicadores})

def lista_autorizadores(request):
    autorizadores = EstudianteAutorizador.objects.all()
    return render(request, 'estudiantes/lista_autorizadores.html', {'autorizadores': autorizadores})

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'estudiantes/lista_publicaciones.html', {'publicaciones': publicaciones})

def lista_estudiantes(request):
    estudiantes = EstudiantePublicador.objects.all()
    return render(request, 'estudiantes/estudiantes.html', {'estudiantes': estudiantes})
