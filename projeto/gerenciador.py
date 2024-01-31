def add_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nTarefa: '{nome_tarefa}' adicionada com sucesso")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    for index, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else "✖"
        nome_tarefa = tarefa["tarefa"]
        print(f"{index}. [{status}] {nome_tarefa}")
        return
    

tarefas = []
while True:
    print("\nMenu do gerenciador de lista de tarefas")
    print("\n1. Adicionar de tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = int(input("\nDigite a sua escolha: "))

    if escolha == 1:
        nome_tarefa = input("\nDigite o nome da nova tarefa: ")
        add_tarefa(tarefas, nome_tarefa)    
    elif escolha == 2:
        ver_tarefas(tarefas)
    elif escolha == 6:
        break
    else:
        break

print("\nPrograma finalizado\n")