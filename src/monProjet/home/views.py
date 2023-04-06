from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse

# Fonction qui renvoie les pages html
def Accueil(request):
    return render (request, 'home/Accueil.html')

def convert(request):
    return render(request, 'home/convert.html')

def contact(request):
    return render(request, 'home/contact.html')
 
def contact_success(request):
    return render(request, 'home/contact_success.html')

def aPropos(request):
    return render(request, 'home/aPropos.html')

def test(request):
    return render(request, 'home/test.html')

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

def pngToJpg(request):
    return render(request, 'home/pngToJpg.html')

def jpgToPng(request):
    return render(request, 'home/jpgToPng.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            f'Nouveau message de {name}',
            f'{message}\n\n{email}',
            email,
            ['gwittmann16@gmail.com'],
            fail_silently=False,
        )
        return redirect(reverse('contact_success'))

    return render(request, 'home/contact.html')