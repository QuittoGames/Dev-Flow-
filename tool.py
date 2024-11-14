import platform
import os
from tkinter.filedialog import askdirectory
from data import data
import ctypes
import sys
import asyncio
from time import sleep
from dataclasses import dataclass
from requests import get
#from Manege_Progect.mange_project_main import Start_Progect
from Format_Boot_Pen_Drive.formart_script import formart


@dataclass
class tool:
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
            for pasta in data.paths:
                if extensao in data.paths[pasta]:
                    pasta_path = os.path.join(path, pasta)
                    if not os.path.exists(pasta_path):
                        os.mkdir(pasta_path)
                    arquivo_antigo = os.path.join(path, arquivo)
                    arquivo_novo = os.path.join(pasta_path, arquivo)
                    os.rename(arquivo_antigo, arquivo_novo)
        return
    
    def install_git():
        try:
            if data.OS == "Windows":
                os.system("winget git")
            else:
                os.system("sudo apt install git")
        except Exception as E:
            print(f"Erro Na Innstalaçao Do Git!, Erro: {E}")


    def Clear_Temp():
        tool.clear_screen()
        try:
            temp_Diretory = r"C:\Users\sidne\AppData\Local\Temp".strip()
            del temp_Diretory
            print("A Tempo Foi Limpa Com Susseso! ")
            sleep(1.5)
            return
        except MemoryError:
            print("Memory Error")

    def Retun_reponse():
        tool.clear_screen()
        url = input("Digite Sua URL: ").strip()
        try:
            reponse = get(url)
        except Exception as e:
            print(f"Erro ao tentar acessar a URL: {url}\n"
            "Possíveis causas:\n"
            "- A URL pode estar incorreta ou malformada.\n"
            "- O site pode estar fora do ar ou com problemas de conexão.\n"
            "- Verifique sua conexão com a internet.\n"
            f"Detalhes técnicos do erro: {e}")
            sleep(5)
            return

        print(f"resposta do server: {reponse}")
        sleep(5)
        return
    
    def Create_Folder():
        global DiretoryBool, Diretory_Salved
        tool.clear_screen()
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
        return
    
    def Formart_Boot_Disk():
        nun_disk = input("Digite O Numero Do Seu Pen Drive Botavel: ")
        if formart(nun_disk=nun_disk):
            print("Pen Drive Botavel Formatado Com Susseso!")
            sleep(2)
            return
        else:
            print("Erro na Formataçao!")
            sleep(2)
            return

    def Windows_Verify():
        tool.clear_screen()
        if data.OS_client == "Windows":
            try:
                os.system("SFC /scannow")
                input("Pressione Enter para continuar...")
                return
            except MemoryError:
                print("Erro de Memória")
                return
        else:
            print("Sistema Operacional Nao Pode Execultar Esta Funaço ")
            return
    

    def clone_rep():
        tool.install_git()
        URL_rep = input("Digite A URL Do Repositorio: ").strip()
        try:
            os.system(f"git clone {URL_rep}")
        except Exception as E:
            return



    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

        