from django.http import HttpResponse
import os
from tkinter import  filedialog
from moviepy.editor import *
from pygame import *
from tkinter import *

#Fonction qui convertit le fichier mp4 en mp3
def convertMp4ToMp3(request):
    root=Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost',True)
    filename = filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select file",filetypes = (("mp4 files" ,"*.mp4"),("all files","*.*")))
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
            videoclip=VideoFileClip(filename)
            audioclip=videoclip.audio
            #télécharger le fichier audio.mp3 dans le dossier Downloads
            audioclip.write_audiofile(os.path.expanduser("~/Downloads/")+"audio.mp3")
            audioclip.close()
            videoclip.close()           
            print("Fichier converti avec succès !")
            alert ="('Fichier converti');"        
    return HttpResponse("""<html> <script> alert"""+ alert + """window.location.replace('/convert/');</script> </html>""")    
    