import sys
from PyQt5 import QtWidgets, uic


class Insumos(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(Insumos, self).__init__(parent)
        uic.loadUi("Ui/Insumos.ui",self)