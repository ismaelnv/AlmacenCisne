from ConnectorBd.Conexion import *
from Entity.Empleado import *

class EmpleadoController():
    def __init__(self):
        bd = Registro_datos()
        self.conexion = bd.conexion
        self.miCursor = bd.miCursor
        empleado = Empleado
        
    def buscar_empleado(self,empleado):
        sql = "SELECT * FROM empleado WHERE NombreEmp = '{}'".format(empleado)
        self.miCursor.execute(sql)
        empleadox = self.miCursor.fetchall()
        return empleadox
    
    def buscar_password(self,correo):
        sql = "SELECT * FROM empleado WHERE CorreoEmp = '{}'".format(correo)
        self.miCursor.execute(sql)
        correox = self.miCursor.fetchall()
        #self.miCursor.close()
        return correox
    
    def inserta_empleados(self,empleado):
        sql = '''INSERT INTO empleado(idEmpleado,NombreEmp,ApellidoPaterno,ApellidoMaterno,DniEmp,CorreoEmp,idCargo)
        VALUES('{}','{}','{}','{}','{}','{}','{}')'''.format(empleado.getIdEmpleado(),empleado.getNombre(),empleado.getApellidoPaterno(),
        empleado.getApellidoMaterno(),empleado.getDniEmpleado(),empleado.getCorreoEmpleado(),empleado.getIdCargo())
        self.miCursor.execute(sql)
        self.conexion.commit()
        self.miCursor.close()
    
    
            
