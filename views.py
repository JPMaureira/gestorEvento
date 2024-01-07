from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Evento
from django.contrib.auth import login, authenticate
from django.template import Template, Context
from .models import UsuarioPersonalizado
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Listado.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('listado')  # Redirige a la vista listado
            else:
                return render(request, "inicio.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario erroneo"})

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# def login_request(request):

#     if request.method == 'POST':
#         form = AuthenticationForm(request, data = request.POST)

#         if form.is_valid():  # Si pasó la validación de Django

#             usuario = form.cleaned_data.get('username')
#             contrasenia = form.cleaned_data.get('password')

#             user = authenticate(username= usuario, password=contrasenia)

#             if user is not None:
#                 login(request, user)

#                 return render(request, "listado.html", {"mensaje":f"Bienvenido {usuario}"})
#             else:
#                 return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
           
#         else:

#             return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})

#     form = AuthenticationForm()

#     return render(request, "login.html", {"form": form})




@login_required  # Este decorador asegura que solo los usuarios autenticados puedan acceder a la vista
def listado(request):
    # Aquí puedes acceder al usuario autenticado usando 'request.user'
    usuario = request.user

    # Puedes pasar el objeto de usuario al contexto para usar en el template
    context = {"usuario": usuario}

    # Renderiza la plantilla 'listado.html' con el contexto proporcionado
    return render(request, "listado.html", context)


def user_logout(request):
    logout(request)
    return redirect('inicio.html')  # Reemplaza 'nombre_de_la_vista_de_inicio' con la URL de tu página de inicio

def inicio(request):
    mihtml = open('C:/Users/jmaur/OneDrive/Escritorio/Tercera pre-entregaMaureira/gestorEvento/gestorEvento/templates/inicio.html')
    inicio = Template(mihtml.read())
    mihtml.close()

    miContexto = Context()
    documento = inicio.render(miContexto)
    return HttpResponse(documento)


def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'detalle_evento.html', {'evento': evento})


def agregar_evento(request):
    if request.method == 'POST':
        # Procesar el formulario enviado
        # Aquí deberías manejar la lógica para agregar un nuevo evento
        # Puedes acceder a los datos del formulario usando request.POST
        # y luego crear una instancia del modelo Evento y guardarla en la base de datos
        # Después, podrías redirigir al usuario a la lista de eventos o a la página de detalle del nuevo evento
        pass
    else:
        # Mostrar el formulario para agregar un nuevo evento
        return render(request, 'agregar_evento.html')

    # Retorno adicional, por ejemplo, puedes redirigir al usuario a la lista de eventos después de procesar el formulario
    return HttpResponseRedirect('/lista_eventos/')  # Ajusta la URL según tus necesidades

# Puedes agregar más vistas según tus necesidades




