def add_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nTarefa: '{nome_tarefa}' adicionada com sucesso")
    return

def ver_tarefas(tarefas):
    print("\nLista de tarefas: ")
    for index, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else ""
        nome_tarefa = tarefa["tarefa"]
        print(f"{index}. [{status}] {nome_tarefa}")
        return

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para: {novo_nome_tarefa}")
    else: 
        print("Indice de tarefa inválido")
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
    elif escolha == 3:
        ver_tarefas(tarefas)
        indice_tarefa = int(input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == 6:
        break
    else:
        break

print("\nPrograma finalizado\n")