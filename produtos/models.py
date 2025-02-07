from django.db import models

# Create your models here.

class Terno (models.Model):
    descricao: models.CharField(max_length=60,verbose_name = 'Texto')
    img = models.ImageField(upload_to='produtos',verbose_name='Imagem 1')