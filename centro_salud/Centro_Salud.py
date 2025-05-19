from vehiculos.Helicoptero import *
from vehiculos.Avion import *
from vehiculos.Auto import *
from pacientes.Receptores import Receptores
from cirujanos.Cirujanos import Cirujanos
from pacientes.Donantes import Donantes
from datetime import datetime
from datetime import timedelta

class CentroSalud:
    
    def __init__(self, nombre, direccion, telefono, partido, provincia, Cirujano = [], Vehiculo = [], Donante = []):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos: list[Cirujanos] = Cirujano #lista 
        self.lista_vehiculos: list[Vehiculos] = Vehiculo #lista 
        self.lista_donantes: list[Donantes] = Donante #lista de donantes que depende del nombre del centro
        
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
         
    def derivar_organo(self, organo, donante: Donantes, receptor: Receptores, horario_ablacion: datetime, distancia, nivel_trafico):
            #evita que el codigo se crashee si por ejemplo divido por cero
            vehiculo = self.asignar_vehiculo(receptor, distancia)
            tiempo_viaje = vehiculo.despachar(distancia, nivel_trafico)
            hora_llegada = horario_ablacion + timedelta(hours=tiempo_viaje)
            
            print(f"Órgano '{organo.tipo}' despachado con éxito:")
            print(f"Vehículo asignado: {vehiculo}")
            print(f"Tiempo estimado de viaje: {round(tiempo_viaje, 2)} hs")
            print(f"Llegada estimada al receptor: {hora_llegada.strftime('%H:%M')}")
            
            return tiempo_viaje
            
                
                    
    
'''
if autos:  # Verificar que haya al menos un auto en la lista
        # Encontrar el auto con mayor velocidad usando max y una función lambda
        maximo = max(autos, key=lambda auto: auto.velocidad_viajes)
        return maximo
    else:
        print("No hay autos disponibles en la lista de vehículos.")
'''