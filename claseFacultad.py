from claseCarrera import Carrera
class Facultad:
    __Codigo=0
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=0
    __Carreras=None

    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__Codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__Carreras=[]


    def AgregarCarrera (self,codigo,nombre,fecha,duracion,titulo):
        unaCarrera=Carrera(codigo, nombre, fecha, duracion, titulo)
        self.__Carreras.append(unaCarrera)


    def __str__(self):
        s=("codigo: {}, Nombre: {}, direccion: {}, localidad. {}, telefono: {} \n".format(self.__Codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono))
        for carrera in self.__Carreras:
            s +=str(carrera) +'\n'

        return s
    
    
    def getCodigo(self):
        return self.__Codigo
    
    
    
    def getNombre (self):
        return self.__nombre
    
    
    
    def getLocalidad(self):
        return self.__localidad
    
    
    
    
    def mostrar(self):
        
        for carrera in self.__Carreras:
            carrera.mostrarEjercicio2()
            
            
    def buscarCarrera(self, nom):
        retorno=True
        i=0
        carrera=self.__Carreras[i]
        nombre=carrera.getNombre()
        while(i<(len(self.__Carreras)))and(nombre!=nom):
            i+=1
            carrera=self.__Carreras[i]
            nombre=carrera.getNombre()
            
        if i<(len(self.__Carreras)):
            print("Se encontro la carrera")
            print("El codigo de la carrera es {}{}".format(self.__Codigo,carrera.getCodigo()))
            retorno=False
        return retorno
        
        
        

