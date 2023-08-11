

class Cargo():
    
    def __init__(self,id_cargo,nombre):
        self.__id_cargo = id_cargo
        self.__Nombre_cargo = nombre
        
    def getIdCargo(self):
        return self.__id_cargo
    def getNombreCargo(self):
        return self.__Nombre_cargo
    
    def setIdCargo(self,cargo):
        self.__id_cargo = cargo
    def setNombreCargo(self,Nombre):
        self.__Nombre_cargo = Nombre    
            