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
        empleado_id = self.txtIdEmpleado.text()
        nombre = self.txtNombre.text()
        paterno = self.txtApellidoPaterno.text()
        materno = self.txtApellidoMaterno.text()
        dni = self.txtDni.text()
        correo = self.txtCorreo.text()
        cargo_id = self.txtIdCargo.text()
    
        if not (empleado_id and nombre and paterno and materno and dni and correo and cargo_id):
            QtWidgets.QMessageBox.warning(self, "Campos Vacíos", "Complete todos los campos.")
            return None
    
        try:
            empleado_id = int(empleado_id)
            dni = int(dni)
            cargo_id = int(cargo_id)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error en Datos", "Ingrese datos numéricos válidos.")
            return None
    
        empleado = Empleado(empleado_id, nombre, paterno, materno, dni, correo, cargo_id)
        return empleado
        
    def registrarEmpleado(self):
        empleado = self.TraerDatos()
        if empleado:
            self.empleadoC.inserta_empleados(empleado)
            QtWidgets.QMessageBox.information(self, "Registro Exitoso", "El empleado ha sido registrado exitosamente.")
            self.limpiar()
        
    def cerrarVentana(self):
        self.close()
        
    def limpiar(self):
        self.txtIdEmpleado.clear()
        self.txtNombre.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDni.clear()
        self.txtCorreo.clear()
        self.txtIdCargo.clear()
