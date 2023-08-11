
class Proveedor():
    
    def __init__(self,id_proveedor,nombre,direc_proveedor,ruc_proveedor
    ,telefono_proveedor,correo_proveedor,estado):
        
        self.__id_proveedor = id_proveedor
        self.__nombre = nombre
        self.__direc_proveedor = direc_proveedor
        self.__ruc_proveedor = ruc_proveedor
        self.__telefono_proveedor = telefono_proveedor
        self.__correo_proveedor = correo_proveedor
        self.__estado = estado
        
    def getIdProveedor(self):
        return self.__id_proveedor      
    def getNombre(self):
        return self.__nombre
    def getDirecProveedor(self):
        return self.__direc_proveedor
    def getRucProveedor(self):
        return self.__ruc_proveedor
    def getTelefonoProveedor(self):
        return self.__telefono_proveedor
    def getCorreoProveedor(self):
        return self.__correo_proveedor
    def getEstado(self):
        return self.__estado
    
    
    def setIdProveedor(self,idProveedor):
        self.__id_proveedor = idProveedor   
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setDirecProveedor(self,direcProveedor):
        self.__direc_proveedor = direcProveedor
    def setRucProveedor(self,rucProveedor):
        self.__ruc_proveedor  = rucProveedor
    def setTelefonoProveedor(self,telefonoProveedor):
        self.__telefono_proveedor = telefonoProveedor
    def setCorreoProveedor(self,correoProveedor):
        self.__correo_proveedor = correoProveedor
    def setEstado(self,estado):
        self.__estado = estado
        
        