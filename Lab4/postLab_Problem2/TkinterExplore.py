from tkinter import filedialog
from tkinter import *
import os.path

nameFile = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
print(nameFile)
nameFile = os.path.basename(nameFile)
print(nameFile)