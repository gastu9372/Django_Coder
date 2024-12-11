from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - comision: {self.comision}"

class Alumnos(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Alumno: {self.nombre} {self.apellido}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido} - Profesion: {self.profesion}"

class Entregables (models.Model):
    nombre =models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self):
        return f"Entrega: {self.nombre} / {self.fecha_de_entrega} / {self.entregado}"