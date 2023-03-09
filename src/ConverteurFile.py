from docx2pdf import convert
from tkinter import  filedialog
from tkinter import *
import tkinter as tk
import os

#################################################################################################################################

#Attributs
filename = "" 
windowMain = None
    
##################################################################################################################################

#fonction qui prend le fichier docx et le convertit en pdf
def convertFileDocxToPdf(filename):
    #si l'utilisateur annule l'opération
    if filename == "":
        print("Aucun fichier sélectionné")
    else:
        #télécharge le fichier converti dans le dossier de téléchargement du pc de l'utilisateur
        convert(filename, os.path.expanduser("~/Downloads/"))

        #Affiche un message de confirmation
        lbl = Label(win2, text="Fichier converti avec succès !", font=("Arial", 20), bg='#FFFFFF', fg='#000000')
        lbl.pack(pady=20)   
        
##################################################################################################################################

#fonction qui ouvre l'explorateur de fichier pour choisir le fichier et le garde en mémoire
def openFile():
    global filename
    #ouvre l'explorateur de fichier
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Word files","*.docx", "*.odt"),("all files","*.*")))
    return filename
        
##################################################################################################################################
        
def windowDocxToPdf():
    
    #création de la fenêtre secondaire qui va permettre de convertir le fichier docx en pdf
    global win2
    win2 = Toplevel(windowMain)
    win2.title("Convertir un fichier docx en pdf")
    win2.geometry("500x500")
    win2.config(background='#FFFFFF')
    
    lbl = Label(win2, text="Convertit vos fichiers docx en pdf", font=("Arial", 20), bg='#B1B1B1', fg='#000000')
    lbl.pack(pady=20)
    
    #bouton pour ouvrir convertir le fichier
    btnConvert = Button(win2, text="Convertir", command= lambda: convertFileDocxToPdf(openFile()))
    btnConvert.pack(pady=20)
    
    #Bouton pour quitter la fenêtre 
    btnQuit = Button(win2, text="Quitter", command= win2.destroy)
    btnQuit.pack(pady=20)
    
    win2.mainloop()
    
##################################################################################################################################
        
#création de la fenêtre
def windowAccueil():
    
    #Attributs
    fontTitle = ("Arial", 20)
    fontContent = ("Arial", 14)
    fontBg = "#B1B1B1"
    fontColor = "#000000"
    
    #création de la fenêtre principale
    windowMain = Tk()
    windowMain.title("Convertisseur de fichier")
    windowMain.geometry("500x500")
    
    #Taille minimum de la fenêtre
    windowMain.minsize(300, 300)
    
    #Taille maximum de la fenêtre
    windowMain.maxsize(500, 500)
    
    #couleur de fond de la fenêtre
    windowMain.config(background='#B1B1B1')
    
    ## CONTENT ##
    
    #Menu
    menu = Menu(windowMain)
    windowMain.config(menu=menu)
    
    #Menu fichier
    fileMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Types de conversion", menu=fileMenu)
    menu.add_command(label="Quitter", command=windowMain.destroy)

    #boutons présents dans le menu fichier
    fileMenu.add_command(label="Docx en pdf", command=windowDocxToPdf)
    
    #Configuration du menu
    fileMenu.config(bg='#FFFFFF', fg=fontColor, activebackground='#5F9EA0', activeforeground='#000000')
    menu.config(bg='#FFFFFF', fg=fontColor, activebackground='#5F9EA0', activeforeground='#000000')
    
    #titre de la fenêtre
    TitreMain = Label(windowMain, text="Application qui convertit vos fichiers", font= fontTitle, bg=fontBg, fg=fontColor)
    #Encadrement du titre
    TitreMain.config(padx=20, pady=20)
    TitreMain.pack(pady=20)
    
    #Contenu de la fenêtre principale
    lbl = Label(windowMain, text="Bienvenue sur notre nouvelle application", font=fontContent, bg=fontBg, fg=fontColor)
    
    #Expliquer ce que fait l'application
    lbl2 = Label(windowMain, text="Cette application vous permet de convertir vos fichiers en plusieurs types", font=fontContent, bg=fontBg, fg=fontColor)
    
    #Expliquer comment l'utiliser
    lbl3 = Label(windowMain, text="Pour commencer, cliquez sur le menu en haut de la page", font=fontContent, bg=fontBg, fg=fontColor)
    
    #Faire en sorte que les labels aillent à la ligne si le texte est trop long
    lbl.config(wraplength=400)
    lbl2.config(wraplength=400)
    lbl3.config(wraplength=400)
      
    lbl.pack(pady=20)
    lbl2.pack(pady=20)
    lbl3.pack(pady=20)
    
    #Ajout d'un footer à la fenêtre
    footer = Label(windowMain, text="© 2023 - Tous droits réservés", font=fontContent, bg=fontBg, fg=fontColor)
    footer.pack(side=BOTTOM, pady=20)
    
    windowMain.mainloop()
    
# main 
if __name__ == "__main__":
    windowAccueil()