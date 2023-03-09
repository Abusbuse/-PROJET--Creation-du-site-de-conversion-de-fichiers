import os
from tkinter import *
from tkinter import filedialog
from moviepy.editor import *
from pygame import *

#lancer la video test.mp4
def mp4tomp3(filename):
    videoclip=VideoFileClip(filename)
    audioclip=videoclip.audio
    #télécharger le fichier audio.mp3 dans le dossier Downloads
    audioclip.write_audiofile(os.path.expanduser("~/Downloads/")+"audio.mp3")
    audioclip.close()
    videoclip.close()