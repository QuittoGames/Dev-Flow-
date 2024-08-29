import os
from tool import clear_screen
from data import IA_Byts,Debug

def Ollaama_Run_IA():
    clear_screen()
    try:
        os.system(f"ollama run llama3.1:{IA_Byts}")
    except:
        print("Nao Foi possuivel Execultar O llama3 , tente intalar o ollama para execuçao do programa")
        return False
    
def Config_IA():
    def IA_Bytes():
        values = ["8","70","405"]
        clear_screen()
        c = input("Digite A Quantidade De Bytes De Para Uso: (Lhama 3: 8B , 70B , 405B (Quanto Mais B Mais Ram Seu Pc Tera Que Usar)): ")
        if c in values:
            c = c[1:] + "b"
            IA_Byts = c
            return 
        else:
            print("Valores Nao Permitidos!")
            return
        

    clear_screen()
    print("1. IA Bytes")
    command = input("Digite Sua Opiçao: ")
    
    if command == "1":
        IA_Bytes()
    elif command == "2":
        Ollaama_Run_IA()

if Debug:
    if __name__ == "__main__":
        Ollaama_Run_IA()