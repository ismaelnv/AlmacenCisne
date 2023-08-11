
class Categoria():
    
    def __init__(self,id_categoria,nombre):
        self.__id_categoria = id_categoria
        self.__nombre = nombre
        
    def getIdCategoria(self):
        return self.__id_categoria    
    def getNombre(self):
        return self.__nombre
    
    def setIdCategoria(self,idCategoria):
        self.__id_categoria = idCategoria
    def setNombre(self, nombre):
        self.__nombre = nombre    
        