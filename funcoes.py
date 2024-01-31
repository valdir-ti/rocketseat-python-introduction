def saudacao(nome):
    print(f"Olá {nome}!")

print("Chamando a função saudação: ")
saudacao("José")
saudacao("Alice")

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Chamando a função com retorno do quadrado: ")
resultado_quadrado = quadrado(32)
print(resultado_quadrado)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("Chamando a função de soma: ")
numero1 = 12
numero2 = 87
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s com o numero %s é: %s" % (numero1, numero2, resultado_soma))