import sys
from PyQt5 import QtWidgets, uic
from Entity.Insumo import Insumo
from Controller.InsumoController import InsumoContoller

class Insumos(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(Insumos, self).__init__(parent)
        uic.loadUi("Ui/Insumos.ui",self)
        self.cInsumo = InsumoContoller()
        self.btnSalir.clicked.connect(self.Salir)
        self.btnRegistrar.clicked.connect(self.registrar)
             
    def Salir(self):
        self.close()
        
    def registrar(self):
        self.cInsumo.inserta_insumos(self.traerDatos())
        
    def modificar():
        pass
    
    def eliminar():
        pass
    
    def limpiar(self):
        self.txtIdusuario.clear()
        self.txtNombre.clear()   
        self.txtPrecio.clear()
        self.txtStock.clear()
        self.txtExistencia.clear()
        self.cboEstado.setCurrentIndex(0)
        self.txtIdcategoria.clear()
        
    def traerDatos(self):
        id =   int(self.txtId.text())
        nombre =  self.txtNombre.text()
        precio =  float(self.txtPrecio.text()) 
        stock =  int(self.txtStock.text())
        existencia = self.txtExistencia.text()
        categoria = int(self.txtIdcategoria.text()) 
        estado = self.cboEstado.currentText()
        insumo = Insumo(id,nombre,precio,stock,estado,categoria)
        return insumo
    
    
        
        
    
    