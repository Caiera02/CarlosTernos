from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from produtos.models import Sapato, Terno
from geminiAi.client import get_descricao, get_descricao_ternos

@receiver(pre_save, sender=Sapato)
def sapato_pre_save(sender,instance, **kwargs):
    if not instance.descricao:
        ai_descricao = get_descricao(
            instance.titulo, instance.cor 
        )
        instance.descricao = ai_descricao 
        
@receiver(pre_save, sender=Terno)
def terno_pre_save(sender,instance, **kwargs):
    if not instance.descricao:
        ai_descricao = get_descricao_ternos(
            instance.titulo
        )
        instance.descricao = ai_descricao 