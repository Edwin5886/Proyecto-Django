from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='/usuarios/login/')
def index(request):
    return render(request, 'home/index.html')

@login_required(login_url='/usuarios/login/')
def about(request):
    return render(request, 'home/about.html')

@login_required(login_url='/usuarios/login/')
def administradores(request):
    from Apps.administradores.models import Administrador
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