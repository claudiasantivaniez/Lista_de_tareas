from django.contrib import admin

# Register your models here.

from Tareas.models import Tarea #importo el modelo tarea

#admin.site.register(Tarea) #registro el modelo en el administrador predeterminado de django 

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_creacion', 'fecha_vencimiento','completada', 'usuario') #vista de lista del objeto tarea en el admin, configura las columnas que se mostraran 
    search_fields= ('completada','fecha_creacion','fecha_vencimiento','usuario')
    list_filter=('completada', 'usuario')
    fields=('titulo', 'descripcion', 'fecha_vencimiento', 'usuario') #si esta linea (fields=) que indica los campos a completar en cada formulario para el registro en el admin no se encuentra, django pondra por defecto todos los campos del modelo 

    # Agrega dentro de la clase la acción personalizada

    actions = ['marcar_como_completada']  

    def marcar_como_completada(self, request, queryset):
        queryset.update(completada=True)  # Marca las tareas seleccionadas como completadas
        self.message_user(request, "Tareas marcadas como completadas.")

    marcar_como_completada.short_description = "Marcar tareas como completadas"