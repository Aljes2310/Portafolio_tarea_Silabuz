from django.db import models

# Create your models here.
class Formulario(models.Model):
    Foto=models.CharField(max_length=200, default="")
    Titulo=models.CharField(max_length=100, default="")
    descripcion=models.CharField(max_length=100, default="")
    tags=models.CharField(max_length=100, default="")
    url=models.CharField(max_length=100, default="")
