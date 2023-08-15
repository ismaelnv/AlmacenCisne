import sys
from PyQt5 import QtWidgets, uic


class VentanaPrincipal(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("Ui/Menu.ui",self)