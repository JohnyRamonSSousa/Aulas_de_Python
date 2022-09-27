frase = "Hoje nao teve aula de violino"

print(frase)

palavra = "violino"
palavra2 = "teste"

if palavra not in frase:
    print("A frase nao contem a palavra: " + palavra)
else:
    print("A frase contem a palavra:" + palavra)

if palavra2 not in frase:
    print("A frase nao contem a palavra: " + palavra2)
else:
    print("A frase contem a palavra:" + palavra2)

if frase.count(palavra) == 0:
    print("A frase nao contem a palavra: " + palavra)
else:
    print("A frase contem a palavra:" + palavra)