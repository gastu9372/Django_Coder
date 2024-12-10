from app_coder.views import *
from django.urls import path
# Es buena practica escribir todas las funciones 1x1, buena practica lo explicito
urlpatterns = [
    path('inicio/', index),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('alumnos/', alumnos),
    path('entregables/', entregables),
]