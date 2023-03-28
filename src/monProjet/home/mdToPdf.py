from django.http import HttpResponse
from tkinter import  filedialog
from reportlab.pdfgen import canvas
import os
import markdown
from tkinter import *

def convertFileMdToPdf(request):
    root=Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost',True)
    filename = filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("Markdown file" ,"*.md"),("all files","*.*")))
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
            with open(filename, "r") as f:
                #une boucle while pour lire le fichier ligne par ligne
                #et ajouter chaque ligne à une variable text
                text=f.read().splitlines()
            pdf=canvas.Canvas(os.path.expanduser("~/Downloads/mdConvert.pdf"))           
            for i in range(len(text)):
                pdf.drawString(50, 800-15*i, text[i])
            pdf.save()           
            print("Fichier converti avec succès !")
            alert ="('Fichier converti');"       
    return HttpResponse("""<html> <script> alert"""+ alert + """window.location.replace('/convert/');</script> </html>""")