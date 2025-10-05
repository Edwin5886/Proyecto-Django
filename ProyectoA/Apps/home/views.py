from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def administradores(request):
    administradores = [
        {'nombre': 'Carlos', 'apellido': 'Ramírez'},
        {'nombre': 'Laura', 'apellido': 'Martínez'},
    ]
    return render(request, 'home/administradores.html', {'administradores': administradores})