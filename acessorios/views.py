from django.shortcuts import render
from acessorios.models import Acessorios

# Create your views here.

def acessorios_view(request):
    acessorios = Acessorios.objects.all()
    return render(
        request,
        'Acessorio.html',
        {'acessorio' : acessorios}
    )