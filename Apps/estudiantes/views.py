from django.shortcuts import render, redirect
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion
from .forms import EstudiantePublicadorForm, PublicacionForm


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


def crear_estudiante_publicador(request):
    if request.method == 'POST':
        form = EstudiantePublicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudiantePublicadorForm()
    return render(request, 'estudiantes/crear_estudiante_publicador.html', {'form': form})


def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'estudiantes/crear_publicacion.html', {'form': form})
