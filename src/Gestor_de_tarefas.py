# src/gestor_de_tarefas.py

class GestorDeTarefas:
    """
    Classe responsável por gerenciar as tarefas do sistema TechFlow Solutions.
    """
    def __init__(self):
        # Lista para armazenar as tarefas na memória
        self.tarefas = []
        # Contador interno para gerar IDs únicos para cada tarefa
        self.proximo_id = 1

    def criar_tarefa(self, titulo, descricao, prioridade="Média"):
        """
        Cria uma nova tarefa e adiciona à lista.
        Valida se o título não está vazio.
        """
        if not titulo or not titulo.strip():
            raise ValueError("O título da tarefa não pode ser vazio.")

        # Cria a estrutura da tarefa como um dicionário
        tarefa = {
            "id": self.proximo_id,
            "titulo": titulo.strip(),
            "descricao": descricao.strip(),
            "status": "To Do",       # Status inicial padrão no Kanban
            "prioridade": prioridade # Campo referente à mudança de escopo
        }

        self.tarefas.append(tarefa)
        self.proximo_id += 1  # Incrementa o ID para a próxima tarefa
        return tarefa

    def listar_tarefas(self):
        """Retorna a lista completa de tarefas cadastradas."""
        return self.tarefas

    def atualizar_status(self, id_tarefa, novo_status):
        """
        Atualiza o status de uma tarefa existente (To Do -> In Progress -> Done).
        """
        status_validos = ["To Do", "In Progress", "Done"]
        if novo_status not in status_validos:
            raise ValueError(f"Status inválido. Use um dos seguintes: {status_validos}")

        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["status"] = novo_status
                return tarefa
        
        raise KeyError("Tarefa não encontrada.")
    