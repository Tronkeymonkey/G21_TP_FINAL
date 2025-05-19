from vehiculos.Helicoptero import *
from vehiculos.Avion import *
from vehiculos.Auto import *
from pacientes.Receptores import Receptores
from cirujanos.Cirujanos import Cirujanos
from pacientes.Donantes import Donantes

class CentroSalud:
    
    def __init__(self, nombre, direccion, telefono, partido, provincia):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos: list[Cirujanos] = [] #lista vacia
        self.lista_vehiculos: list[Vehiculos] = [] #lista 
        self.lista_donantes: list[Donantes] = [] #lista de donantes que depende del nombre del centro
        
    def asignar_vehiculo(self, receptores : Receptores , distancia):
        if receptores.partido != self.partido:
            for i in self.lista_vehiculos:
                if isinstance(i, Helicoptero): # si pertenece a la clase helicoptero
                    return i
        elif receptores.provincia != self.provincia:
            for i in self.lista_vehiculos:
                if isinstance(i,Avion): #si pertenece  a la clase avion
                    return i
        elif receptores.partido == self.partido and receptores.provincia == self.provincia: # si no necesito ni avion ni el helicoptero, uso el avion. 
            if isinstance(self.lista_vehiculos, Auto): 
                    # Encontrar el auto con mayor velocidad usando max y una función lambda
                    maximo = max(self.lista_vehiculos, key=lambda Auto: self.lista_vehiculos.velocidad_viajes)
                    return maximo
                