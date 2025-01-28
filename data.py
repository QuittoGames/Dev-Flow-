import platform
from datetime import datetime
from dataclasses import dataclass

@dataclass
class data:
        paths = {
                "Imagens": [".png", ".jpg"],
                "planilhas": [".xlsx", "cvs"],
                "pdfs": [".pdf"],
                "HTML":[".html"],
                "Texto":[".txt",".docx"]
        }

        Diretory_Saled = ""

        IA_Byts = "70b".lower()

        Projetcs = []

        Debug = False

        # Variáveis Globais
        ano = datetime.now().year
        mes = datetime.now().month
        day = datetime.now().day

        OS_client = platform.system()

        modules = ["PyQt6","requests","winotify"]

        file_note = r"/data_note/note.txt"

        DiretoryBool = False

        Tasks_to_do = []
