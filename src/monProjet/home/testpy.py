from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
import os

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        # afficher le nom du fichier
        print(file.name)
        # afficher la taille du fichier
        print(file.size)
        #afficher le chemin du fichier
        print(os.path.dirname(os.path.abspath(__file__)))
        
        # Renvoyer une réponse JSON indiquant que le fichier a été traité avec succès
        response_data = {'success': True}
        return JsonResponse(response_data)
    else:
        return render(request, 'test.html')    