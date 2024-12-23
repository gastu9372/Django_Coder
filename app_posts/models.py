from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts' )
    titulo = models.CharField(max_length=30)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    foto = models.ImageField(upload_to='posts/', null=True, blank=True)
    editado = models.BooleanField(default=False)

    def __str__(self):
        return f"Titulo: {self.titulo}"
    
class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentario')
    contenido = models.TextField()
    foto = models.ImageField(upload_to='posts/', null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    editado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"autor: {self.autor}"