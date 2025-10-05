from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def administradores(request):
    from Apps.administradores.models import Administrador
    administradores = Administrador.objects.all()
    return render(request, 'home/administradores.html', {'administradores': administradores})