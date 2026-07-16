# Projeto TechFlow Solutions - Sistema de Gerenciamento de Tarefas

## 1. Descrição do Projeto
Este projeto foi desenvolvido para a **TechFlow Solutions**, uma startup de logística, com o objetivo de criar um sistema web para o gerenciamento de tarefas. O sistema permite o acompanhamento do fluxo de trabalho em tempo real, priorização de tarefas e monitoramento de desempenho da equipe.

## 2. Metodologia
Utilizei metodologias ágeis para a gestão do desenvolvimento, organizando as demandas através de um quadro **Kanban** no GitHub Projects, com as colunas: 
*   **A Fazer (To Do)**
*   **Em Progresso (In Progress)**
*   **Concluído (Done)**

## 3. Como Executar
1. Clone este repositório:
   `git clone https://github.com/camillysalviano50-collab/projeto-techflow.git`
2. Instale as dependências necessárias:
   `pip install -r requirements.txt`
3. Execute a aplicação:
   `python main.py`

## 4. Gestão de Mudanças
Durante o ciclo de vida do projeto, foi necessária uma alteração de escopo para atender a uma nova demanda do cliente.

*   **Mudança efetuada:** Implementação de um filtro de prioridade (Baixa, Média, Alta) nas tarefas do sistema.
*   **Justificativa:** A equipe de logística da TechFlow precisava identificar visualmente quais entregas eram críticas, pois o volume de demandas aumentou significativamente.
*   **Impacto no Kanban:** Foi criado um novo card no Backlog ("Adicionar filtro de prioridade"), movido para "Em Progresso" durante a implementação e finalizado após a validação dos testes unitários.

## 5. Controle de Qualidade
Este projeto utiliza **GitHub Actions** para Integração Contínua (CI). Sempre que um novo código é enviado (push), o pipeline executa automaticamente os testes automatizados para garantir a estabilidade do sistema.
