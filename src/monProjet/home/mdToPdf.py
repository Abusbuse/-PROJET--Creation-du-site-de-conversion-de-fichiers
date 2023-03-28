from django.http import HttpResponse
from tkinter import  filedialog
from reportlab.pdfgen import canvas
import os
import markdown

def convertFileMdToPdf(request):
    
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Markdown file" ,"*.md"),("all files","*.*")))
    
    sizeFile= os.path.getsize(filename)
    
    if filename == "":
        print("Aucun fichier sélectionné")
    elif sizeFile > 10000000:
        print("Fichier trop volumineux")
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
        
    return HttpResponse("""<html> <script> alert("Fichier converti");window.location.replace('/convert/');</script> </html>""")