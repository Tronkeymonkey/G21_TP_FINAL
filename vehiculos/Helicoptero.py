from vehiculos.Vehiculos import *
from typing import override


class Helicoptero(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        """
        Inicializa una instancia de Helicoptero con su velocidad de viaje
        y un identificador único. Hereda los atributos y comportamientos de Vehiculos.
        """
        super().__init__(velocidad_viajes, identificador) 
        
    @override
    def despachar(self, distancia, nivel_trafico=None):
        """
        Método que sobrescribe el 'despachar' de la clase base Vehiculos.
        Simula el envío de un helicóptero a una cierta distancia. Al igual que con los aviones,
        el tráfico no afecta al helicóptero, pero el parámetro 'nivel_trafico' se incluye por compatibilidad.
        El método interno _despacho_default() se encarga de calcular el tiempo del viaje,
        registrar la información en el historial y retornar el tiempo total.
        Además, actualiza el estado de disponibilidad del helicóptero a 'Disponible'.
        """
        self.dispoinibilidad == "Disponible"
        return self._despacho_default(distancia, nivel_trafico) #metodo protegido default para helicpotero  
        
    