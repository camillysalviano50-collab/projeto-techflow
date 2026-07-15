# Sistema de Gerenciamento de Tarefas - TaskFlow
tarefas = []

def adicionar_tarefa(titulo):
    tarefas.append({"titulo": titulo, "status": "A Fazer"})
    print(f"Tarefa '{titulo}' adicionada.")

def concluir_tarefa(titulo):
    for t in tarefas:
        if t["titulo"] == titulo:
            t["status"] = "Concluído"
            print(f"Tarefa '{titulo}' marcada como concluída.")

adicionar_tarefa("Estudar Engenharia de Software")
concluir_tarefa("Estudar Engenharia de Software")
