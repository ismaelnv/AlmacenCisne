import sys
from PyQt5 import QtWidgets
from Modelo.Login import FormularioLogin
from ConnectorBd.Conexion import *

if __name__=="__main__":
    #prueba de los metodos 
   # insuo = Insumo(1,"ismael",20,12,'ac',3)
   # bd = Registro_datos()
    #print(bd.traer_datos())
    #print(bd.eliminar_insumos("ismael")) 
    
    
    app=QtWidgets.QApplication(sys.argv)
    window=FormularioLogin()
    app.exec()
    
    