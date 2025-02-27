from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Mensaje
# Create your views here.


# Manejo de los manesajes

@login_required
def enviar_mensaje(request):
    
    usuarios = User.objects.exclude(username= request.user.username)
    if request.method == "POST":
        destinatario_username = request.POST.get("destinatario")
        contenido = request.POST.get("contenido")
        destinatario = User.objects.get(username=destinatario_username)
        Mensaje.objects.create(remitente = request.user, destinatario = destinatario, contenido = contenido)
        return redirect("mostrar-mensajes")
    
    return render(request, "app_mensajeria/enviar-mensaje.html", {"usuarios": usuarios})

@login_required
def mostrar_mensajes(request):
    
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by("-fecha_envio")
    
    return render(request, 'app_mensajeria/mostrar-mensajes.html', {"mensajes": mensajes})

@login_required
def mensajes_enviados(request):
    
    mensajes = Mensaje.objects.filter(remitente=request.user).order_by("-fecha_envio")
    
    return render(request, 'app_mensajeria/mensajes-enviados.html', {"mensajes": mensajes})

@login_required
def eliminar_mensajes(request, id):
    mensaje = Mensaje.objects.get(id=id)
    mensaje.delete()
    return redirect("mostrar-mensajes")

@login_required
def responder_mensaje(request, id):
    mensaje = Mensaje.objects.get(id=id)
    if request.method == "POST":
        contenido = request.POST.get("contenido")
        Mensaje.objects.create(remitente=request.user, destinatario=mensaje.remitente, contenido=contenido)
        return redirect('mostrar_mensajes')
    return render(request, "app_mensajeria/responder-mensaje.html", {"mensaje": mensaje})
