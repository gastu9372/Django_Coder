from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensaje_enviado')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensaje_recibido')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensaje de {self.remitente} a {self.destinatario}"