# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CrearUsuarioForm


def lista_usuarios(request):
    """Vista para mostrar la lista de todos los usuarios"""
    usuarios = User.objects.all().order_by('username')
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


def crear_usuario(request):
    """Vista para crear un nuevo usuario"""
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('lista_usuarios')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = CrearUsuarioForm()
    
    return render(request, 'usuarios/crear_usuario.html', {
        'form': form,
        'titulo_pagina': 'Crear Nuevo Usuario'
    })