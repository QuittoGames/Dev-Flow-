from tool import tool
from data import data,Auto_Flow_UI
import sys
from time import sleep
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt6.QtGui import QPixmap,QIcon,QFont
from setings import setings
import speech_recognition as sr

app = QApplication(sys.argv)
def Start():
    tool.clear_screen()
    try:
        StartUI = QWidget()
        StartUI.resize(data.resolutionX,data.resolutionY)
        StartUI.setWindowTitle("Auto Flow")
        StartUI.setWindowIcon(QIcon("icon/TerminalLogo.ico"))
        StartUI.setFont(QFont(data.Font))
        StartUI.setStyleSheet("""
        background-color: qlineargradient(
            spread:pad, 
            x1:0, y1:0, 
            x2:1, y2:1, 
            stop:0 rgba(30, 30, 30, 255), 
            stop:0.5 rgba(45, 45, 50, 255), 
            stop:1 rgba(20, 20, 60, 255)
        );
    """)

        
        Title = Auto_Flow_UI.create_text(screm= StartUI,txt = "Auto Flow",x= 170,y= 40)

        SetingsBTN = Auto_Flow_UI.create_btn(screm= StartUI,txt="Setings",X=140,Y=100,L= data.basicBtnLarge, A= data.basicBtnAltura)
        SetingsBTN.clicked.connect(setings)

        exitBTN = Auto_Flow_UI.create_btn(screm=StartUI,txt="Exit",X=140,Y = 200, L= data.basicBtnLarge, A= data.basicBtnAltura)
        exitBTN.clicked.connect(tool.exit_program)
        #exitBTN.show()

        StartUI.show()
    except Exception as E:
        print(f"Erro Al Inicar Interface, Erro: {E}")
        return
    voice_command()
    app.exec()

def voice_command():
    rec = sr.Recognizer()   
    with sr.Microphone(0) as mic:
        tool.clear_screen()
        print("Micrfone Started")
        try:
            while data.Microfone_Open:
                rec.adjust_for_ambient_noise(mic)
                print("Waining Audio ")
                audio = rec.listen(mic)
                command = rec.recognize_google(audio, language=data.languege)
                tool.start_command(command)
                print("Promt: "+ command)
        except Exception as E:
            print(f"Errro No Loop De Aldio, Erro: {E}")
            voice_command()
            return
if __name__ == "__main__":
    #Start() Satrt UI
    voice_command()