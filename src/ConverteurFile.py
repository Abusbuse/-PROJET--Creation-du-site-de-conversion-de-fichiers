from tkinter import  filedialog
from tkinter import *

from docxToPdf import convertFileDocxToPdf
from mp4Tomp3 import ConvertMp4ToMp3
from htmlToPdf import convertFileHtmlToPdf

#################################################################################################################################

#Attributs
filename = ""
windowMain = None
        
##################################################################################################################################

#fonction qui ouvre l'explorateur de fichier pour choisir le fichier et le garde en mémoire
def openFile():
    global filename
    #ouvre l'explorateur de fichier
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("Word files","*.docx"),("Video files" ,"*.mp4")))
    return filename
        
##################################################################################################################################
        
def windowDocxToPdf():
    
    #création de la fenêtre secondaire qui va permettre de convertir le fichier docx en pdf
    global win2
    win2 = Toplevel(windowMain)
    win2.title("Convertir un fichier docx en pdf")
    win2.geometry("500x500")
    win2.config(background='#B1B1B1')
    
    lbl = Label(win2, text="Convertit vos fichiers docx en pdf", font=("Arial", 20), bg='#B1B1B1', fg='#000000')
    lbl.pack(pady=20)
    
    #bouton pour ouvrir convertir le fichier
    btnConvert = Button(win2, text="Convertir", command= lambda: convertFileDocxToPdf(openFile()))
    btnConvert.pack(pady=20)
    
    #Bouton pour quitter la fenêtre 
    btnQuit = Button(win2, text="Quitter", command= win2.destroy)
    btnQuit.pack(pady=20)
    
    win2.mainloop()
    
def windowMp4ToMp3():
    
    #création de la fenêtre secondaire qui va permettre de convertir le fichier docx en pdf
    global win3
    win2 = Toplevel(windowMain)
    win2.title("Convertir un fichier mp4 en mp3")
    win2.geometry("500x500")
    win2.config(background='#B1B1B1')
    
    lbl = Label(win2, text="Convertit vos fichiers mp4 en mp3", font=("Arial", 20), bg='#B1B1B1', fg='#000000')
    lbl.pack(pady=20)
    
    #bouton pour ouvrir convertir le fichier
    btnConvert = Button(win2, text="Convertir", command= lambda: ConvertMp4ToMp3(openFile()))
    btnConvert.pack(pady=20)
    
    #Bouton pour quitter la fenêtre 
    btnQuit = Button(win2, text="Quitter", command= win2.destroy)
    btnQuit.pack(pady=20)
    
    win2.mainloop()


def windowHtmlToPdf():
        
    #création de la fenêtre secondaire qui va permettre de convertir le fichier docx en pdf
    global win4
    win4 = Toplevel(windowMain)
    win4.title("Convertir un fichier html en pdf")
    win4.geometry("500x500")
    win4.config(background='#B1B1B1')
    
    lbl = Label(win4, text="Convertit vos fichiers html en pdf", font=("Arial", 20), bg='#B1B1B1', fg='#000000')
    lbl.pack(pady=20)
    
    #bouton pour ouvrir convertir le fichier
    btnConvert = Button(win4, text="Convertir", command= lambda: convertFileHtmlToPdf())
    btnConvert.pack(pady=20)
    
    #Bouton pour quitter la fenêtre 
    btnQuit = Button(win4, text="Quitter", command= win4.destroy)
    btnQuit.pack(pady=20)
    
    win4.mainloop()
    
##################################################################################################################################
        
#création de la fenêtre
def windowAccueil():
    
    #Attributs
    fontTitle = ("Arial", 20, "bold")
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
    menu.add_cascade(label="Types de conversion \/", menu=fileMenu)
    menu.add_command(label="Quitter", command=windowMain.destroy)

    #boutons présents dans le menu fichier
    fileMenu.add_command(label="Docx en pdf", command=windowDocxToPdf)
    fileMenu.add_command(label="Mp4 en mp3", command=windowMp4ToMp3)
    fileMenu.add_command(label="Html en pdf", command=windowHtmlToPdf)
    
    #Configuration du menu
    fileMenu.config(bg='#FFFFFF', fg=fontColor, activebackground='#5F9EA0', activeforeground='#000000')
    menu.config(bg='#FFFFFF', fg=fontColor, activebackground='#5F9EA0', activeforeground='#000000')
    
    #titre de la fenêtre en gras
    TitreMain = Label(windowMain, text="Application qui convertit vos fichiers", font=fontTitle, bg=fontBg, fg=fontColor)
    #Encadrement du titre
    TitreMain.config(padx=20, pady=20)
    TitreMain.pack(pady=20)
    
    #Contenu de la fenêtre principale
    lbl = Label(windowMain, text="Bienvenue sur notre nouvelle application.", font=fontContent, bg=fontBg, fg=fontColor)
    
    #Expliquer ce que fait l'application
    lbl2 = Label(windowMain, text="Cette application vous permet de convertir vos fichiers en plusieurs types.", font=fontContent, bg=fontBg, fg=fontColor)
    
    #Expliquer comment l'utiliser
    lbl3 = Label(windowMain, text="Pour commencer, cliquez sur le menu en haut de la page.", font=fontContent, bg=fontBg, fg=fontColor)
    
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