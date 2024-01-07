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

from django.shortcuts import render
from .forms import UserRegisterForm

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"listado.html" ,  {"form":form})





def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "listado.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "listado.html", {"form": form})




def listado(request):
    mihtml = open('C:/Users/jmaur/OneDrive/Escritorio/Tercera pre-entregaMaureira/gestorEvento/gestorEvento/templates/listado.html')
    inicio = Template(mihtml.read())
    mihtml.close()

    miContexto = Context()
    documento = inicio.render(miContexto)
    return HttpResponse(documento)

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




