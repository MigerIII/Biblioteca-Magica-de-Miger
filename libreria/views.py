from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Bienvenidos a la libreria mágica de Míger!!!</h1>")
def nosotros(request):
    return render(request,'paginas/nosotros.html')