import sys
import os
import pytest

# Adiciona o diretório raiz do projeto ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa da pasta src
from src.Gestor_de_tarefas import GestorDeTarefas


def test_criar_tarefa_com_sucesso():
    """
    Teste 1: Verifica se uma tarefa é criada com sucesso com os dados corretos.
    """
    gestor = GestorDeTarefas()
    tarefa = gestor.criar_tarefa("Entrega Expressa", "Entregar pacote urgente na zona sul", "Alta")
    
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Entrega Expressa"
    assert tarefa["status"] == "To Do"
    assert tarefa["prioridade"] == "Alta"


def test_criar_tarefa_sem_titulo_deve_falhar():
    """
    Teste 2: Verifica se o sistema impede a criação de tarefa sem título (Qualidade).
    """
    gestor = GestorDeTarefas()
    # Espera-se que o sistema lance um erro ao tentar enviar título vazio
    with pytest.raises(ValueError, match="O título da tarefa não pode ser vazio."):
        gestor.criar_tarefa("", "Descrição sem título")


def test_atualizar_status_com_sucesso():
    """
    Teste 3: Verifica a mudança de status da tarefa no fluxo Kanban.
    """
    gestor = GestorDeTarefas()
    tarefa = gestor.criar_tarefa("Mapear Rota", "Mapeamento da rota de entrega")
    
    # Atualiza o status para 'In Progress'
    tarefa_atualizada = gestor.atualizar_status(tarefa["id"], "In Progress")
    assert tarefa_atualizada["status"] == "In Progress"