from django.shortcuts import render

def administradores(request):
    administradores = [
        {'nombre': 'Carlos', 'apellido': 'Ramírez'},
        {'nombre': 'Laura', 'apellido': 'Martínez'},
    ]
    return render(request, 'home/administradores.html', {'administradores': administradores})

# Create your views here.
