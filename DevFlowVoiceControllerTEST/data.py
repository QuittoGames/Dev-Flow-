from dataclasses import dataclass
from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt6.QtGui import QPixmap,QIcon,QFont
import os

@dataclass
class data:
    resolutionX = 500
    resolutionY = 500
    basicBtnLarge = 200
    basicBtnAltura = 35
    Font = r"fonts\\Font.ttf".strip()
    Microfone_List_reported = []
    Microfone_Open = True
    languege = "pt-BR"

class Auto_Flow_UI():
        def create_btn(screm, txt, X, Y, A, L):
                BTN = QPushButton(txt, screm)
                BTN.setGeometry(X, Y, L, A)
                BTN.setStyleSheet("""
                        QPushButton {
                        background-color: qlineargradient(
                                spread:pad,
                                x1:0, y1:0,
                                x2:1, y2:1,
                                stop:0 #0078D4,           /* Azul padrão gradiente */
                                stop:1 #005A9E            /* Azul mais escuro gradiente */
                        );
                        color: white;
                        border-radius: 10px;            /* Bordas arredondadas */
                        padding: 10px 15px;             /* Espessura interna */
                        font-size: 18px;                /* Tamanho da fonte */
                        font-weight: bold;              /* Negrito */
                        border: 2px solid #005A9E;      /* Azul mais escuro */
                        }
                        QPushButton:hover {
                        background-color: #005A9E;      /* Azul mais escuro no hover */
                        color: #FFFFFF;                 /* Texto branco */
                        font-size: 20px;                /* Aumenta a fonte ao passar o mouse */
                        }
                        QPushButton:pressed {
                        background-color: #004578;      /* Azul ainda mais escuro ao clicar */
                        color: #D1E8FF;                 /* Texto mais claro */
                        font-size: 18px;
                        }
                """)
                return BTN

        def create_text(screm,txt,x,y):
                Title = QLabel("Auto Flow",screm)
                Title.move(x,y)
                #Title.setFont(data.Font)
                Title.setStyleSheet("""
                QLabel {
                color: #000000;
                font-size: 24px;                /* Tamanho da fonte */
                font-weight: bold;              /* Fonte em negrito */
                border: none;                   /* Sem bordas */
                background-color: transparent;  /* Fundo transparente */
                padding: 10px;                  /* Espessura interna para espaçamento */
                }
        """)
                return Title

        def create_window(resX,resY,Logo_path):
                Window = QWidget()
                Window.resize(resX,resY)
                Window.setWindowTitle("Auto Flow")
                Window.setWindowIcon(QIcon(Logo_path))
                Window.setFont(QFont(data.Font))
                return Window