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
        """
        Constructor de la clase CentroSalud.
        Inicializa un centro de salud con su nombre, dirección, ubicación (partido y provincia), 
        y listas vacías o dadas de cirujanos, vehículos y pacientes. Estas listas se utilizarán para asignar recursos
        en el proceso de trasplantes.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos: list[Cirujanos] = [] #lista de cirujanos
        self.lista_vehiculos: list[Auto | Helicoptero | Avion] = [] #lista de los vehiculos
        self.lista_pacientes: list[Receptores | Donantes] = []
        
    def asignar_pacientes(self, pacientes: list[Receptores | Donantes]):
        """
        Asigna una lista de pacientes (donantes o receptores) al centro de salud.
        Además de agregar los pacientes a la lista interna, actualiza su centro, partido y provincia
        para reflejar que están vinculados con esta institución.
        """
        self.lista_pacientes.extend(pacientes)
        for paciente in pacientes:    
            paciente.centro_de_salud = self
            paciente.partido = self.partido
            paciente.provincia = self.provincia

        
#La logica es que el centro es el del donante

    def asignar_y_mandar_vehiculo(self, receptores : Receptores): 
        """
        Determina qué tipo de vehículo utilizar para transportar un órgano, 
        según la ubicación del receptor comparada con la del centro.
        Si el partido es diferente se usa helicoptero, si la provincia es diferente, usa avión, y si estan en el mismo 
        y provincia usa el auto mas veloz. Marca el vehiculo como "ocupado" y lo despaca con una distancia aleatoria 
        correspondiente al tipo de viaje. 
        """
        
        if receptores.partido != self.partido: #condicion para llamar al helicopter
            distancia = rnd.randint(20,300) #distancia en km
            for i in self.lista_vehiculos:
                if isinstance(i, Helicoptero): # si pertenece a la clase helicoptero
                    if i.disponibilidad == "Disponible":
                        i.disponibilidad == "Ocupado"
                        return i.despachar(distancia)
                
        elif receptores.provincia != self.provincia: #condicion para llamar al avion
            distancia = rnd.randint(300,1700) #distancia en km
            for i in self.lista_vehiculos:
                if isinstance(i,Avion): #si pertenece  a la clase avion
                    if i.disponibilidad == "Disponible":
                        i.disponibilidad == "Ocupado"
                        return i.despachar(distancia)

        elif receptores.partido == self.partido and receptores.provincia == self.provincia: #condicion para llamar al terrestre (y mas veloz)
            distancia = rnd.randint(1,20) #distancia en km
            for i in self.lista_vehiculos:
                if isinstance(i, Auto): 
                    if i.disponibilidad == "Disponible":
                    # Encontrar el auto con mayor velocidad usando max 
                        if i.velocidad_viajes > (i+1).velocidad_viajes:  #HAY QUE CORREGIR EL I+1
                            max = i
                    max.disponibilidad == "Ocupado"
                    return max.despachar(distancia)
                
    def asignar_cirujano_y_operar(self, receptor: Receptores, tiempo):
        """
        Busca un cirujano disponible del centro y le asigna la cirugía del receptor dado.
        Marca al cirujano como "Ocupado" y ejecuta el método `realizar_cirujia` pasándole el tiempo
        desde la ablación y el órgano del receptor.
        """
        for cirujanos in self.lista_cirujanos:
            if cirujanos.disponibilidad == "Disponible":
                cirujanos.disponibilidad == "Ocupado"
                cirujanos.realizar_cirujia(tiempo, receptor.organos_a_disposicion)
            
            
