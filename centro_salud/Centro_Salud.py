from vehiculos.Helicoptero import *
from vehiculos.Avion import *
from vehiculos.Auto import *
from pacientes.Receptores import Receptores
from cirujanos.Cirujanos import Cirujanos
from pacientes.Donantes import Donantes
from pacientes.Pacientes import Pacientes
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class CentroSalud:
    
    def __init__(self, nombre, direccion, telefono, partido, provincia, lista_cirujanos, lista_vehiculos, lista_pacientes):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos: list[Cirujanos] = [] #lista de cirujanos
        self.lista_vehiculos: list[Auto | Helicoptero | Avion] = [] #lista de los vehiculos
        self.lista_pacientes: list[Receptores | Donantes] = [] #lista de pacientes
        
    def asignar_y_mandar_vehiculo(self, receptores : Receptores , distancia): #Linea cambiada 23/5/2025 15.17
        
        geolocator = Nominatim(user_agent= "mi_app") #identificar la aplicacion

        if receptores.partido != self.partido:
            loc1 = geolocator.geocode(f"{self.partido}, Argentina") #toma el partido del centro
            loc2 = geolocator.geocode(f"{receptores.partido}, Argentina") #toma el partido del receptor
            if loc1 and loc2:
                distancia = geodesic((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).kilometers #calcula la distancia
            for i in self.lista_vehiculos:
                if isinstance(i, Helicoptero): # si pertenece a la clase helicoptero
                    if i.dispoinibilidad == "Disponible":
                        i.dispoinibilidad == "Ocupado"
                        i.despachar(distancia)
                
        elif receptores.provincia != self.provincia:
            loc1 = geolocator.geocode(f"{self.provincia}, Argentina") #toma las provincias de ambos
            loc2 = geolocator.geocode(f"{receptores.provincia}, Argentina")
            if loc1 and loc2:
                distancia = geodesic((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).kilometers #calcula la distancia
            for i in self.lista_vehiculos:
                if isinstance(i,Avion): #si pertenece  a la clase avion
                    if i.dispoinibilidad == "Disponible":
                        i.dispoinibilidad == "Ocupado"
                        i.despachar(distancia)

        elif receptores.partido == self.partido and receptores.provincia == self.provincia: # si no necesito ni avion ni el helicoptero, uso el avion. 
            loc1 = geolocator.geocode(f"{self.partido}, {self.provincia}, Argentina")
            loc2 = geolocator.geocode(f"{receptores.partido}, {receptores.provincia}, Argentina")
            if loc1 and loc2:
                distancia = geodesic((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).kilometers
            for i in self.lista_vehiculos:
                if isinstance(i, Auto): 
                    if i.dispoinibilidad == "Disponible":
                    # Encontrar el auto con mayor velocidad usando max 
                        if self.lista_vehiculos[i].velocidad_viajes > self.lista_vehiculos[i+1].velocidad_viajes:
                            max = i
                    max.dispoinibilidad == "Ocupado"
                    max.despachar(distancia)
                
    def asignar_cirujano_y_operar(self, cirujanos:Cirujanos, receptor: Receptores):
        for cirujanos in self.lista_cirujanos:
            if cirujanos.disponibilidad == "Disponible":
                cirujanos.disponibilidad == "Ocupado"
                cirujanos.realizar_cirujia(receptor.organos_a_disposicion)
            
