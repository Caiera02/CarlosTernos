from django.shortcuts import render
from produtos.models import Terno, Sapato

# Create your views here.

def terno_view(request):
    ternos = Terno.objects.all()
    return render(
        request,
        'Adulto.html',
        {'terno': ternos}
        )

def home_view (request):
    return render(
        request,
        'Home.html'
    )

def sapato_view(request):
    sapatos = Sapato.objects.all()
    return render(
        request,
        'Sapato.html',
        {'sapato': sapatos}
    )