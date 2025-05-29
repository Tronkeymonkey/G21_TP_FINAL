from abc import ABC, abstractmethod #uso clase abstracta

class Vehiculos(ABC):
    def __init__(self, velocidad_viajes, identificador):
        """
        Constructor de la clase base abstracta Vehiculos.

        Almacena la velocidad de viaje del vehículo y su identificador único (como la patente de una ambulancia,
        nombre de helicóptero o código de avión). También inicializa una lista para registrar los viajes realizados 
        y establece la disponibilidad inicial del vehículo como 'Disponible'.
        """
        self.velocidad_viajes = velocidad_viajes
        self.identificador = identificador #El número de patente de una ambulancia. Un nombre de helicóptero ("HELI01", "HELI02") ,Código de un avión de transporte.
        self.registro_viajes = [] #lista donde guardo los datos de cada viaje que hace el vehiculo
        self.disponibilidad = "Disponible"
        
    @abstractmethod    
    def despachar(self, distancia, nivel_trafico=3): #abstract method que se implementa o se sobreescribe por las subclases
        """
        Método abstracto que debe ser implementado por todas las subclases.
        Este método se encarga de calcular y registrar el tiempo de viaje de un vehículo a cierta distancia. 
        Las subclases como Auto, Avion y Helicoptero deberán sobrescribir este método para definir su comportamiento específico.
        """
        pass 
    
    def _despacho_default(self, distancia, nivel_trafico): # creo un metodo protegido por default para avion y helicoptero (reutilizan el comportamiento sin sobreescribir)
        """
        Método protegido que implementa un comportamiento común de despacho para Avion y Helicoptero.
        Calcula el tiempo de viaje como distancia dividida por la velocidad del vehículo. 
        Luego, guarda un registro con los datos del viaje (distancia, tráfico, tiempo estimado) 
        y lo retorna.
        Este método permite evitar duplicación de código en subclases que comparten la misma lógica.
        """
        tiempo = distancia / self.velocidad_viajes
        self.registro_viajes.append({
        'distancia': distancia,
        'nivel_trafico': nivel_trafico,
        'tiempo': tiempo
    })
        return tiempo
    
    def __str__(self): #metodo magico que ayuda al orden del codigo si quiero imprimirlo: print(vehiculo1) tengo que crear un vehiculo
        """
        Método mágico que devuelve una representación legible del vehículo.
        Sirve para imprimir objetos de esta clase de forma clara usando `print(vehiculo)`. 
        Retorna un string con el identificador y la velocidad del vehículo.
        """
        return f"Vehículo {self.identificador} - Velocidad: {self.velocidad_viajes} km/h" 