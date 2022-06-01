from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    edad = forms.IntegerField(label="Edad")
    email = forms.EmailField(label="Email")
    