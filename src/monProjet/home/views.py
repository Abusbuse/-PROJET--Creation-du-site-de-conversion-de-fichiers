from django.shortcuts import render
from django.http import HttpResponse

# Fonction qui renvoie les pages html
def Accueil(request):
    return render (request, 'home/Accueil.html')

def convert(request):
    return render(request, 'home/convert.html')

def contact(request):
    return render(request, 'home/contact.html')

def aPropos(request):
    return render(request, 'home/aPropos.html')

def htp(request):
    return render(request, 'home/htp.html')

def dtp(request):
    return render(request, 'home/dtp.html')

def m4tm3(request):
    return render(request, 'home/m4tm3.html')

def mdToPdf(request):
    return render(request, 'home/mdToPdf.html')

def mdToHtml(request):
    return render(request, 'home/mdToHtml.html')

def dragAndDrop(request):
    return render(request, 'home/dragAndDrop.html')