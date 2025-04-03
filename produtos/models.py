from django.db import models

# Create your models here.

class Tamnho (models.Model):
    size = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.size

class Terno (models.Model):
    titulo = models.CharField(max_length=20,verbose_name= 'Titulo')
    descricao= models.TextField(max_length=100,verbose_name = 'Texto')
    tamanho= models.ManyToManyField(Tamnho,related_name='produtos')
    img = models.ImageField(upload_to='produtos/',verbose_name='Imagem 1')

class Infantil( models.Model):
    titulo = models.CharField(max_length=20,verbose_name= 'Titulo')
    descricao= models.TextField(max_length=100,verbose_name = 'Texto')
    img = models.ImageField(upload_to='produtos/infantil',verbose_name='Imagem 1')


