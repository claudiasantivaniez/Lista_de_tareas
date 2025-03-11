from django.db import models
from django.contrib.auth.models import User #importo usuario de django 

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion =models.TextField(blank=True, null=True)
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE) #relacion con el usuario de django 

    def __str__ (self) :
        return f"{self.titulo} {self.fecha_creacion} {self.fecha_vencimiento} {self.completada} {self.usuario}"
