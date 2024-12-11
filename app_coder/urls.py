from app_coder.views import *
from django.urls import path
# Es buena practica escribir todas las funciones 1x1, buena practica lo explicito
urlpatterns = [
    path('inicio/', index, name="Inicio"),
    path('cursos/', cursos, name ="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('alumnos/', alumnos, name="Alumnos"),
    path('entregables/', entregables, name="Entregas"),
    path('formulario/', formulario_curso, name="Formulario")
]