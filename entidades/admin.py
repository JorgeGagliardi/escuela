from django.contrib import admin
from .models import *
from django.utils.html import format_html


class EstudiantesAdmin(admin.ModelAdmin):
	list_display = ("apellido","nombre","email")
	list_filter = ("nombre",)

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiantes,EstudiantesAdmin)
admin.site.register(TrabajosPracticos)
