from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import Q

from django.contrib import messages

from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from django.shortcuts import get_object_or_404


from .forms import post_vtuber, UserUpdateForm, UserProfileForm
from .models import Vtuber, Profile


# Create your views here.

@login_required
def show_profile(request):
    return render(request, "app_coder/show-profile.html")

@login_required
def edit_profile(request):
    user = request.user
    
    profile, _ = Profile.objects.get_or_create(user=user)
    
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Perfil editado con exito")
            return redirect("Perfil")
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UserProfileForm(instance=profile)  
    
    return render(request, "app_coder/forms/edit-profile.html", {"user_form": user_form, "profile_form": profile_form})

@login_required
def change_password(request):
    user = request.user
    if request.method == "POST":
        form_password = PasswordChangeForm(user)
        if form_password.is_valid():
            form_password.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Contraseña cambiada con exito")
            return redirect("Perfil")
        else:
            messages.error(request, "Error al cambiar la contraseña. Revisa los campos.")
    else:
        form_password = PasswordChangeForm(user)
        
    return render(request, "app_coder/forms/change-password.html", {"form_password": form_password})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get('next') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = next_url or 'Inicio'  
            return redirect(next_url)
        else:
            return render(request, "app_coder/forms/login.html", {
                "error": "Usuario o contraseña incorrectos",
                "next": next_url
            })
    else:
        next_url = request.GET.get('next', '')
        return render(request, "app_coder/forms/login.html", {"next": next_url})


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
def users(request):
    usuarios = User.objects.select_related('profile').all
    return render(request, "app_coder/users.html", {"usuarios":usuarios})

@login_required
def posts(request):
    return render(request, "app_coder/posts.html")

@login_required
def formulario_vtuber_api(request):
    if not request.user.is_staff:
        return redirect("Inicio")
    
    if request.method == "POST":
        post_vtuber_form = post_vtuber(request.POST, request.FILES)
        if post_vtuber_form.is_valid():
            post_vtuber_form.save()
            return redirect("Vtubers")
    else:
        post_vtuber_form = post_vtuber()
        
    contexto= {"post_vtuber": post_vtuber_form}
    return render(request, "app_coder/forms/formulario.html", contexto)

@login_required
def eliminar_vtuber(request, id):
    if not request.user.is_staff:
        return redirect("Inicio")
    vtuber = Vtuber.objects.get(id=id)
    vtuber.delete()
    return redirect("Vtubers")

@login_required
def editar_vtuber(request, pk):
    vtuber = get_object_or_404(Vtuber, pk = pk)
    if not request.user.is_staff:
        return redirect("Inicio")
    if request.method == "POST":
        post_vtuber_form = post_vtuber(request.POST, request.FILES, instance=vtuber)
        if post_vtuber_form.is_valid():
            post_vtuber_form.save()
            return redirect("Vtubers")
    else:
        post_vtuber_form = post_vtuber(instance=vtuber)
    
    return render(request,"app_coder/forms/edit_vtuber.html", {"post_vtuber": post_vtuber_form})




def about_me(request):
    return render(request, "app_coder/about-me.html")