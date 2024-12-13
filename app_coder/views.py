from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q

from .forms import post_vtuber
from .models import Vtuber


# Create your views here.
def index(request):
    return render(request, "app_coder/index.html")

def vtubers(request):
    vtubers = Vtuber.objects.all()
    query = request.GET.get('q')
    if query:
        vtubers = Vtuber.objects.filter(nombre__icontains=query) | Vtuber.objects.filter(company__icontains=query)
    else:
        vtubers = Vtuber.objects.all()
        
    return render(request, "app_coder/vtubers.html", {"vtubers":vtubers})

def mods(request):
    return render(request, "app_coder/mods.html")

def users(request):
    return render(request, "app_coder/users.html")

def posts(request):
    return render(request, "app_coder/posts.html")

def formulario_vtuber_api(request):
    
    if request.method == "POST":
        post_vtuber_form = post_vtuber(request.POST, request.FILES)
        if post_vtuber_form.is_valid():
            #informacion_limpia = post_vtuber_form.cleaned_data
            #vtuber = Vtuber(nombre=informacion_limpia["nombre"], company=informacion_limpia["company"], descripcion=informacion_limpia["descripcion"], foto=informacion_limpia["foto"])
            post_vtuber_form.save()
            return redirect("Vtubers")
    else:
        post_vtuber_form = post_vtuber()
        
    
    contexto= {"post_vtuber": post_vtuber_form}
    return render(request, "app_coder/forms/formulario.html", contexto)

def eliminar_vtuber(request, id):
    vtuber = Vtuber.objects.get(id=id)
    vtuber.delete()
    return redirect("Vtubers")

def editar_vtuber(request, id):
    vtuber = Vtuber.objects.get(id=id)
    post_vtuber_form = post_vtuber(initial= {"nombre": vtuber.nombre,"company": vtuber.company, "descripcion": vtuber.descripcion, "foto": vtuber.foto})
    return render(request,"app_coder/vtubers.html", {"post_vtuber": post_vtuber_form})