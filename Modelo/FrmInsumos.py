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
        self.btnRegistrar.clicked.connect(self.registrarInsumo)
        self.btnBorrar.clicked.connect(self.eliminarInsumo)
        self.btnConsultar.clicked.connect(self.consultarInsumo)
       
             
    def Salir(self):
        self.close()
        
    def registrarInsumo(self):
        self.cInsumo.inserta_insumos(self.traerDatos())
        #self.listar(self.listarDatos())
        
    def consultarInsumo(self):
        obInsumo = self.cInsumo.buscar_insumos(self.traerId())
        self.cargarInsumo(obInsumo)
        
    def modificar():
        pass
    
    def eliminarInsumo(self):
        self.cInsumo.eliminar_insumos(self.traerId())
    
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
        categoria = int(self.txtIdcategoria.text()) 
        estado = self.cboEstado.currentText()
        insumo = Insumo(id,nombre,precio,stock,estado,categoria)
        return insumo
    
    def traerId(self):
        id =  int(self.txtId.text())
        return id
    
    def cargarInsumo(self,obInsumo):
        
        for i in obInsumo:
            self.txtNombre.setText(i[1])
            self.txtPrecio.setText(str(i[2]))
            self.txtStock.setText(str(i[3]))
            self.txtIdcategoria.setText(str(i[5]))
            estado = i[4]
            if estado == "Activo":
                self.cboEstado.setCurrentIndex(1)
            else:
                self.cboEstado.setCurrentIndex(2)
                
    #Falta terminar metodo que carga las tablas
    #def listar(self,insumoList):
        #self.tbDatos.setRowCount(self.cInsumo.ObtenerTamaño())
        #for indice, ancho in enumerate((130,70,70,70,70,70,70)):
            #self.tbDatos.setColumnWidth(indice,ancho)
       # for i in range(len(self):   
           # self.tbDatos.setItem(i,0, QtWidgets.QTableWidgetItem(str(insumoList [i][0]))) 
           # self.tbDatos.setItem(i,1, QtWidgets.QTableWidgetItem(str(insumoList [i][1])))      
           # self.tbDatos.setItem(i,2, QtWidgets.QTableWidgetItem(str(insumoList [i][2]))) 
           # self.tbDatos.setItem(i,3, QtWidgets.QTableWidgetItem(str(insumoList [i][3])))
            #self.tbDatos.setItem(i,4, QtWidgets.QTableWidgetItem(str(insumoList [i][4])))
            #self.tbDatos.setItem(i,5, QtWidgets.QTableWidgetItem(str(insumoList [i][5])))  
    
    def listarDatos (self):
        
        id =   str(self.txtId.text())
        nombre = str(self.txtNombre.text()) 
        precio =  str(self.txtPrecio.text())
        stock =  str(self.txtStock.text())
        existencia = str(self.txtExistencia.text())
        categoria = str(self.txtIdcategoria.text())
        estado = str(self.cboEstado.currentText())
        insumolist = (id,nombre,precio,stock,estado,categoria)
        return insumolist       
            
    
        
        
    
    