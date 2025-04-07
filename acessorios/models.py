from django.db import models

# Create your models here.

class Acessorios(models.Model):
    nome= models.CharField(max_length=20)
    descricao=models.CharField(max_length=50)
    cor = models.CharField(max_length=10)
    