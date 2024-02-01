print("Exemplo de exceções")
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variável incompatível")
except Exception as e:
    print(f"Erro exception: {e}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Operação finalizada")
