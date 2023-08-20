import sys
from PyQt5 import QtWidgets, uic
from Modelo.FrmMenu import VentanaPrincipal
from Modelo.FrmNuevo import Nuevo
from Controller.EmpleadoController import *



qtCreatorFile= "Ui/Login.ui"
Ui_MainWindow, QtBaseClass= uic.loadUiType(qtCreatorFile)

class FormularioLogin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(FormularioLogin,self).__init__()
        uic.loadUi(qtCreatorFile, self)
        self.usuarioBd = EmpleadoController()
        self.btnIngresar.clicked.connect(self.iniciarSesion)
        self.btnSalir.clicked.connect(self.cerrar_ventana)
        self.lnkRegistrarse.clicked.connect(self.nuevoRegistro)
        self.show()
    
    def  validaciones(self):
        usuario =self.txtUsuario.text()
        correo =self.txtPassword.text()
        if usuario == "" and correo == "":
            return "Ingresar Usuario y Contraseña"
        elif usuario == "" and correo == correo:
            return  "Usuario"
        elif usuario == usuario and correo == "":
            return "Contraseña"
        else:
            return "El usuario No esta registrado"
           
    
    def iniciarSesion(self): 
        usuario =self.txtUsuario.text()
        correo =self.txtPassword.text()
        if self.usuarioBd.buscar_empleado(usuario) and self.usuarioBd.buscar_password(correo):
            vprincipal=VentanaPrincipal(self)
            vprincipal.show()
            self.Limpiar()
        else:
             QtWidgets.QMessageBox.information(self,"","ERROR...!!!"+self.validaciones(),
            QtWidgets.QMessageBox.Ok)                 
        
    def nuevoRegistro(self):
        vClientes= Nuevo(self)
        vClientes.show() 
                
    def cerrar_ventana(self):
        self.close() 
        
    def Limpiar(self):
        self.txtUsuario.clear()
        self.txtPassword.clear()         
        

            
