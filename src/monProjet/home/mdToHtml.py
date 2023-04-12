from django.http import HttpResponse
from reportlab.pdfgen import canvas
import os
import markdown
from tkinter import  filedialog
from tkinter import *

def convertFileMdToHtml(request):
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
    elif filename[-2:] == "md":
        #Récupère la taille du fichier
        sizeFile= os.path.getsize(filename)
        if sizeFile > 10000000:
            print("Fichier trop volumineux")
            alert ="('Fichier trop volumineux');"
        else:
            with open(filename, "r") as f:
                text=f.read()
                html=markdown.markdown(text)
            with open(os.path.expanduser("~/Downloads/mdConvert.html"), "w") as f:
                f.write(html)           
            print("Fichier converti avec succès !")
            alert ="('Fichier converti');"
    else:
        print("Fichier non pris en charge")
        alert ="('Fichier non pris en charge');"   
    return HttpResponse("""<html> <script> alert"""+ alert + """window.location.replace('/convert/');</script> </html>""")    
