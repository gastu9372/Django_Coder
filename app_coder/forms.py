from django import forms
from .models import Vtuber

class post_vtuber(forms.ModelForm):
    class Meta:
        model = Vtuber
        fields = ['nombre', 'company', 'descripcion', 'foto']