import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
from winotify import Notification
from to_do_tool import to_do_tool
import asyncio


def To_Do_Main():
    tool.clear_screen()
    print("_"*30 + "Dev Flow "+"_"*30)
    print("_"*30 + " To Do "+"_"*30)
    print(f"Tarefas: ")
    to_do_tool.Show_Menu_Task(data.Tasks_to_do)
    print("1. Add Task")
    print("2. Remove Task")
    c = input("Digite Sua Resposta: ").strip().lower()
    if c == "1":
        if to_do_tool.Add_Task() == None:
            To_Do_Main()
            return
        
    elif c == "2":
        if to_do_tool.Remove_Task() == None:
            To_Do_Main()
            return
    else:
        To_Do_Main()
        return


if data.Debug:
    print("Iniciando To_Do_Main...")
To_Do_Main()