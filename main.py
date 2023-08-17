import sys
from PyQt5 import QtWidgets
from Modelo.Login import FormularioLogin
from ConnectorBd.Conexion import *
from Controller.InsumoController import *

if __name__=="__main__": 
    app=QtWidgets.QApplication(sys.argv)
    window=FormularioLogin()
    app.exec()
    
    