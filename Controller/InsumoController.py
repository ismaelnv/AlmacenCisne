
from ConnectorBd.Conexion import *
from Entity.Insumo import *
from PyQt5 import QtWidgets, uic

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
        try:
            self.miCursor.execute(sql)
            self.conexion.commit()
            QtWidgets.QMessageBox.information(None, "Registro Exitoso", "El insumo ha sido registrado exitosamente.")
        except Error:
            QtWidgets.QMessageBox.warning(None, "Tipo de dato no valido", "ERROR...!!!")   
       
    def traer_insumos(self):
        sql = "SELECT * FROM insumos"
        self.miCursor.execute(sql)
        registroInsumo = self.miCursor.fetchall()
            
        return registroInsumo 
    
    def buscar_insumos(self,id):
        
        sql = "SELECT * FROM insumos WHERE idInsumos = '{}'".format(id)
        try:
            self.miCursor.execute(sql)
            nombreX = self.miCursor.fetchall()
            return nombreX
        except Error:
            QtWidgets.QMessageBox.warning(None, "ERROR...!!!", "Insumo no encontrado")
            
    def eliminar_insumos(self,id):
        sql ="DELETE FROM insumos WHERE idInsumos = '{}'".format(id)
        try:
            self.miCursor.execute(sql)
            self.conexion.commit()
            QtWidgets.QMessageBox.information(None, ":v", "Insumo eliminado")
        except Error:
            QtWidgets.QMessageBox.warning(None, "Error", "ERROR...!!!")    
        
    def ObtenerTamaño(self):
        sql = "SHOW TABLE STATUS LIKE insumos"
        self.miCursor.execute(sql)
        self.conexion.commit()    
        
    def actualizarInsumo(self,insumo,id):
        sql = """
        UPDATE insumos SET idInsumos = '{}', NombreIns = '{}', PrecioIns = '{}', StockIns = '{}', EstadoIns = '{}', idCategoria = '{}'
        WHERE idInsumos = '{}'
        """.format(insumo.getIdInsumo(),insumo.getNombre(), insumo.getPrecioInsumo(), insumo.getStockInsumo(), insumo.getEstado(), insumo.getIdCategoria(), id)
        try:
            self.miCursor.execute(sql)
            self.conexion.commit()
            QtWidgets.QMessageBox.information(None, "Se", "El insumo fue actualizado correctamente")
        except Error:
            QtWidgets.QMessageBox.warning(None, "ERROR", "No se logro actualizar verifique los campos")    
         
            
        
        
        
        
        
    
     
    

    
     
    