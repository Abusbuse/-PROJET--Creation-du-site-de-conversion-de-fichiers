from django.urls import path
from . import views
from . import htmlToPdf
from . import docxToPdf
from . import mp4ToMp3
from . import mdToPdf
from . import mdToHtml
from .views import contact

urlpatterns = [
    #Chemin vers la page d'accueil
    path('', views.Accueil, name='Accueil'),
    
    #Chemin vers la page de centralisation des conversions
    path('convert/', views.convert, name='convert'),
    
    #Cehmin vers les autres pages
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('aPropos/', views.aPropos, name='aPropos'),

    
    #Chemin vers les pages de conversion 
    path('htp/', views.htp, name='htp'),
    path('dtp/', views.dtp, name='dtp'),
    path('m4tm3/', views.m4tm3, name='m4tm3'),
    path('mdToPdf/', views.mdToPdf, name='mdToPdf'),
    path('mdToHtml/', views.mdToHtml, name='mdToHtml'),
    path('dragAndDrop/', views.dragAndDrop, name='dragAndDrop'),
    
    #Chemin vers les fonctions de conversion
    path('convertFileHtmlToPdf/', htmlToPdf.convertFileHtmlToPdf),
    path('convertFileDocxToPdf/', docxToPdf.convertFileDocxToPdf),
    path('convertMp4ToMp3/', mp4ToMp3.convertMp4ToMp3),
    path('convertFileMdToPdf/', mdToPdf.convertFileMdToPdf),
    path('convertFileMdToHtml/', mdToHtml.convertFileMdToHtml),
]