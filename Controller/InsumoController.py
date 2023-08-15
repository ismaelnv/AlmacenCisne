
from ConnectorBd.Conexion import Conexion

Bd = Conexion()
class insumoController():
  
    print("aaaa")
    
    def getInsumos(self):
        return Bd.listarInsumos()
    
class prueba(insumoController):   
    
    if __name__=="__main__":
       a = insumoController()
       print(a.getInsumos())

    

    
     
    