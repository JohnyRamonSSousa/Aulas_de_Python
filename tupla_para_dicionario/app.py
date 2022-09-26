tupla = (('valor', 'chave'), ('nome', 'Johny'), ('idade', 30))

print(tupla)
print(tupla[1][1])
print(tupla[0][1])
print(tupla[2][1])

dicionario = dict((x, y) for x, y in tupla)

print(dicionario)
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['valor'])