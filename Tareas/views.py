from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

class TareasTemplateView (TemplateView): #esta funcion es una vista
    template_name = 'tareas.html'
