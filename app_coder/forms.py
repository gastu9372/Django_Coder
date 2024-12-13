from django import forms

class post_vtuber(forms.Form):
    nombre = forms.CharField( max_length= 40, required=False)
    company = forms.CharField(max_length=30)
    descripcion = forms.CharField( max_length=100, required=False)