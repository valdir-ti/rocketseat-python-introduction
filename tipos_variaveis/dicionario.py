# Coleção não ordenada de pares de elementos de chave:valor
pessoa = {
    "id": 12,
    "nome": "Jane Doe",
    "idade": 32
}

# Exibindo o dicionario todo
print("Pessoa: ", pessoa)

# Exibindo o elemento pela chave
print("Pessoa: ", pessoa["idade"])


# Exibindo o elemento atualizado
pessoa["idade"] = 44
print("Pessoa idade atualizada: ", pessoa["idade"])

# Deletando um elemento
del pessoa["idade"]
print("Pessoa sem a chave idade: ", pessoa)

# keys(), value(), items()
chaves = list(pessoa.keys())
values = list(pessoa.values())
items = list(pessoa.items())
print("Chaves: ", chaves)
print("Primeira chave: ", chaves[0])
print("Valores: ", values)
print("Primeiro valor: ", values[0])
print("Items: ", items)
print("Primeiro item: ", items[0][0])
print("Primeiro Valor: ", items[0][1])