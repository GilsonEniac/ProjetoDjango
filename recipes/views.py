from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,'recipes/Home.html',context={'name': 'Gilson Gomes','nome':'Cassia Volpati'})
    
def contato(request):
    return render(request,'temp/temp.html')

def sobre(request):
    return render(request,'recipes/sobre.html')

def info(request):
    return render(request,'recipes/info.html')

def detalhe(request):
    return render(request,'recipes/detalhe.html')

# Create your views here.
