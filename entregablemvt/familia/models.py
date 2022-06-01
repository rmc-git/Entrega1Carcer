from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.CharField(max_length=100, default='')

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo = models.CharField(max_length=50)
    
