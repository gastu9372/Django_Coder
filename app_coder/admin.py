from django.contrib import admin
from .models import Curso, Alumnos, Profesores, Entregables

# Register your models here.

admin.site.register(Curso)
admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Entregables)