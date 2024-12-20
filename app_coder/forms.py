from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Vtuber, Profile

class post_vtuber(forms.ModelForm):
    class Meta:
        model = Vtuber
        fields = "__all__" 
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingresa el nombre del vtuber"}),
            "company": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ingresa la compañía"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribe una descripción", "rows": 3}),
            "foto": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name", "email"] 
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Apellido"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Correo electrónico"}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
