from docx2pdf import convert
import os

#fonction qui prend le fichier docx et le convertit en pdf
def convertFileDocxToPdf(filename):
    #si l'utilisateur annule l'opération
    if filename == "":
        print("Aucun fichier sélectionné")
    else:
        #télécharge le fichier converti dans le dossier de téléchargement du pc de l'utilisateur
        convert(filename, os.path.expanduser("~/Downloads/"))