"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Es buena practica escribir todas las funciones 1x1, buena practica lo explicito
from app_coder.views import index, cursos, profesores, alumnos, entregables

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', index),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('alumnos/', alumnos),
    path('entregables/', entregables),
]
