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

        Diretory_Salved = ""

        IA_Byts = "70b".lower()

        Projetcs = []

        Debug = False

        # Variáveis Globais
        ano = datetime.now().year
        mes = datetime.now().month
        day = datetime.now().day

        OS_client = platform.system()

        DiretoryBool = False
