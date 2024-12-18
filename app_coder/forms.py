from django import forms
from .models import Vtuber

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