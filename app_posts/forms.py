from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'foto']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu post aquí...', 'rows': 5}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido', 'foto']
        widgets = {
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }