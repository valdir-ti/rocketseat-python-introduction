# if, elif, else

# Exemplo
idade = 18
print("Exemplo do comando if")
if idade >= 18:
    print("Você é maior de idade")
elif idade >= 12:
    print("Você é adolescente")
else:
    print("Você é menor de idade")

# Exemplo 2
mensagem = "VocÊ pode tirar habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"

print(mensagem)