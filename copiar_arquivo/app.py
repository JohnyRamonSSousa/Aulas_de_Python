from shutil import copyfile
import os

#arquivo de origem, arquivo copia

copyfile("texte.txt", "dir/texte2.copy.txt")

os.remove("texte.copy.txt")