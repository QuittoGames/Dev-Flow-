import platform
import os
from tkinter.filedialog import askdirectory
from data import paths
import ctypes
import sys
import asyncio
from time import sleep

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def Organizador_De_Arquivo():
    #print("pegar pasta")
    path = askdirectory(title="Selecione uma pasta")
    while path == "":
        path = askdirectory(title="Selecione uma pasta")
        
    listpaths = os.listdir(path)
    print(listpaths)

    for arquivo in listpaths:
        nome, extensao = os.path.splitext(arquivo)
        for pasta in paths:
            if extensao in paths[pasta]:
                pasta_path = os.path.join(path, pasta)
                if not os.path.exists(pasta_path):
                    os.mkdir(pasta_path)
                arquivo_antigo = os.path.join(path, arquivo)
                arquivo_novo = os.path.join(pasta_path, arquivo)
                os.rename(arquivo_antigo, arquivo_novo)
    return


def Clear_Temp():
    clear_screen()
    try:
        temp_Diretory = r"C:\Users\sidne\AppData\Local\Temp".strip()
        del temp_Diretory
        print("A Tempo Foi Limpa Com Susseso! ")
        sleep(1.5)
        return
    except MemoryError:
        print("Memory Error")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

    