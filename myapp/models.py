from django.db import models

# Create your models here.
class Project(models.Model):
  # Especificamos los atributos del modelo
  name = models.CharField(max_length=200)

class Task(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField() #Textos extensos
  # Creamos un foreignkey de PROJECT
  project = models.ForeignKey(Project, on_delete=models.CASCADE)