from reportlab.pdfgen import canvas
import os
import markdown

with open("test.md", "r") as f:
    text=f.read()
    html=markdown.markdown(text)

with open("test.html", "w") as f:
    f.write(html)
