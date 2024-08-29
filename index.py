from tool import clear_screen, Organizador_De_Arquivo,Clear_Temp,is_admin
import datetime
from time import sleep
from data import Diretory_Salved,IA_Byts
from IA.IA import Ollaama_Run_IA,Config_IA
import os
import ctypes
import sys
import asyncio
import platform
from requests import get
from Manege_Progect.mange_project_main import Start_Progect

# Variáveis Globais
ano = datetime.datetime.now().year
mes = datetime.datetime.now().month
day = datetime.datetime.now().day

OS_client = platform.system()

DiretoryBool = False

# Interface
def Start():
    clear_screen()
    print("Bem Vindo Al DevFlow! ")
    print(f"{day}/{mes}/{ano}")
    print(f"Sistema Operacional: {OS_client}")
    print("1. Verificar Arquivos Corrompidos (Windows)")
    print("2. Criar Pasta")
    print("3. Organizador De Arquivos")
    print("4. Limpar %Temp%")
    print("5. Lhama 3 IA (Local)")
    print("6. Verificar Resposta De Servidor De Um Site")
    print("7. Mange Progect")

    command = input("Digite Sua Opção: ")
    if command == "1":
        Windows_Verify()
    elif command == "2":
        Create_Folder()
    elif command == "3":
        Organizador_De_Arquivo()
    elif command == "4":
        Clear_Temp()
        Start()
        return
    elif command == "5":
        Run_IA()
    elif command == "6":
        Retun_reponse()
        return
    elif command == "7":
        Start_Progect()
    else:
        Start()
        return

def Create_Folder():
    global DiretoryBool, Diretory_Salved
    clear_screen()
    name_Folder = input("Digite o Nome da Pasta: ")
    auto_diretory = input("Você deseja utilizar o diretório salvo? (y/n): ")

    if DiretoryBool and auto_diretory.lower() == "y":
        Diretory = Diretory_Salved
    else:
        Diretory = input("Digite seu Diretório: ").strip()
        worder = input("Você deseja adicionar este repositório aos favoritos? (y/n): ")
        if worder.lower() == "y":
            Diretory_Salved = Diretory
            DiretoryBool = True
    
    os.makedirs(os.path.join(Diretory, name_Folder), exist_ok=True)
    Start()
    return
        
def Windows_Verify():
    clear_screen()
    if OS_client == "Windows":
        try:
            os.system("SFC /scannow")
            input("Pressione Enter para continuar...")
            Start()
            return
        except MemoryError:
            print("Erro de Memória")
            Start()
            return
    else:
        print("Sistema Operacional Nao Pode Execultar Esta Funaço ")
        Start()
        return

def Run_IA():
    clear_screen()
    strat_IA = input("Config IA: (y/n)")
    if strat_IA.lower() == "n":
        Ollaama_Run_IA()
    elif strat_IA.lower() == "y":
        Config_IA()
    Start()
    return

def Retun_reponse():
    clear_screen()
    url = input("Digite Sua URL: ").strip()
    reponse = get(url)

    print(f"resposta do server: {reponse}")
    sleep(1)
    Start()
    return

if __name__ == "__main__":
    if is_admin():
        Start()  # Executa a função principal se o script tiver privilégios administrativos
    else:
        print("Reiniciando como administrador...")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        except Exception as e:
            print(f"Erro ao tentar reiniciar como administrador: {e}")
        sleep(1)  # Aguarda um momento para evitar loops rápidos
        sys.exit(0)  # Finaliza o script original para evitar múltiplas instâncias
