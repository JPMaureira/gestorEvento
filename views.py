from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Evento
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm
from django.template import Template, Context
from .models import UsuarioPersonalizado



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listado')
    else:
        form = SignUpForm()

    template_path = 'gestorEvento/plantillas/signup.html'
    template = Template(open(template_path).read())
    context = Context({'form': form})

    return HttpResponse(template.render(context))


def signin(request):
    mihtml = open('C:/Users/jmaur/OneDrive/Escritorio/Tercera pre-entregaMaureira/gestorEvento/gestorEvento/plantillas/signin.html')
    inicio = Template(mihtml.read())
    mihtml.close()

    miContexto = Context()
    documento = inicio.render(miContexto)
    return HttpResponse(documento)

def listado(request):
    mihtml = open('C:/Users/jmaur/OneDrive/Escritorio/Tercera pre-entregaMaureira/gestorEvento/gestorEvento/plantillas/listado.html')
    inicio = Template(mihtml.read())
    mihtml.close()

    miContexto = Context()
    documento = inicio.render(miContexto)
    return HttpResponse(documento)

def inicio(request):
    mihtml = open('C:/Users/jmaur/OneDrive/Escritorio/Tercera pre-entregaMaureira/gestorEvento/gestorEvento/plantillas/inicio.html')
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




