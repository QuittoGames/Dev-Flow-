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
import threading
import winotify

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
            if data.OS_client == "Windows":
                os.system("winget install git")
            else:
                os.system("sudo apt install git")
        except Exception as E:
            print(f"Erro Na Innstalaçao Do Git!, Erro: {E}")

        
    def install_ollama():
        try:
            if data.OS_client == "Windows":
                print("Para Execuçao Da Feture IA Local E Ultilizado ferramentas de terceros neste caso sendo a ferramenta 'ollama' mais informaçoes no site 'https://ollama.com/'")
                print("Caso Ja Possua A Ferramete Apenas Presisone Qualquer Tecla")
                license_run = input("Deseja Continuar: (y/n)")
                if license_run.lower().strip() == "y":return
                os.system("winget install ollama")
            else:
                print("Para Execuçao Da Feture IA Local E Ultilizado ferramentas de terceros neste caso sendo a ferramenta 'ollama' mais informaçoes no site 'https://ollama.com/'")
                print("Caso Ja Possua A Ferramete Apenas Presisone Qualquer Tecla")
                license_run = input("Deseja Continuar: (y/n)")
                if license_run.lower().strip() == "y":return
                os.system("sudo apt install ollama")
        except Exception as E:
            print(f"Erro Na Innstalaçao Do ollama!, Erro: {E}")

    def Clear_Temp():
        tool.clear_screen()
        try:
            temp_Diretory = r"C:\Users\USER\AppData\Local\Temp".strip()
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
    
    def verify_modules():
        for i in data.modules:
            os.system(f"pip3 install {i}")
            sleep(0.1)
        return

    def write_in_notes():
        tool.clear_screen()
        try:
            if not os.path.exists("/data_note/note.txt"):
                os.system("cd data_note touch note.txt")
            print(f"Note: {open(data.file_note, "a")}")
            txt = input("Digite Seu Texto: ")
            with open(data.file_note, "a") as file:
                file.write(txt + "\n")
            return
        except Exception as e:
            print(f"Erro ao escrever no arquivo: {e}")

    def start_tread(fuction,parameter):
        if not isinstance(parameter, tuple):
            parameter = (parameter,) 
        tread = threading.Thread(target=fuction,args=parameter)
        tread.daemon = True
        tread.start()
        return tread
    
    def Notification(task: object):
        try:
            if not os.path.exists(r"C:\Users\Admin\Downloads\Projects\Dev-Flow-\icon\coffee.png"):
                print(f"Ícone encontrado: {os.path.exists(r'./icon/coffee.png')}")
                return None

            notification = winotify.Notification(
                app_id="Dev Flow",
                title=task.name_task,
                msg=task.descri_task,
                icon=r"C:\Users\Admin\Downloads\Projects\Dev-Flow-\icon\coffee.png"
            )
            notification.set_audio(winotify.audio.Default, loop=False)
            notification.add_actions(
                label="Abrir Dev Flow",
                launch=r"C:\Users\Public\Downloads\Projects\Dev-Flow-\index.py"
            )
            notification.show()
        except Exception as e:
            print(f"Erro ao exibir a notificação: {e}")
            return None

    
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

        