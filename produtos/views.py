from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from produtos.models import Terno, Sapato, Camisa
from django.views.generic import DetailView, DeleteView

def terno_view(request):
    ternos = Terno.objects.all()
    return render(request,'Adulto.html',{'terno': ternos})

class TernoDetailview(DetailView):
    model=Terno
    template_name = 'teste.html'
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class TernoDeleteView(DeleteView):
    model = Terno
    template_name = 'car_delete.html'
    success_url = '/terno/'

def home_view(request):
    return render(request,'Home.html')


def sapato_view(request):
    sapatos = Sapato.objects.all().order_by('tamanho')
    buscar = request.GET.get('search')

    if buscar:
        sapatos = sapatos.filter(tamanho__icontains=buscar)

    return render(request,'Sapato.html',{'sapato': sapatos})

def camisa_view(request):
    camisas = Camisa.objects.all()
    return render(request,'Camisa.html',{'camisa' : camisas})