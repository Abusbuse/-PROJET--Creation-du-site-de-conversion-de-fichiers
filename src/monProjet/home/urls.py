from django.urls import path
from . import views
from . import test


urlpatterns = [
    path('', views.index, name='index'),
    path('convertFileHtmlToPdf/', test.convertFileHtmlToPdf),
]