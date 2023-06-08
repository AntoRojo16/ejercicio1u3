import csv
from claseFacultad import Facultad
class ManejadorFacultad:
    __facultades=[]


    def ___init__(self):
        self.__facultades=[]

    def agregarFacultad(self,facultad):
        self.__facultades.append(facultad)
    

    def CargarArchivo(self):
        archivo=open("facultades.csv")
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            if len(fila)==5:
                codigo=fila[0]
                nombre=fila[1]
                direccion=fila[2]
                localidad=fila[3]
                telefono=fila[4]
                unaFacultad=Facultad(codigo, nombre, direccion, localidad, telefono)
                self.agregarFacultad(unaFacultad)
            else:
                codigoF=fila[0]
                codigo=fila[1]
                nombre=fila[2]
                fecha=fila[3]
                duracion=fila[4]
                titulo=fila[5]
                self.__facultades[int(codigoF)-1].AgregarCarrera(codigo,nombre,fecha,duracion,titulo)

        archivo.close()



    def mostrar(self):

        for facultad in self.__facultades:
            print(facultad)
            
            
    def buscarCarrera(self):
        codigo=input("Ingrese el codigo la facultad")
        i=0
        facultad=self.__facultades[i]
        cod=facultad.getCodigo()
        
        while(i<len(self.__facultades))and(cod!=codigo):
            i+=1
            facultad=self.__facultades[i]
            cod=facultad.getCodigo()
            
        if i<len(self.__facultades):
            print("se encontro la facultad")
            print("La facultad es: {}".format(facultad.getNombre()))
            print(facultad.mostrar())
            
            
            
    def ejercicio2(self):
        carrera=input("Ingrese el nombre de la carrera ")
        i=0
        facultad=self.__facultades[i]
        band=True
        
        while(band==True)and(i<len(self.__facultades)):
            i+=1
            facultad=self.__facultades[i]
            band=facultad.buscarCarrera(carrera)
        if band==False:
            print("La se encuentra en: {} \nSu localidad es: {}".format(facultad.getNombre(),facultad.getLocalidad()))
            
            
            
            

