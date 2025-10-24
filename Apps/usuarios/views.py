# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CrearUsuarioForm


@login_required(login_url='/usuarios/login/')
def lista_usuarios(request):
    """Vista para mostrar la lista de todos los usuarios"""
    usuarios = User.objects.all().order_by('username')
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})


@login_required(login_url='/usuarios/login/')
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


def login_view(request):
    """Vista para el login de usuarios"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user.first_name or user.username}!')
                # Redirigir al home después del login
                return redirect('/home/')
            else:
                messages.error(request, 'Contraseña o usuario incorrecto.')
        else:
            messages.error(request, 'Contraseña o usuario incorrecto.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {
        'form': form,
        'titulo_pagina': 'Iniciar Sesión'
    })


def logout_view(request):
    """Vista para cerrar sesión"""
    # Limpiar todos los mensajes anteriores antes del logout
    storage = messages.get_messages(request)
    storage.used = True  # Marca todos los mensajes como utilizados
    
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')


# Función dashboard removida - ahora redirige directamente a lista de estudiantes