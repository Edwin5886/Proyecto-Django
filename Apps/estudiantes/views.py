from django.shortcuts import render, redirect
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion
from .forms import EstudiantePublicadorForm, PublicacionForm
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from Apps.administradores.models import Administrador


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


class DetallePublicacionView(DetailView):
    model = Publicacion
    template_name = 'estudiantes/detalle_publicacion.html'
    context_object_name = 'publicacion'

class EditarPublicacionView(UpdateView):
    model = Publicacion
    fields = ['titulo', 'contenido', 'autorizador']
    template_name = 'estudiantes/editar_publicacion.html'
    success_url = reverse_lazy('lista_publicaciones')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Publicación'
        return context

class DetalleEstudianteView(DetailView):
    model = EstudiantePublicador
    template_name = 'estudiantes/detalle_estudiante.html'
    context_object_name = 'estudiante'

class EditarEstudianteView(UpdateView):
    model = EstudiantePublicador
    fields = ['nombre', 'apellido', 'correo']
    template_name = 'estudiantes/editar_estudiante.html'
    success_url = reverse_lazy('lista_estudiantes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Estudiante'
        return context

class DetalleAdministradorView(DetailView):
    model = Administrador
    template_name = 'estudiantes/detalle_administrador.html'
    context_object_name = 'administrador'

class EditarAdministradorView(UpdateView):
    model = Administrador
    fields = ['nombre', 'apellido', 'email', 'telefono', 'cargo']
    template_name = 'estudiantes/editar_administrador.html'
    success_url = reverse_lazy('lista_administradores')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Administrador'
        return context
