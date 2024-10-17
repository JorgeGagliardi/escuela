from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    grupo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Estudiantes"
        verbose_name_plural = "Estudiantes"
        ordering = ["-nombre","apellido"]

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

class TrabajosPracticos(models.Model):
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Trabajos Prácticos"
        verbose_name_plural = "Trabajos Prácticos"
