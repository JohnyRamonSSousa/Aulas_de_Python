nome = "johny"

#Escopo local
if "nome" in locals():
    print("A variavel nome esta no escopo local")

if "idade" in locals():
    print("A variavel nao idade esta no escopo local")

#Escopo global
if "nome" in globals():
    print("A variavel nome esta no escopo Global")

if "idade" in globals():
    print("A variavel nome esta no escopo Global")

def teste():
    idade = 36

    if "idade" in globals():
        print("A idade esta no escopo Global")

    if "nome" in locals():
        print("A variavel nome esta no escopo local")

teste()