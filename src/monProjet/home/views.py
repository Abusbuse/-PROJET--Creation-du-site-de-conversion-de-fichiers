from django.shortcuts import render
from django.http import HttpResponse

# Fonction qui renvoie les pages html
def Accueil(request):
    return render (request, 'home/Accueil.html')

def htp(request):
    return render(request, 'home/htp.html')

def dtp(request):
    return render(request, 'home/dtp.html')

def m4tm3(request):
    return render(request, 'home/m4tm3.html')