from django.conf import settings
from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    Nombre = models.CharField(max_length=60)
    id = models.BigAutoField(primary_key=True)

class Asignatura(models.Model):
     Nombre = models.CharField(max_length=128)
     id = models.BigAutoField(primary_key=True)

class Asignatura_alumno(models.Model):
     id = models.BigAutoField(primary_key=True)
     id_alumno= models.ForeignKey(Alumno, on_delete=models.CASCADE)
     id_asignatura=models.ForeignKey(Asignatura, on_delete=models.CASCADE)

