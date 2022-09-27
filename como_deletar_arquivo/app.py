import os 

if os.path.exists("teste.c"):
    os.remove("teste.c")
    print("Foi excluido com sucesso")
else:
    print("O arquivo nao existe")