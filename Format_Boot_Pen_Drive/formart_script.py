from tool import clear_screen
import os
import tempfile

def formart(nun_disk):
    try:
        # Cria um arquivo temporário para armazenar os comandos do diskpart
        with tempfile.NamedTemporaryFile('w', delete=False) as script_file: # cria umm temp file para execuçao do script 
            script_file.write(f"select disk {nun_disk}\n")
            script_file.write("clean\n")
            script_file.write("create partition primary\n")
            script_file.write("format fs=fat32 quick\n")
            script_file.write("assign\n")
            script_file.write("exit\n")
        
        # Executa o arquivo de script no diskpart
        os.system(f"diskpart /s {script_file.name}")
        
        # Remove o arquivo de script após a execução
        os.remove(script_file.name)
        
        return True
    except:
        return False