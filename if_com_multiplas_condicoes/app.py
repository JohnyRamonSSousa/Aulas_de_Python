#Usuario ele pode ou nao dirigir

cnh = True
idade = 18
idade_base = 18

if((cnh == True) and (idade >= idade_base)):
    print("O usuario pode dirigir um carro")


cnh = True
ano = 15
ano_base = 18

if((cnh == True) and (ano >= ano_base)):
    print("O usuario pode dirigir um carro")
else:
    print("O usuario nao pode dirigir o carro")


nome = "johny"
idadeDeJohny = 36
idadeDeJohnyBase = 40

if((nome == "johny") and (idadeDeJohny >= idadeDeJohnyBase)):
  print("bom dia johny")
else:
    print("A idade ta diferente")