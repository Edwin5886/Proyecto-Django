from django.db import models

# Create your models here.
from django.db import models

class EstudiantePublicador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class EstudianteAutorizador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    publicador = models.ForeignKey(EstudiantePublicador, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(EstudianteAutorizador, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo