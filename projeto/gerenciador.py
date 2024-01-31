tarefas = []

def add_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} adicionada com sucesso")
    return

while True:
    print("Menu do gerenciador de lista de tarefas")
    print("1. Adicionar de tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome_tarefa = input("Digite o nome da nova tarefa: ")
        add_tarefa(tarefas, nome_tarefa)
    elif escolha == 6:
        break


print(tarefas)

print("Programa finalizado")