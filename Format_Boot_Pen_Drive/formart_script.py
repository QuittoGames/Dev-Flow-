from tool import clear_screen
from os import system

def formart(nun_disk):
    try:
        system(f"select disk{nun_disk}")
        system("create partition primary")
        system(f"select partition {nun_disk}")
        system("format fs=fat32 quick")
        system("assign")
        system("exit")
        return True
    except:
        return False