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
from .views import inicio, agregar_evento,signup, signin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('inicio/',inicio),
    path('', inicio),  # Esta línea cambia para que la raíz apunte a la vista de inicio
    path('signup/', signup),  # Agrega name='signup'
    path('signin/', signin),  # Agrega name='signin'
    # path('lista_eventos/', lista_eventos),
    # path('detalle_evento/<int:evento_id>/', detalle_evento),
    path('agregar_evento/', agregar_evento),
    # Puedes agregar más patrones de URL según tus necesidades
]



