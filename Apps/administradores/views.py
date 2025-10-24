from django.shortcuts import render, redirect
from .models import Administrador
from .forms import AdministradorForm
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='/usuarios/login/')
def administradores(request):
    query = request.GET.get('buscar')
    if query:
        administradores = Administrador.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query)
        )
    else:
        administradores = Administrador.objects.all()
    
    return render(request, 'home/administradores.html', {
        'administradores': administradores,
        'query': query
    })

@login_required(login_url='/usuarios/login/')
def crear_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_administradores')
    else:
        form = AdministradorForm()
    return render(request, 'administradores/crear_administrador.html', {'form': form})


class DetalleAdministradorView(DetailView):
    model = Administrador
    template_name = 'administradores/detalle_administrador.html'
    context_object_name = 'administrador'


class EditarAdministradorView(UpdateView):
    model = Administrador
    fields = ['nombre', 'apellido']
    template_name = 'administradores/editar_administrador.html'
    success_url = reverse_lazy('lista_administradores')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Editar Administrador'
        return context
