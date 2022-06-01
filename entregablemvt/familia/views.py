import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Persona, Mascota 
from django.template import loader
from familia.forms import PersonaForm

# Create your views here.
def inicio(request):
   template = loader.get_template('familia/base.html')
   
   return HttpResponse(template.render())

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
            Persona(nombre=nombre, edad=edad, fecha_carga=email).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/template_carga_persona.html', {'form': form})

