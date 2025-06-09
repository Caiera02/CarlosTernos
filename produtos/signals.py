from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from produtos.models import Sapato

@receiver(pre_save, sender=Sapato)
def sapato_pre_save(sender,instance, **kwargs):
    if not instance.descricao:
        ai_descricao = gerar_descricao(
            instance.titulo, instance.cor 
        )
        instance.descricao = ai_descricao 