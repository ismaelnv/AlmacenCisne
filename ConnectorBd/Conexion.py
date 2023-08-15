import mysql.connector
from mysql.connector import Error

class Conexion():
    
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(user = 'root', password = '12345678',
                                   host = 'localhost',database = 'el_cisne'
                                   ,port = '3306')
            self.miCursor = self.conexion.cursor()
        except Error as ex: 
            print("Error al intentar conexión".format(ex))
        
    def listarInsumos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM Insumos ORDER BY nombreIns ASC")
                resultado = cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error al intentar conexión".format(ex))
    def insertarInsumos(self):
        self.miCursor.execute("insert into insumos (NombreIns,PrecioIns,StockIns,EstadoIns,IdCategoria) values ('almoadas',28,13,'nuevo',3)")            
        n = self.miCursor.rowcount
        
    insertarInsumos()
    

