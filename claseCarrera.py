class Carrera:
    __codigo=0
    __nombre=""
    __fechaInicio=0
    __Duracion=0
    __Titulo=0



    def __init__ (self,codigo,nombre,fecha,duracion,titulo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__fechaInicio=fecha
        self.__Duracion=duracion
        self.__Titulo=titulo


    def __str__(self):
        return "codigo: {}, nombre: {}, fecha de inicio: {}, duracion: {}, titulo: {}".format(self.__codigo,self.__nombre,self.__fechaInicio,self.__Duracion,self.__Titulo)
    
    
    def mostrarEjercicio2(self):
        print("nombre: {},  Duracion: {}".format(self.__nombre,self.__Duracion))
        
        
        
    def getNombre(self):
        return self.__nombre
    
    
    
    def getCodigo(self):
        return self.__codigo