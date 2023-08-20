
class Empleado():
    
    def __init__(self,id_empleado,nombre,apellido_paterno,apellido_materno,
    dni_empleado,correo_empleado,id_cargo):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__dni_empleado = dni_empleado
        self.__correo_empleado = correo_empleado
        self.__id_cargo = id_cargo
        #self.__estado = estado
        
    def getIdEmpleado(self):
        return self.__id_empleado
    def getNombre(self):
        return self.__nombre
    def getApellidoPaterno(self):
        return self.__apellido_paterno
    def getApellidoMaterno(self):
        return self.__apellido_materno
    def getDniEmpleado(self):
        return self.__dni_empleado
    def getCorreoEmpleado(self):
        return self.__correo_empleado
    def getIdCargo(self):
        return self.__id_cargo
    def getEstado(self):
        return self.__estado    
    
    def setIdEmpleado(self,empleado):
        self.__id_empleado = empleado
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setApellidoPaterno(self,apellido_paterno):
        self.__apellido_paterno = apellido_paterno
    def setApellidoMaterno(self,apellidoMaterno):
        self.__apellido_materno = apellidoMaterno
    def setDniEmpleado(self,dni):
        self.__dni_empleado = dni
    def setCorreoEmpleado(self,correo):
        self.__correo_empleado = correo
    def setIdCargo(self,idCargo):
        self.__id_cargo = idCargo
    def setEstado(self,estado):
        self.__estado = estado    