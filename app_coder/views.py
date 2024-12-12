from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Vtuber

# Create your views here.
def index(request):
    return render(request, "app_coder/index.html")

def vtubers(request):
    return render(request, "app_coder/vtubers.html")

def mods(request):
    return render(request, "app_coder/mods.html")

def users(request):
    return render(request, "app_coder/users.html")

def posts(request):
    return render(request, "app_coder/posts.html")

# def formulario_curso(request):
#     if request.method == "POST":
#         curso = Curso(nombre=request.POST["curso"], comision=request.POST["comision"])
#         print(curso)
#         curso.save()
#         return redirect(cursos)
#     else:
#         return render(request, "app_coder/forms/formulario.html")

def formulario_curso_api(request):
    return render(request, "app_coder/forms/formulario.html")