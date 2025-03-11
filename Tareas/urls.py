from django.urls import path
from Tareas.views import TareasTemplateView

urlpatterns = [
    path('', TareasTemplateView.as_view()), 
]