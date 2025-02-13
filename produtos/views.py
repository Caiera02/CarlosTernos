from django.shortcuts import render
from produtos.models import Terno

# Create your views here.

def terno_view(request):
    ternos = Terno.objects.all()
    print(ternos)

    return render(
        request,
        # 'control.html',
        'Adulto.html',
        {'terno': ternos}
        )

def home_view (request):

    return render(
        request,
        'Home.html'
    )