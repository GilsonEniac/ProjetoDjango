from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,'global/Home.html')
    
def sobre(request):
    return HttpResponse('SOBRE 03')

def contato(request):
    return HttpResponse('CONTATO 03')




# Create your views here.
