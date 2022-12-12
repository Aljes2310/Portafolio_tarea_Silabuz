from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('form/', views.get_name, name="get_name"),
    path('proyectos/', views.proyectos, name="proyectos"),
    path('delete/<int:id>', views.deleteproyect, name="delete"),
]

