from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Categoria, Lugar, Participante, Evento,User

admin.site.register(User)
admin.site.register(Categoria)
admin.site.register(Lugar)
admin.site.register(Participante)
admin.site.register(Evento)


AUTH_USER_MODEL = 'gestorEvento.UsuarioPersonalizado'


