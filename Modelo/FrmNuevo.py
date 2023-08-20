import sys
from PyQt5 import QtWidgets, uic
from Controller.EmpleadoController import EmpleadoController
from Entity.Empleado import Empleado


class nuevo(QtWidgets.QMainWindow):
    
    def __init__(self,parent=None):
        super(nuevo, self).__init__(parent)
        uic.loadUi("Ui/Nuevo.ui",self)
        self.btnRegistrar.clicked.connect(self.registrarEmpleado)
        self.btnCerrar.clicked.connect(self.cerrarVentana)
        self.empleadoC = EmpleadoController()
        
    def TraerDatos(self):
        empleado = int (self.txtIdEmpleado.text())
        nombre = self.txtNombre.text()
        paterno = self.txtApellidoPaterno.text()
        materno = self.txtApellidoMaterno.text()
        dni = int(self.txtDni.text())
        correo = self.txtCorreo.text()
        Cargo = int(self.txtIdCargo.text())
        empleado = Empleado(empleado,nombre,paterno,materno,dni,correo,Cargo,)
        return empleado
        
    def registrarEmpleado(self):
        self.empleadoC.inserta_empleados(self.TraerDatos())
        
    def cerrarVentana(self):
        self.close()