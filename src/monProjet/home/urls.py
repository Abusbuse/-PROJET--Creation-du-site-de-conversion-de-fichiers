from django.urls import path
from . import views
from . import htmlToPdf


urlpatterns = [
    path('', views.index, name='index'),
    path('convertFileHtmlToPdf/', htmlToPdf.convertFileHtmlToPdf),
]