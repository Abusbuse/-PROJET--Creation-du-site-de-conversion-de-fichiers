from django.http import HttpResponse
import os
from tkinter import  filedialog
from pyhtml2pdf import converter
from tkinter import *

#Fonction qui prend le fichier html et le convertit en pdf
#Faudra changer la fonction
def convertFileHtmlToPdf(request):
    root=Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost',True)
    filename = filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("Html files" ,"*.html"),("all files","*.*")))
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
            converter.convert(filename, os.path.expanduser("~/Downloads/")+"FichierConverti.pdf")
            print("Fichier converti avec succès !")
            alert ="('Fichier converti');"
    return HttpResponse("""<html> <script> alert"""+ alert + """window.location.replace('/convert/');</script> </html>""")