from django.shortcuts import render, redirect
from .models import Administrador
from .forms import AdministradorForm


def administradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'home/administradores.html', {'administradores': administradores})

def crear_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_administradores')
    else:
        form = AdministradorForm()
    return render(request, 'administradores/crear_administrador.html', {'form': form})
