from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app_coder/index.html")

def cursos(request):
    return render(request, "app_coder/cursos.html")

def profesores(request):
    return render(request, "app_coder/profesores.html")

def alumnos(request):
    return render(request, "app_coder/alumnos.html")

def entregables(request):
    return render(request, "app_coder/entregables.html")

def formulario_curso(request):
    if request.method == "POST":
        curso = Curso(nombre=request.POST["curso"], comision=request.POST["comision"])
        print(curso)
        curso.save()
        return redirect("cursos")
    else:
        return render(request, "app_coder/forms/curso-formulario.html")