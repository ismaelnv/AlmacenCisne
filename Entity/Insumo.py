

class Insumo():
    
    def __init__(self,id_insumo,nombre,precio_insumo,stock_insumo
    ,estado,id_categoria):
        self.__id_insumo = id_insumo 
        self.__nombre = nombre
        self.__precio_insumo = precio_insumo
        self.__stock_insumo = stock_insumo
        self.__id_categoria = id_categoria
        self.__estado = estado
        
    def getIdInsumo(self):
        return  self.__id_insumo
    def getNombre(self):
        return self.__nombre
    def getPrecioInsumo(self):
        return self.__precio_insumo
    def getStockInsumo(self):
        return self.__stock_insumo
    def getExistenciaInsumo(self):
        return self.__existencia_insumo
    def getIdCategoria(self):
        return self.__id_categoria
    def getEstado(self):
        return self.__estado
    
    def setIdInsumo(self,insumo):
        self.__id_insumo = insumo
    def setNombre(self,nombre):
        self.__id_insumo = nombre
    def setPrecioInsumo(self,precio):
        self.__precio_insumo = precio
    def setStockInsumo(self,stock):
        self.__stock_insumo = stock
    def setExistenciaInsumo(self,existencia):
        self.__existencia_insumo = existencia
    def setIdCategoria(self,idCategoria):
        self.__id_categoria = idCategoria
    def setEstado(self,estado):
        self.__estado == estado
    
    
            
        
        
        