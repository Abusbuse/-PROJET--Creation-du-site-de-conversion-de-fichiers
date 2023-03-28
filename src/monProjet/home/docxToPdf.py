from django.http import HttpResponse
import os
from tkinter import  filedialog
from docx2pdf import convert
from tkinter import *

#fonction qui prend le fichier docx et le convertit en pdf
def convertFileDocxToPdf(request):
    root=Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost',True)
    #Ouvre une fenêtre pour sélectionner le fichier
    filename = filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("Docx files" ,"*.docx"),("all files","*.*")))
    root.destroy()
    
    #si l'utilisateur ne sélectionne pas de fichier
    if filename == "":
        print("Aucun fichier sélectionné")
        alert ="('Aucun fichier sélectionné');"
    else:
        #Récupère la taille du fichier
        sizeFile= os.path.getsize(filename)
        if sizeFile > 10000000:
            print("Fichier trop volumineux")
            alert ="('Fichier trop volumineux');"
            
        else:
            #télécharge le fichier converti dans le dossier de téléchargement du pc de l'utilisateur
            convert(filename, os.path.expanduser("~/Downloads/"))
            
            print("Fichier converti avec succès !")
            alert ="('Fichier converti');"

    return HttpResponse("""<html> <script> alert"""+ alert + """window.location.replace('/convert/');</script> </html>""")