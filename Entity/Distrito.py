
class Distrito():
    
    def __init__(self,id_distrito,nombre_distrito,codigo_postal):
        self.__id_distrito = id_distrito
        self.__nombre_distrito = nombre_distrito
        self.__codigo_postal = codigo_postal
        
    def getIdDistrito(self):
        return self.__id_distrito
    def getNombreDistrito(self):
        return self.__nombre_distrito    
    def getCodigoPostal(self):
        return self.__codigo_postal
    
    def setIdDistrito(self,idDistrito):
        self.__id_distrito = idDistrito
    def setNombreDistrito(self,nombre):
        self.__nombre_distrito = nombre
    def setCodigoPostal(self,codigoPostal):
        self.__codigo_postal = codigoPostal
        