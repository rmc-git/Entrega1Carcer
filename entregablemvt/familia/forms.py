from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    edad = forms.IntegerField(label="Edad")
    email = forms.EmailField(label="Email")

class MascotaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    edad = forms.IntegerField(label="Edad")
    tipo = forms.CharField(label="Tipo", max_length=50)