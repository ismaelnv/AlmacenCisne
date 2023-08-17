
import mysql.connector
from mysql.connector import Error
from Entity.Insumo import *

class Registro_datos():
    
    
    try:
        conexion = mysql.connector.connect(user = 'root', password = '12345678',
        host = 'localhost',database = 'el_cisne'
        ,port = '3306')
        miCursor = conexion.cursor()
    except Error as ex: 
        print("Error al intentar conexión".format(ex)) 
        
        
        
   
        
            
          
    
    

 