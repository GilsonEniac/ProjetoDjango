from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse('HOME 03')

def sobre(request):
    return HttpResponse('SOBRE')

def contato(request):
    return HttpResponse('CONTATO')




# Create your views here.
