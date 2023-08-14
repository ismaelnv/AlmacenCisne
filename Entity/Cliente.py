
class Cliente():
    
    def __init__(self,id_cliente,nombre_cliente,apellido_paterno,apellido_materno
    ,dni_cliente,genero_cliente,direccion_cliente,telefono_cliente,correo_cliente
    ,id_distrito,estado):
       self.__id_cliente = id_cliente
       self.__nombre_cliente = nombre_cliente
       self.__apellido_paterno = apellido_paterno
       self.__apellido_materno = apellido_materno
       self.__dni_cliente = dni_cliente
       self.__genero_cliente =genero_cliente
       self.__direccion_cliente = direccion_cliente
       self.__telefono_cliente = telefono_cliente
       self.__correo_cliente = correo_cliente
       self.__id_distrito = id_distrito
       self.__estado = estado
       
    def getIdCliente(self):
        return self.__id_cliente
    def getNombreCliente(self):
        return self.__nombre_cliente
    def getApellidoPaterno(self):
        return self.__apellido_paterno
    def getApellidoMaterno(self):
        return self.__apellido_materno
    def getDniCliente(self):
        return self.__dni_cliente
    def getGeneroCliente(self):
        return self.__genero_cliente
    def getDireccionCliente(self):
        return self.__direccion_cliente   
    def getTelefonoCliente(self):
        return self.__telefono_cliente
    def getCorreoCliente(self):
        return self.__correo_cliente
    def getIdDistrito(self):
        return self.__id_distrito
    def getEstado(self):
        return self.__estado
    
    def setIdCliente(self,idCliente):
        self.__id_cliente = idCliente
    def setNombreCliente(self,nombreC):
        self.__nombre_cliente = nombreC
    def setApellidoPaterno(self,apellido):
        self.__apellido_paterno = apellido
    def setApellidoMaterno(self,apellidoM):
        self.__apellido_materno = apellidoM
    def setDniCliente(self,dni):
        self.__dni_cliente = dni
    def setGeneroCliente(self,genero):
        self.__genero_cliente = genero
    def setDireccionCliente(self,direccion):
        self.__direccion_cliente = direccion 
    def setTelefonoCliente(self,telefono):
        self.__telefono_cliente = telefono
    def setCorreoCliente(self,correo):
        self.__correo_cliente = correo
    def setIdDistrito(self,distrito):
        self.__id_distrito = distrito
    def setEstado(self,estado):
        self.__estado = estado
    