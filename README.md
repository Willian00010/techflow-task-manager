Markdown
# TechFlow Task Manager - Sistema de Gerenciamento de Tarefas Ágil

## 🎯 Sobre o Projeto
Este projeto foi desenvolvido para a **TechFlow Solutions** como solução de gerenciamento de tarefas para um cliente do setor de logística[cite: 1]. O objetivo é permitir o acompanhamento do fluxo de trabalho em tempo real, priorização de tarefas críticas e monitoramento de desempenho da equipe[cite: 1].

## 🛠️ Metodologia Utilizada
Adotou-se a metodologia **Kanban** (via GitHub Projects) para a gestão visual de tarefas, dividida em três colunas principais:
- **To Do**: Tarefas aguardando início.
- **In Progress**: Tarefas em desenvolvimento.
- **Done**: Tarefas concluídas e validadas.

## 🗂️ Estrutura do Repositório
- `/src`: Código fonte da aplicação contendo a classe de regras de negócio (`Gestor_de_tarefas.py`) e a interface interativa de terminal (`main.py`).
- `/tests`: Testes automatizados unitários desenvolvidos com `pytest` (`test_gestor_de_tarefas.py`).
- `/docs`: Documentação técnica e diagramas UML.
- `/.github/workflows`: Configuração de CI via GitHub Actions para validação contínua.

## 🚀 Como Executar o Projeto Localmente
### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.

## 🛠️ Metodologia Utilizada
Abra o terminal na pasta raiz do projeto e instale os pacotes necessários:
```bash
pip install -r requirements.txt


## 🚀 Como Executar o Projeto
Para interagir com o sistema (criar tarefas, listar em formato de tabela e atualizar status):

Bash
python src/main.py


Executar os Testes Automatizados
Para rodar a suíte de testes com o pytest:

Bash
pytest -v


## 🔄 Gerenciamento de Mudança de Escopo
Motivação Operacional
A equipe de operações logísticas identificou a necessidade de classificar as tarefas de acordo com o nível de urgência do frete (ex.: cargas expressas vs. entregas convencionais).

Modificações Realizadas
Modelagem e Código Source (src/):

A classe GestorDeTarefas foi refatorada para aceitar o argumento prioridade.

Valores aceitos: 'Baixa', 'Média', 'Alta'.

Garantia de Qualidade (tests/):

Atualizados os testes unitários no pytest para cobrir o atributo de prioridade sem quebrar as funcionalidades legadas.

Esteira de CI (.github/workflows/):

A alteração passou automaticamente pelo pipeline de integração contínua (GitHub Actions), validando a estabilidade da aplicação.

Projeto desenvolvido para a disciplina de Engenharia de Software - UniFECAF.