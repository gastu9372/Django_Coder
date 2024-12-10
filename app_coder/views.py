from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido a la pagina")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def alumnos(request):
    return HttpResponse("vista alumnos")

def entregables(request):
    return HttpResponse("Vista entregables")