from django.shortcuts import render, redirect
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion
from .forms import EstudiantePublicadorForm, PublicacionForm
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Apps.administradores.models import Administrador


@login_required(login_url='/usuarios/login/')
def lista_publicadores(request):
    publicadores = EstudiantePublicador.objects.all()
    return render(request, 'estudiantes/lista_publicadores.html', {'publicadores': publicadores})

@login_required(login_url='/usuarios/login/')
def lista_autorizadores(request):
    autorizadores = EstudianteAutorizador.objects.all()
    return render(request, 'estudiantes/lista_autorizadores.html', {'autorizadores': autorizadores})

@login_required(login_url='/usuarios/login/')
def lista_publicaciones(request):
    query = request.GET.get('buscar')
    if query:
        publicaciones = Publicacion.objects.filter(
            Q(titulo__icontains=query) | 
            Q(contenido__icontains=query) |
            Q(publicador__nombre__icontains=query) |
            Q(publicador__apellido__icontains=query) |
            Q(autorizador__nombre__icontains=query) |
            Q(autorizador__apellido__icontains=query)
        )
    else:
        publicaciones = Publicacion.objects.all()
    
    return render(request, 'estudiantes/lista_publicaciones.html', {
        'publicaciones': publicaciones,
        'query': query
    })

@login_required(login_url='/usuarios/login/')
def lista_estudiantes(request):
    query = request.GET.get('buscar')
    if query:
        estudiantes = EstudiantePublicador.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) |
            Q(correo__icontains=query)
        )
    else:
        estudiantes = EstudiantePublicador.objects.all()
    
    return render(request, 'estudiantes/estudiantes.html', {
        'estudiantes': estudiantes,
        'query': query
    })


@login_required(login_url='/usuarios/login/')
def crear_estudiante_publicador(request):
    if request.method == 'POST':
        form = EstudiantePublicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudiantePublicadorForm()
    return render(request, 'estudiantes/crear_estudiante_publicador.html', {'form': form})


@login_required(login_url='/usuarios/login/')
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
