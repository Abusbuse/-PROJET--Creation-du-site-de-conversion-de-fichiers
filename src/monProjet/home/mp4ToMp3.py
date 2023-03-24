from django.http import HttpResponse
import os
from tkinter import  filedialog
from moviepy.editor import *
from pygame import *

#Fonction qui convertit le fichier mp4 en mp3
def convertMp4ToMp3(request):
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("mp4 files" ,"*.mp4"),("all files","*.*")))
    
    sizeFile = os.path.getsize(filename)
    
    if filename == "":
        print("Aucun fichier sélectionné")
    if sizeFile > 10000000:
        print("Fichier trop volumineux")
    else:
        videoclip=VideoFileClip(filename)
        audioclip=videoclip.audio
        #télécharger le fichier audio.mp3 dans le dossier Downloads
        audioclip.write_audiofile(os.path.expanduser("~/Downloads/")+"audio.mp3")
        audioclip.close()
        videoclip.close()
        
        print("Fichier converti avec succès !")
        
    return HttpResponse("""<html> <script> alert("Fichier converti");window.location.replace('/convert/');</script> </html>""")
    
    