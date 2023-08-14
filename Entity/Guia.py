
class Guia():
    
    def __init__(self,id_guia,direc_entrega,tipo_remision,estado_guia,id_empleado
    ,fec_entrega,pto_partida,id_proveedor,id_cliente):             
        self.__id_guia = id_guia
        self.__direc_entrega = direc_entrega
        self.__tipo_remision = tipo_remision
        self.__estado_guia = estado_guia
        self.__id_empleado = id_empleado
        self.__fec_entrega = fec_entrega
        self.__pto_partida = pto_partida
        self.__id_proveedor = id_proveedor
        self.__id_cliente = id_cliente
        
    def getIdGuia(self):
        return self.__id_guia
    def getDirecEntrega(self):
        return self.__direc_entrega
    def getTipoRemision(self):
        return self.__tipo_remision
    def getEstadoGuia(self):
        return self.__estado_guia
    def getIdEmpleado(self):
        return self.__id_empleado
    def getFecEntrega(self):
        return self.__fec_entrega
    def getPtoPartida(self):
        return self.__pto_partida
    def getIdProveedor(self):
        return self.__id_proveedor
    def getIdCliente(self):
        return self.__id_cliente 
    
    def setIdGuia(self,idGuia):
        self.__id_guia = idGuia
    def setDirecEntrega(self,direcEntrega):
        self.__direc_entrega = direcEntrega
    def setTipoRemision(self,tRemision):
        self.__tipo_remision = tRemision
    def setEstadoGuia(self,estado):
        self.__estado_guia = estado
    def setIdEmpleado(self,idEmpleado):
        self.__id_empleado = idEmpleado
    def setFecEntrega(self,fecEntrega):
        self.__fec_entrega = fecEntrega
    def setPtoPartida(self,partida):
        self.__pto_partida = partida
    def setIdProveedor(self,idProveedor):
        self.__id_proveedor = idProveedor
    def setIdCliente(self,idCliente):
        self.__id_cliente = idCliente 