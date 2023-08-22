import sys
from PyQt5 import QtWidgets, uic
from Modelo.FrmInsumos import Insumos
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QDateTime, QTimer

class VentanaPrincipal(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("Ui/Menu.ui",self)
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 300, 50)
        self.verFechayhora()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.verFechayhora)
        self.timer.start(1000)
        self.btnInsumos.clicked.connect(self.abrirInsumos)
        self.btnCerrar.clicked.connect(self.cerrarSesion)
    
    def verFechayhora(self):
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString('yyyy-MM-dd hh:mm:ss')
        self.lblMostrarfecha.setText(f"Fecha y hora actual: {formatted_datetime}")
    
        
    def abrirInsumos(self):
        vClientes= Insumos(self)
        vClientes.show()
        
    def cerrarSesion(self): 
        self.close()
        