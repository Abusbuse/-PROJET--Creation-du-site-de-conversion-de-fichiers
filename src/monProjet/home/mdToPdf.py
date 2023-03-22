from reportlab.pdfgen import canvas
import os
import markdown

with open("test.md", "r") as f:
    #une boucle while pour lire le fichier ligne par ligne
    #et ajouter chaque ligne à une variable text
    text=f.read().splitlines()

pdf=canvas.Canvas("test.pdf")
texte=""


for i in range(len(text)):
    pdf.drawString(50, 800-15*i, text[i])

pdf.save() 