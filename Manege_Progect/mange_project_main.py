from tool import clear_screen
from Manege_Progect.projectclass import Progect, Projetcs
from time import sleep
import time

def Start_Progect():
    clear_screen()
    print("Bem Vindo ao Manage Project, um gestor de projetos!")
    if not Projetcs:
        print("1. Criar um Projeto")
        command = input("Digite sua opção: ")

        if command == "1":
            Create_Project()
    else:
        Main_Project()

def Main_Project():
    clear_screen()
    print(f"Projetos: {Projetcs}")
    print("1. Selecionar Projeto")
    print("2. Sair")
    command = input("Digite sua opção: ")

    if command == "1":
        index_project = input("Digite o índice do projeto: ")
        Manage_Project_Work(index=index_project)
    else:
        return
    
def Create_Project():
    clear_screen()
    project_name = input("Digite o nome do projeto: ")
    description = input("Digite a descrição do projeto (não obrigatório): ")
    language = input("Digite a linguagem de programação: (.py): ")

    if not description:
        description = "Não informada"

    new_project = Progect(
        name=project_name,
        description=description,
        language=language, 
        start_time= time.localtime()
    )
    Projetcs.append(new_project)

    sleep(1)

    print("Projeto criado com sucesso!")
    sleep(1)
    Main_Project()
    return

def Manage_Project_Work(index):
    clear_screen()
    try:
        project = Projetcs[int(index)]
    except IndexError:
        print("Projeto não encontrado.")
        return
    
    name = project.name
    description = project.description
    task_list = project.task_list
    start_time = project.start_time
    language = project.language

    print(f"Nome do Projeto: {name}")
    print("1. Tarefas")
    print("2. Sair")
    command = input("Digite sua opção: ")

    if command == "1":
        Tarefas(task_list)
        return
    elif command == "2":
        Main_Project()
        return

def Tarefas(task_list):
    clear_screen()
    print(f"Tarefas: {task_list}")
    print("1. Adicionar Tarefa")
    print("2. Completar Tarefa")
    command = input("Digite sua opção: ")

    if command == "1":
        Add_Task(task_list)
        return
    elif command == "2":
        Complete_Task(task_list)
        return

def Add_Task(task_list):
    clear_screen()
    task_name = input("Nome da Tarefa: ")
    description_task = input("Descrição da Tarefa: ")
    status_task = input("Status da tarefa (1 = Concluída, 0 = Ainda não concluída): ")
    bool(status_task)

    task = {
        "name": task_name,
        "description": description_task,
        "status": status_task
    }
    task_list.append(task)
    print("Tarefa adicionada com sucesso!")

    Tarefas(task_list)
    return

def Complete_Task(task_list):
    clear_screen()
    task_name = input("Nome da Tarefa: ")
    task_found = False

    for task in task_list:
        if task["name"] == task_name:
            task["status"] = True
            task_found = True
            print(f"Tarefa '{task_name}' marcada como concluída.")
            break

    if not task_found:
        print(f"Tarefa '{task_name}' não encontrada.")
    
    Tarefas(task_list)

