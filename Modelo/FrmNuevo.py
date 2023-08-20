import sys
from PyQt5 import QtWidgets, uic


class Nuevo(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(Nuevo, self).__init__(parent)
        uic.loadUi("Ui/Nuevo.ui",self)
        self.btnRegistrar.clicked.connect(self.registrarUsuario)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        
    def registrarUsuario(self):
        pass
        
    def cerrarVentana(self):
        self.close()