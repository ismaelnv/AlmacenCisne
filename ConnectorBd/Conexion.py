import mysql.connector

conexion = mysql.connector.connect(user = 'root', password = '12345678',
                                   host = 'localhost',database = 'el_cisne'
                                   ,port = '3306')
print(conexion)
