
from ConnectorBd.Conexion import *
from Entity.Insumo import *

class InsumoContoller():
    
    def __init__(self):
        
        bd = Registro_datos()
        self.conexion = bd.conexion
        self.miCursor =  bd.miCursor
        insumo = Insumo
    
    
    def inserta_insumos(self,insumo):
        sql = '''INSERT INTO insumos(idInsumos,NombreIns,PrecioIns,StockIns,EstadoIns,idCategoria)
        VALUES('{}','{}','{}','{}','{}','{}')'''.format(insumo.getIdInsumo(),insumo.getNombre(),insumo.getPrecioInsumo(),
        insumo.getStockInsumo(),insumo.getEstado(),insumo.getIdCategoria())
        self.miCursor.execute(sql)
        self.conexion.commit()
        self.miCursor.close()
       
    def traer_insumos(self):
        sql = "SELECT * FROM insumos"
        self.miCursor.execute(sql)
        registroInsumo = self.miCursor.fetchall()
        return registroInsumo  
    
    def buscar_insumos(self,nombre):
        sql = "SELECT * FROM insumos WHERE NombreIns = '{}'".format(nombre)
        self.miCursor.execute(sql)
        nombreX = self.miCursor.fetchall()
        self.miCursor.close()
        return nombreX
    
    def eliminar_insumos(self,nombre):
        sql ="DELETE FROM insumos WHERE NombreIns = '{}'".format(nombre)
        self.miCursor.execute(sql)
        self.conexion.commit()
        self.miCursor.close()
        
     #def ingreso_usuario(self,usuario,contraseña):
        #sql = "SELECT * FROM empleado WHERE idEmpleado '{}'".format(usuario)   
        #sql1 = "SELECT * FROM empleado WHERE CorreoEmp '{}'".format(contraseña)
        #self.miCursor.execute(sql,sql1)
        #self.miCursor.close()
         
            
        
        
        
        
        
    
     
    

    
     
    