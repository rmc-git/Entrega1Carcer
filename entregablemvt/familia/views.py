import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Persona, Mascota 
from django.template import loader
from familia.forms import PersonaForm, MascotaForm

# Create your views here.
def inicio(request):
    personas = Persona.objects.all()
    mascotas = Mascota.objects.all()
    context = {"app1": "Familiares", "personas": personas, "app2": "Mascotas", "mascotas": mascotas, }
    return render(request, 'familia/inicio.html', context)
    
def verfamilia(request):
    personas = Persona.objects.all()
    context = {"app": "Familiares", "personas": personas}
    return render(request, 'familia/template_familia.html', context)

def vermascota(request):
    mascotas = Mascota.objects.all()
    context = {"app": "Mascotas", "mascotas": mascotas}
    return render(request, 'familia/template_mascota.html', context)

def cargar_persona(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            email = form.cleaned_data['email']
            Persona(nombre=nombre, edad=edad, email=email).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/template_carga_persona.html', {'form': form})

def cargar_mascota(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            tipo = form.cleaned_data['tipo']
            Persona(nombre=nombre, edad=edad, tipo=tipo).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/template_carga_mascota.html', {'form': form})

