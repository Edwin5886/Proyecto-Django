from django.shortcuts import render

def estudiantes(request):
    estudiantes = [
        {'nombre': 'Juan', 'apellido': 'Pérez'},
        {'nombre': 'Ana', 'apellido': 'García'},
    ]
    return render(request, 'home/estudiantes.html', {'estudiantes': estudiantes})
