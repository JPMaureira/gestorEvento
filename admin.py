from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Categoria, Lugar, Participante, UsuarioPersonalizado, Evento


class UsuarioPersonalizadoAdmin(UserAdmin):
    model = UsuarioPersonalizado
    

admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)
admin.site.register(Categoria)
admin.site.register(Lugar)
admin.site.register(Participante)
admin.site.register(Evento)


AUTH_USER_MODEL = 'gestorEvento.UsuarioPersonalizado'


