from vehiculos.Helicoptero import *
from vehiculos.Avion import *
from vehiculos.Auto import *
class CentroSalud:
    
    def __init__(self, nombre, direccion, telefono, partido, provincia):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos = [] #lista vacia
        self.lista_vehiculos = [] #lista vacia
        
        '''  Los centros de salud asignan un vehiculo para el
transporte del órgano. Esta selección de vehículos se realiza en base a la distancia. Si se encuentra en la
misma provincia y partido, se debe hacer uso del vehiculo disponible de mayor velocidad pero que no se use
para distancias mayores. Si se encuentra en la misma provincia, pero en un partido distinto, se utiliza el
helicóptero. Si discierne la provincia se utiliza el avión.'''
    def asignar_vehiculo(self, partido, provincia, distancia):
        if partido != self.partido:
            for i in self.lista_vehiculos:
                if isinstance(i, Helicoptero): # si pertenece a la clase helicoptero
                    return i
        elif provincia != self.provincia:
            for i in self.lista_vehiculos:
                if isinstance(i,Avion): #si pertenece  a la clase avion
                    return i
        else: # si no necesito ni avion ni el helicoptero, uso el avion. 
            # busco el auto mas rapido 
            auto = [a for a in self.lista_vehiculos if isinstance(a, Auto) and distancia <= 100] # ordeno mi lista en base a los autos 
            # tengo que ordenar los autos en base al tiempo que llevan en recorrer cada uno. 