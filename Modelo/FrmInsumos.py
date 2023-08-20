import sys
from PyQt5 import QtWidgets, uic


class Insumos(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(Insumos, self).__init__(parent)
        uic.loadUi("Ui/Insumos.ui",self)
        self.btnSalir.clicked.connect(self.Salir)
        
    def Salir(self):
        self.close()
        
    def Registrar():
        pass
    
    def Modificar():
        pass
    
    def Eliminar():
        pass
    
    def Limpiar(self):
        self.txtIdusuario.clear()
        self.txtNombre.clear()   
        self.txtPrecio.clear()
        self.txtStock.clear()
        self.txtExistencia.clear()
        self.cboEstado.setCurrentIndex(0)
        self.txtIdcategoria.clear()
    
    