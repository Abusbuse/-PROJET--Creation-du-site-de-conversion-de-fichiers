from django.http import HttpResponse
import os
from tkinter import  filedialog
from PIL import Image as PILImage
from tkinter import *

#fonction qui prend le fichier docx et le convertit en pdf
def convertFilePngToJpg(request):
    root=Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost',True)
    #Ouvre une fenêtre pour sélectionner le fichier
    filename = filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("PNG file" ,"*.png"),("all files","*.*")))
    root.destroy()
    
    #si l'utilisateur ne sélectionne pas de fichier
    if filename == "":
        print("Aucun fichier sélectionné")
        alert ="('Aucun fichier sélectionné');"
    #Si l'utilisateur sélectionne un fichier
    elif filename[-3:] == "png":
        #Récupère la taille du fichier
        sizeFile= os.path.getsize(filename)
        #si le fichier est trop volumineux
        if sizeFile > 10000000:
            print("Fichier trop volumineux")
            alert ="('Fichier trop volumineux');"
        #Si tout est bon
        else:
            #Converti l'image png en jpeg
            im = PILImage.open(filename)
            im = im.convert('RGB')
            im.save(os.path.expanduser("~/Downloads/Image.jpeg"), 'jpeg')
            print("Fichier converti avec succès !")
            alert ="('Fichier converti');"
    else:
        print("Fichier non pris en charge")
        alert ="('Fichier non pris en charge');"
    return HttpResponse("""<html> <script> alert"""+ alert + """window.location.replace('/convert/');</script> </html>""")