from abc import ABC, abstractmethod #uso clase abstracta

class Vehiculos(ABC):
    def __init__(self, velocidad_viajes, identificador):
        self.velocidad_viajes = velocidad_viajes
        self.identificador = identificador #El número de patente de una ambulancia. Un nombre de helicóptero ("HELI01", "HELI02") ,Código de un avión de transporte.
        self.registro_viajes = [] #lista donde guardo los datos de cada viaje que hace el vehiculo
        
    @abstractmethod    
    def despachar(self, distancia, nivel_trafico=3): #abstract method que se implementa o se sobreescribe por las subclases
        pass 
    
    def _despacho_default(self, distancia, nivel_trafico): # creo un metodo protegido por default para avion y helicoptero (reutilizan el comportamiento sin sobreescribir)
        tiempo = distancia / self.velocidad_viajes
        self.registro_viajes.append({
        'distancia': distancia,
        'nivel_trafico': nivel_trafico,
        'tiempo': tiempo
    })
        return tiempo
    
    def __str__(self): #metodo magico que ayuda al orden del codigo si quiero imprimirlo: print(vehiculo1) tengo que crear un vehiculo
        return f"Vehículo {self.identificador} - Velocidad: {self.velocidad_viajes} km/h" 