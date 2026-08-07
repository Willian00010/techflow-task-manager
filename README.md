# TechFlow Task Manager - Sistema de Gerenciamento de Tarefas Ágil

## 🎯 Sobre o Projeto
Este projeto foi desenvolvido para a **TechFlow Solutions** como solução de gerenciamento de tarefas para um cliente do setor de logística. O objetivo é permitir o acompanhamento do fluxo de trabalho em tempo real, priorização de tarefas críticas e monitoramento de desempenho da equipe.

## 🛠️ Metodologia Utilizada
Adotou-se a metodologia **Kanban** para a gestão visual de tarefas, dividida em três colunas principais:
- **To Do**: Tarefas aguardando início.
- **In Progress**: Tarefas em desenvolvimento.
- **Done**: Tarefas concluídas e validadas.

## 🗂️ Estrutura do Repositório
- `/src`: Código fonte da aplicação.
- `/tests`: Testes automatizados unitários.
- `/docs`: Documentação técnica e diagramas UML.
- `/.github/workflows`: Configuração de CI via GitHub Actions.

## 🚀 Como Executar o Projeto
*(Instruções para rodar o código localmente)*


## 🔄 Gerenciamento de Mudança de Escopo

### Motivação Operacional
A equipe de operações logísticas identificou a necessidade de classificar as tarefas de acordo com o nível de urgência do frete (ex.: cargas expressas vs. entregas convencionais). 

### Modificações Realizadas
1. **Modelagem e Código Source (`src/`):**
   - A classe `GestorDeTarefas` foi refatorada para aceitar o argumento `prioridade`.
   - Valores aceitos: `'Baixa'`, `'Média'`, `'Alta'`.

2. **Garantia de Qualidade (`tests/`):**
   - Atualizados os testes unitários no `pytest` para cobrir o atributo de prioridade sem quebrar as funcionalidades legadas.

3. **Esteira de CI (`.github/workflows/`):**
   - A alteração passou automaticamente pelo pipeline de integração contínua (GitHub Actions), validando a estabilidade da aplicação.

   ---
*Projeto desenvolvido para a disciplina de Engenharia de Software - UniFECAF.*
