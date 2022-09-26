import os 
import pathlib
from pathlib import Path

#diretorios e arquivos
if os.path.isdir("diretorio"):
    print("O diretorio existe")
else:
    print("O diretorio nao existe")    

if Path("diretorio").is_dir():
    print("O diretorio existe")
else:
    print("O diretorio nao existe")

if Path("johny").is_dir():
    print("O diretorio johny existe")
else:
    print("O diretorio nao existe")