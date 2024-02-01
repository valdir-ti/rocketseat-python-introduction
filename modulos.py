print("Import de módulo padrão")
from math import sqrt

numero = 25
raiz_quadrada = sqrt(numero)
print(f"Raiz quadrada de {numero} é {raiz_quadrada}")

print("Import de módulo personalizado")

from meu_modulo import saudacao, dobro
numero = 11
mensagem = meu_modulo.saudacao("Valdir")
resultado_dobro = meu_modulo.dobro(numero)

print(mensagem)
print(f"O dobro de {numero} é {resultado_dobro}")