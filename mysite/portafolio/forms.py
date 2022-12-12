from django import forms
from .models import Formulario

""" class NameForm(forms.Form):

    Foto= forms.CharField(label= "Foto (url) ", max_length=200 , widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))

    Titulo=forms.CharField(label= "Titulo del Proyecto", max_length=200 , widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
    descripcion=forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
    tags=forms.CharField(max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  }))
    url=forms.CharField(label='Url de tu github',max_length=200, widget=forms.TextInput(attrs={
    "class": "form-control mb-3"
  })) """

class MyForm(forms.ModelForm):
  class Meta:
    model = Formulario
    fields = ["Foto", "Titulo", "descripcion", "tags", "url"]
    labels = {'Foto': "Foto (url)", "Titulo": "Titulo del Proyecto", 'descripcion': "Descripcion", "tags": "Tags",
    'url': "Url de tu github"}