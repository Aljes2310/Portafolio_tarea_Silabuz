from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Formulario
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Formulario.objects.create(**form.cleaned_data)
            return render(request, "thanks.html")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()

    return render(request, 'crear_proyecto.html', {'form': form})



def proyectos(request):
    lista=Formulario.objects.all()
    return render(request, "lista.html", {'lista' :lista})

@login_required
def deleteproyect(request, id):
    proyectos = Formulario.objects.get(id=id)
    proyectos.delete()
    return redirect("proyectos")


