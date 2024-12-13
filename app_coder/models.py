from django.db import models

# Create your models here.
class Vtuber(models.Model):
    nombre = models.CharField(max_length=40)
    company = models.CharField(max_length=30)
    descripcion = models.CharField(max_length= 100)
    foto = models.ImageField(upload_to='vtubers_photos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - Compañia: {self.company} - Descripcion: {self.descripcion}"

class User(models.Model):
    nombre = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Username: {self.nombre} #{self.apellido}"

class Moderator(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido} - Profesion: {self.profesion}"

class Post(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    foto = models.ImageField(upload_to='posts/', null=True, blank=True)
    # La foto es algo a implementar todavia
    def __str__(self):
        return f"Entrega: {self.nombre} / {self.fecha_de_entrega} / {self.entregado}"