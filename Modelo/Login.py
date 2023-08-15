import sys
from PyQt5 import QtWidgets, uic
from Modelo.FrmMenu import VentanaPrincipal

qtCreatorFile= "Ui/Login.ui"
Ui_MainWindow, QtBaseClass= uic.loadUiType(qtCreatorFile)

class FormularioLogin(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(FormularioLogin,self).__init__()
        uic.loadUi(qtCreatorFile, self)
        

        self.btnIngresar.clicked.connect(self.iniciarSesion)
        self.show()
    
    def iniciarSesion(self): 
        usuario=self.txtUsuario.text()
        contraseña=self.txtPassword.text()
        if usuario =="admin" and contraseña=="admin":
            self.close()
            vprincipal=VentanaPrincipal(self)
            vprincipal.show()
        

            
