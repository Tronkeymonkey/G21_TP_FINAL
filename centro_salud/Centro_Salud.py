from vehiculos.Helicoptero import *
from vehiculos.Avion import *
from vehiculos.Auto import *
from pacientes.Receptores import Receptores
from cirujanos.Cirujanos import Cirujanos
from pacientes.Donantes import Donantes
from pacientes.Pacientes import Pacientes
import random as rnd 

class CentroSalud:
    
    def __init__(self, nombre, direccion, telefono, partido, provincia, lista_cirujanos = [], lista_vehiculos= [], lista_pacientes= []):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos: list[Cirujanos] = [] #lista de cirujanos
        self.lista_vehiculos: list[Auto | Helicoptero | Avion] = [] #lista de los vehiculos
        self.lista_pacientes: list[Receptores | Donantes] = []
        
    def asignar_pacientes(self, pacientes: list[Receptores | Donantes]):
        
        self.lista_pacientes.extend(pacientes)
        for paciente in pacientes:    
            paciente.centro_de_salud = self
            paciente.partido = self.partido
            paciente.provincia = self.provincia

        
#La logica es que el centro es el del donante

    def asignar_y_mandar_vehiculo(self, receptores : Receptores): 
        
        if receptores.partido != self.partido: #condicion para llamar al helicopter
            distancia = rnd.randint(20,300) #distancia en km
            for i in self.lista_vehiculos:
                if isinstance(i, Helicoptero): # si pertenece a la clase helicoptero
                    if i.dispoinibilidad == "Disponible":
                        i.dispoinibilidad == "Ocupado"
                        return i.despachar(distancia)
                
        elif receptores.provincia != self.provincia: #condicion para llamar al avion
            distancia = rnd.randint(300,1700) #distancia en km
            for i in self.lista_vehiculos:
                if isinstance(i,Avion): #si pertenece  a la clase avion
                    if i.dispoinibilidad == "Disponible":
                        i.dispoinibilidad == "Ocupado"
                        return i.despachar(distancia)

        elif receptores.partido == self.partido and receptores.provincia == self.provincia: #condicion para llamar al terrestre (y mas veloz)
            distancia = rnd.randint(1,20) #distancia en km
            for i in self.lista_vehiculos:
                if isinstance(i, Auto): 
                    if i.dispoinibilidad == "Disponible":
                    # Encontrar el auto con mayor velocidad usando max 
                        if self.lista_vehiculos[i].velocidad_viajes > self.lista_vehiculos[i+1].velocidad_viajes:
                            max = i
                    max.dispoinibilidad == "Ocupado"
                    return max.despachar(distancia)
                
    def asignar_cirujano_y_operar(self, receptor: Receptores, tiempo):
        for cirujanos in self.lista_cirujanos:
            if cirujanos.disponibilidad == "Disponible":
                cirujanos.disponibilidad == "Ocupado"
                cirujanos.realizar_cirujia(tiempo, receptor.organos_a_disposicion)
            
            
