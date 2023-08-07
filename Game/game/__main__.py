import typing
import sys
from PyQt5 import QtCore
from .gui.inicio import Ui_Game
from .gui.principal import Ui_Game_principal
from .gui.final import Ui_Final
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QLabel, QWidget
from PyQt5.QtCore import QRect, QPropertyAnimation, QParallelAnimationGroup, Qt, QEasingCurve
from PyQt5.QtGui import QMovie
import random

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ventana_game = None
        
        self.inicializarGui()
    
    def inicializarGui(self):
        self.ui = Ui_Game()
        self.ui.setupUi(self)
        
        self.ui.btn_cerrar.clicked.connect(self.close)
        self.ui.btn_iniciar.clicked.connect(self.game)
        
        self.animacion_lbl = QPropertyAnimation(self.ui.lbl_game, b"geometry")
        self.animacion_lbl.setDuration(500)
        self.animacion_lbl.setStartValue(QRect(130, 0, 111, 111))
        self.animacion_lbl.setEndValue(QRect(130, 60, 111, 111))

        self.animacion_btn = QPropertyAnimation(self.ui.btn_iniciar, b"geometry")
        self.animacion_btn.setDuration(500)
        self.animacion_btn.setStartValue(QRect(130, 270, 111, 111))
        self.animacion_btn.setEndValue(QRect(130, 170, 111, 61))
        
        self.grupo_animacion = QParallelAnimationGroup()
        self.grupo_animacion.addAnimation(self.animacion_lbl)
        self.grupo_animacion.addAnimation(self.animacion_btn)

        self.grupo_animacion.start()
        
        self.show()
        
    def game(self):
        self.ventana_game = Principal()
        self.close()
        self.ventana_game.show()
    
class Principal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ventana_si = None
        self.inicializarGui()
        
    def inicializarGui(self):
        self.ui = Ui_Game_principal()
        self.ui.setupUi(self)
        
        self.x_start, self.y_start = 360, 330
        
        self.ui.btn_cerrar.clicked.connect(self.close)
        
        self.animacion_lbl = QPropertyAnimation(self.ui.lbl_pregunta, b"geometry")
        self.animacion_lbl.setDuration(500)
        self.animacion_lbl.setStartValue(QRect(130, 0, 371, 41))
        self.animacion_lbl.setEndValue(QRect(130, 130, 371, 41))
        
        self.grupo_animacion = QParallelAnimationGroup()
        self.grupo_animacion.addAnimation(self.animacion_lbl)

        self.grupo_animacion.start()
        
        self.ui.btn_no.clicked.connect(self.mover)
        self.ui.btn_si.clicked.connect(self.respuesta_si)
        
    def mover(self):
        self.animacion_btn = QPropertyAnimation(self.ui.btn_no, b"geometry")
        self.animacion_btn.setDuration(20)
        self.animacion_btn.setStartValue(QRect(self.x_start, self.y_start, 155, 42))
        while True:
            self.x_final = random.randint(0, 600)
            self.y_final = random.randint(0, 430)
            
            if self.x_final > self.x_start:
                diferencia_1 = self.x_final - self.x_start
            else:
                diferencia_1 = self.x_start - self.x_final
                
            if self.y_final > self.y_start:
                diferencia_2 = self.y_final - self.y_start
            
            else:
                diferencia_2 = self.y_start - self.y_final
                
            if diferencia_1 > 70 and diferencia_2 > 30:
                break
            
        self.animacion_btn.setEndValue(QRect(self.x_final, self.y_final, 155, 42))
        self.animacion_btn.start()
        
        
        self.x_start, self.y_start = self.x_final, self.y_final

    def respuesta_si(self):
        self.ventana_si = Final()
        self.close()
        self.ventana_si.show()
    
class Final(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.inicializarGui()
        
    def inicializarGui(self):
        self.ui = Ui_Final()
        self.ui.setupUi(self)
        self.ui.btn_cerrar.clicked.connect(self.close)
        
        
        

def main():
    app = QApplication(sys.argv)
    ventana = Game()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()