from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def habitacion(request):
    return render(request,'habitacion.html')

def usuario(request):
    return render(request,'usuario.html')