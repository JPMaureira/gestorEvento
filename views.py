from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Evento
from django.contrib.auth import login, authenticate
from django.template import Template, Context
from .models import UsuarioPersonalizado
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render, redirect
from .forms import UserRegisterForm

from django.contrib.auth.decorators import login_required

from .models import Evento, Categoria, Lugar
from .forms import TuFormularioDeEvento  

from django.contrib import messages


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






@login_required  # Este decorador asegura que solo los usuarios autenticados puedan acceder a la vista
def listado(request):
   
    usuario = request.user
    context = {"usuario": usuario}
    return render(request, "listado.html", context)


def user_logout(request):
    logout(request)
    return redirect('inicio.html')

def inicio(request):
    return render(request, 'inicio.html')


def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'detalle_evento.html', {'evento': evento})





def agregar_evento(request):
    if request.method == 'POST':
        form = TuFormularioDeEvento(request.POST)

        if form.is_valid():
            evento = form.save()
            messages.success(request, 'Evento agregado exitosamente.')
            return redirect('evento_agregado')

    else:
        form = TuFormularioDeEvento()

    return render(request, 'agregar_evento.html', {'form': form})


# def evento_agregado(request):
#     # Obtén los mensajes de la sesión
#     messages_to_show = request.session.get('messages_to_show', [])
#     # Limpia los mensajes en la sesión para evitar duplicados
#     request.session['messages_to_show'] = []
    
#     eventos = Evento.objects.all()
#     return render(request, 'evento_agregado.html', {'eventos': eventos, 'messages_to_show': messages_to_show})

from .forms import BuscarEventoForm

def evento_agregado(request):
    messages_to_show = request.session.get('messages_to_show', [])
    request.session['messages_to_show'] = []

    eventos = Evento.objects.all()
    
    # Procesar la búsqueda si se envió un formulario de búsqueda
    form_buscar = BuscarEventoForm(request.GET)
    if form_buscar.is_valid():
        busqueda = form_buscar.cleaned_data['busqueda']
        eventos = eventos.filter(Q(nombre__icontains=busqueda) | Q(lugar__icontains=busqueda))


    return render(request, 'evento_agregado.html', {'eventos': eventos, 'messages_to_show': messages_to_show, 'form_buscar': form_buscar})

def eliminar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    evento.delete()
    messages.success(request, 'Evento eliminado exitosamente.')
    return redirect('evento_agregado')

def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    if request.method == 'POST':
        form = TuFormularioDeEvento(request.POST, instance=evento)

        if form.is_valid():
            form.save()
            messages.success(request, 'Evento editado exitosamente.')
            return redirect('evento_agregado')
    else:
        form = TuFormularioDeEvento(instance=evento)

    return render(request, 'editar_evento.html', {'form': form, 'evento_id': evento_id})