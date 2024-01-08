"""
URL configuration for gestorEvento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import inicio, agregar_evento, login_request, register,listado, agregar_evento,evento_agregado,eliminar_evento, editar_evento

from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('inicio/',inicio),
    path('', inicio),  
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('listado/', listado, name='listado'),
    path('agregar_evento/', agregar_evento, name='agregar_evento'),
    path('evento_agregado/', evento_agregado, name='evento_agregado'),
    path('eliminar_evento/<int:evento_id>/', eliminar_evento, name='eliminar_evento'),
    path('editar_evento/<int:evento_id>/', editar_evento, name='editar_evento'),


   
]



