from django.http import HttpResponse
import os
from tkinter import  filedialog
from pyhtml2pdf import converter

#Fonction qui prend le fichier html et le convertit en pdf
#Faudra changer la fonction
def convertFileHtmlToPdf(request):
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Html files" ,"*.html")))
    
    #Récupère la taille du fichier
    sizeFile= os.path.getsize(filename)
    
    if filename == "":
        print("Aucun fichier sélectionné")
    #Si le fichier est supérieur à 10Mo, on ne le convertit pas
    if sizeFile > 10000000:
        print("Fichier trop volumineux")
    else:
        #convertit le fichier html en pdf
        converter.convert(filename, os.path.expanduser("~/Downloads/")+"FichierConverti.pdf")

        #message de confirmation
        print("Fichier converti avec succès !")
        
    return HttpResponse("""<html> <script> window.location.replace('/');</script> </html>""")