from django.http import HttpResponse
import os
from tkinter import  filedialog
from pyhtml2pdf import converter

#Fonction qui prend le fichier html et le convertit en pdf
def convertFileHtmlToPdf(request):
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Html files" ,"*.html")))
    if filename == "":
        print("Aucun fichier sélectionné")
    else:
        #convertit le fichier html en pdf
        converter.convert(filename, os.path.expanduser("~/Downloads/")+"FichierConverti.pdf")

        #message de confirmation
        print("Fichier converti avec succès !")
        
    return HttpResponse("""<html> <script> window.location.replace('/');</script> </html>""")