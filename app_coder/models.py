from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vtuber(models.Model):
    nombre = models.CharField(max_length=40)
    company = models.CharField(max_length=30)
    descripcion = models.CharField(max_length= 100)
    foto = models.ImageField(upload_to='vtubers_photos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - Compañia: {self.company} - Descripcion: {self.descripcion}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_picture/", null = True, blank= True)