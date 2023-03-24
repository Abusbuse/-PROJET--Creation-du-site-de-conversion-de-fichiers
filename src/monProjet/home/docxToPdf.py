from django.http import HttpResponse
import os
from tkinter import  filedialog
from docx2pdf import convert

#fonction qui prend le fichier docx et le convertit en pdf
def convertFileDocxToPdf(request):
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Docx files" ,"*.docx"),("all files","*.*")))
    
    #Récupère la taille du fichier
    sizeFile= os.path.getsize(filename)
    
    #si l'utilisateur annule l'opération
    if filename == "":
        print("Aucun fichier sélectionné")
    elif sizeFile > 10000000:
        print("Fichier trop volumineux")
    else:
        #télécharge le fichier converti dans le dossier de téléchargement du pc de l'utilisateur
        convert(filename, os.path.expanduser("~/Downloads/"))
        
        print("Fichier converti avec succès !")
        
    return HttpResponse("""<html> <script> window.location.replace('/convert/');</script> </html>""")