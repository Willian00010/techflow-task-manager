import sys
import os

# Importa a classe GestorDeTarefas que você já criou
from Gestor_de_tarefas import GestorDeTarefas


def exibir_menu():
    """Exibe o menu de opções na tela."""
    print("\n" + "=" * 45)
    print(" 🚚 TECHFLOW TASK MANAGER - PAINEL LOGÍSTICO ")
    print("=" * 45)
    print(" [1] Criar Nova Tarefa")
    print(" [2] Listar Todas as Tarefas")
    print(" [3] Atualizar Status de uma Tarefa")
    print(" [4] Sair")
    print("=" * 45)


def listar_tarefas_formatadas(tarefas):
    """Exibe a lista de tarefas em formato de tabela legível."""
    if not tarefas:
        print("\n⚠️  Nenhuma tarefa cadastrada até o momento.")
        return

    print("\n" + "-" * 65)
    print(f"{'ID':<5} | {'TÍTULO':<22} | {'PRIORIDADE':<10} | {'STATUS':<12}")
    print("-" * 65)

    for tarefa in tarefas:
        # Pega a prioridade (usa 'Média' se não houver)
        prioridade = tarefa.get("prioridade", "Média")
        print(
            f"{tarefa['id']:<5} | {tarefa['titulo']:<22} | {prioridade:<10} | {tarefa['status']:<12}"
        )

    print("-" * 65)


def main():
    # Instancia o objeto que gerencia as tarefas
    gestor = GestorDeTarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        # OPTION 1: Criar Tarefa
        if opcao == "1":
            print("\n--- 📝 NOVA TAREFA ---")
            titulo = input("Título da tarefa: ").strip()
            descricao = input("Descrição: ").strip()
            prioridade = (
                input("Prioridade (Baixa, Média, Alta) [Média]: ").strip()
                or "Média"
            )

            try:
                # Chama a função que você testou no PyTest
                tarefa = gestor.criar_tarefa(titulo, descricao, prioridade)
                print(f"\n✅ Tarefa #{tarefa['id']} criada com sucesso!")
            except ValueError as erro:
                # Captura a validação de título vazio ou erro
                print(f"\n❌ Erro ao criar tarefa: {erro}")

        # OPTION 2: Listar Tarefas
        elif opcao == "2":
            # Pega a lista de tarefas cadastradas na memória
            # (Ajuste o nome do atributo se na sua classe for diferente de 'tarefas')
            lista = getattr(gestor, "tarefas", [])
            listar_tarefas_formatadas(lista)

        # OPTION 3: Atualizar Status
        elif opcao == "3":
            print("\n--- 🔄 ATUALIZAR STATUS ---")
            try:
                id_tarefa = int(input("Informe o ID da tarefa: "))
                print("Status disponíveis: To Do | In Progress | Done")
                novo_status = input("Novo status: ").strip()

                tarefa_atualizada = gestor.atualizar_status(
                    id_tarefa, novo_status
                )
                print(
                    f"\n✅ Status da tarefa #{id_tarefa} alterado para '{novo_status}'!"
                )
            except ValueError as erro:
                print(f"\n❌ Erro: {erro}")
            except Exception:
                print("\n❌ Digite um número de ID válido.")

        # OPTION 4: Sair
        elif opcao == "4":
            print("\nEncerrando o TechFlow Task Manager... Até logo!")
            break

        else:
            print("\n⚠️ Opção inválida. Por favor, escolha um número de 1 a 4.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()