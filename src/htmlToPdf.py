import os
from tkinter import  filedialog
from pyhtml2pdf import converter

#Fonction qui prend le fichier html et le convertit en pdf
def convertFileHtmlToPdf():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Html files" ,"*.html")))
    if filename == "":
        print("Aucun fichier sélectionné")
    else:
        #convertit le fichier html en pdf
        converter.convert(filename, "htmlConvert.pdf")

        #message de confirmation
        print("Fichier converti avec succès !")
    
    #Déplacer le fichier dans le dossier téléchargement
    #os.rename("htmlConvert.pdf", os.path.expanduser("~/Downloads/htmlConvert.pdf"))
