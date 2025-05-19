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
                autos = [i for i in self.lista_vehiculos if isinstance(i, Auto)] #busco en mi lista vehiculos cuales son autos
                if autos:  # Encontrar el auto con mayor velocidad usando max y una función lambda
                    max_veloz_auto = max(autos, key=lambda a: a.velocidad_viajes)
                    return max_veloz_auto
        raise Exception("No hay vehículo disponible para este traslado")       
                    
    
'''
if autos:  # Verificar que haya al menos un auto en la lista
        # Encontrar el auto con mayor velocidad usando max y una función lambda
        maximo = max(autos, key=lambda auto: auto.velocidad_viajes)
        return maximo
    else:
        print("No hay autos disponibles en la lista de vehículos.")
'''