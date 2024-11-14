from tool import tool
import datetime
from time import sleep
from data import data
from IA.IA import Ollaama_Run_IA,Config_IA
import os
from ctypes import windll
import sys
#import asyncio
import platform
from requests import get
from Manege_Progect.mange_project_main import Start_Progect
from Format_Boot_Pen_Drive.formart_script import formart

# Interface
def Start():
    tool.clear_screen()
    print("Bem Vindo Al DevFlow! ")
    print(f"{data.day}/{data.mes}/{data.ano}")
    print(f"Sistema Operacional: {data.OS_client}")
    print("1. Verificar Arquivos Corrompidos (Windows)")
    print("2. Criar Pasta")
    print("3. Organizador De Arquivos")
    print("4. Limpar %Temp%")
    print("5. Lhama 3 IA (Local)")
    print("6. Verificar Resposta De Servidor De Um Site")
    print("7. Mange Progect")
    print("8. Formart Boot Pen Drive")
    print("9. Clone Repo Git Hub")

    command = input("Digite Sua Opção: ")
    if command == "1":
        tool.Windows_Verify()
        return
    elif command == "2":
        tool.Create_Folder()
        Start()
        return
    elif command == "3":
        tool.Organizador_De_Arquivo()
        Start()
        return
    elif command == "4":
        tool.Clear_Temp()
        Start()
        return
    elif command == "5":
        Run_IA()
    elif command == "6":
        tool.Retun_reponse()
        Start()
        return
    elif command == "7":
        Start_Progect()
        return
    elif command == "8":
        Formart_Boot_Disk()
        Start()
        return
    elif command == "9":
        tool.clone_rep()
        sleep(1)
        Start()
        return
    else:
        Start()
        return

def Run_IA():
    tool.clear_screen()
    strat_IA = input("Config IA: (y/n)")
    if strat_IA.lower() == "n":
        Ollaama_Run_IA()
    elif strat_IA.lower() == "y":
        Config_IA()
    Start()
    return

def Formart_Boot_Disk():
    tool.clear_screen()
    nun_disk = input("Digite O Numero Do Seu Pen Drive Botavel: ")
    if formart(nun_disk=nun_disk):
        print("Pen Drive Botavel Formatado Com Susseso!")
        sleep(2)
        Start()
        return
    else:
        print("Erro na Formataçao!")
        sleep(2)
        Start()
        return

if __name__ == "__main__":
    if tool.is_admin():
        Start()  # Executa a função principal se o script tiver privilégios administrativos
    else:
        print("Reiniciando como administrador...")
        try:
            windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        except Exception as e:
            print(f"Erro ao tentar reiniciar como administrador: {e}")
        sleep(1)  # Aguarda um momento para evitar loops rápidos
        sys.exit(0)  # Finaliza o script original para evitar múltiplas instâncias
