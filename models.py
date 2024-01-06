from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Agrega cualquier campo adicional que necesites
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=25)

    # Añade un related_name personalizado para evitar conflictos con auth.User
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    hora = models.TimeField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    participantes = models.ManyToManyField('Participante', blank=True)

    def __str__(self):
        return self.nombre

class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
