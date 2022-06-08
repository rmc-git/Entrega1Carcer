import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Persona, Mascota, Hobbies 
from django.template import loader
from familia.forms import PersonaForm, MascotaForm, BuscarPersonasForm, BuscarMascotasForm

# Create your views here.
def inicio2(request):
    personas = Persona.objects.all()
    mascotas = Mascota.objects.all()
    hobbies = Hobbies.objects.all()
    context = {"app1": "Familiares", "personas": personas, "app2": "Mascotas", "mascotas": mascotas, "app3": "Hobbies", "hobbies": hobbies }
    return render(request, 'familia/inicio2.html', context)
    
def verfamilia(request):
    personas = Persona.objects.all()
    context = {"app": "Familiares", "personas": personas}
    return render(request, 'familia/template_familia.html', context)

def vermascota(request):
    mascotas = Mascota.objects.all()
    context = {"app": "Mascotas", "mascotas": mascotas}
    return render(request, 'familia/template_mascota.html', context)

def verhobbies(request):
    hobbies = Hobbies.objects.all()
    context = {"app": "Hobbies", "hobbies": hobbies}
    return render(request, 'familia/template_hobbies.html', context)

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
            Mascota(nombre=nombre, edad=edad, tipo=tipo).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/template_carga_mascota.html', {'form': form})

def buscar_persona(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarPersonasForm(request.GET)
        if form_busqueda.is_valid():
            personas = Persona.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'familia/template_familia.html', {"personas": personas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/template_buscar_persona.html', {"template_buscar_persona": form_busqueda})

def buscar_mascota(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarMascotasForm(request.GET)
        if form_busqueda.is_valid():
            mascotas = Mascota.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'familia/template_mascota.html', {"mascotas": mascotas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarMascotasForm()
        return render(request, 'familia/template_buscar_mascota.html', {"template_buscar_mascota": form_busqueda})
