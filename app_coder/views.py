from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import post_vtuber
from .models import Vtuber


# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Inicio")
        else:
            return render(request, "app_coder/forms/login.html")
    else:
        return render(request, "app_coder/forms/login.html")

def user_logout(request):
    logout(request)
    return redirect("Inicio")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("Inicio")
    else:
        form = UserCreationForm()
    return render(request, "app_coder/forms/register.html", {"form": form})

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

@login_required
def mods(request):
    return render(request, "app_coder/mods.html")

@login_required
def users(request):
    return render(request, "app_coder/users.html")

@login_required
def posts(request):
    return render(request, "app_coder/posts.html")

@login_required
def formulario_vtuber_api(request):
    
    if request.method == "POST":
        post_vtuber_form = post_vtuber(request.POST, request.FILES)
        if post_vtuber_form.is_valid():
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