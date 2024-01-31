print("Utilizando lista")
lista = [1,2,3,4,5]
for item in lista:
    print('lista: ', item)

print("Utilizando tupla")
tupla = [6,7,8,9,10]
for item in tupla:
    print('tupla: ', item)

print("Utilizando dicionario")
pessoa = {"nome": "João", "idade": 29, "cidade": "São Paulo"}
print("- Utilizando keys")
for chave in pessoa.keys():
    print(chave)

print("- Utilizando values")
for value in pessoa.values():
    print(value)

print("- Utilizando items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("Criando um range de elementos")
print(list(range(0,10)))

print("Utilizando a function range()")
for numero in range(0,10):
    print("Número: ", numero)

print("Utilizando a function len()")
lista = [1,2,3,4,5]
print(lista)
for indice in range(0,len(lista)):
    if indice == 3:
        lista[indice] = 55
    else:
        lista[indice] = 00    
print(lista)

print("Utilizando a function enumerate")
lista_enumerada = ["a","b","c"]
for indice, valor in enumerate(lista_enumerada):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")