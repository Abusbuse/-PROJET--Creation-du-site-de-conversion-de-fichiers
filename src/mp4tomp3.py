import os
from moviepy.editor import *
from pygame import *

#Fonction qui convertit le fichier mp4 en mp3
def ConvertMp4ToMp3(filename):
    videoclip=VideoFileClip(filename)
    audioclip=videoclip.audio
    #télécharger le fichier audio.mp3 dans le dossier Downloads
    audioclip.write_audiofile(os.path.expanduser("~/Downloads/")+"audio.mp3")
    audioclip.close()
    videoclip.close()