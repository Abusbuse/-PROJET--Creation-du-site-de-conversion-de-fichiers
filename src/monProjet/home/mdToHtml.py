from django.http import HttpResponse
from reportlab.pdfgen import canvas
import os
import markdown
from tkinter import  filedialog


def convertFileMdToHtml(request):
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Markdown file" ,"*.md")))
    
    sizeFile= os.path.getsize(filename)
    
    if filename == "":
        print("Aucun fichier sélectionné")
    elif sizeFile > 10000000:
        print("Fichier trop volumineux")
    else:
        with open(filename, "r") as f:
            text=f.read()
            html=markdown.markdown(text)

        with open(os.path.expanduser("~/Downloads/mdConvert.html"), "w") as f:
            f.write(html)
                    
        print("Fichier converti avec succès !")
    
    return HttpResponse("""<html> <script> window.location.replace('/');</script> </html>""")
    
