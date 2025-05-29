from vehiculos.Vehiculos import * 
from typing import override


class Avion(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        """
        Inicializa una instancia de Avion con velocidad y un identificador único.
        Hereda los atributos y métodos de la clase base Vehiculos.
        """
        super().__init__(velocidad_viajes, identificador) 
     
    @override  #sobreescribo el metodo de mi clase madre
    def despachar(self, distancia, nivel_trafico=None):
        """
        Sobrescribe el método despachar de la clase Vehiculos.
        El avión no se ve afectado por el tráfico, pero el método conserva el parámetro 'nivel_trafico' por compatibilidad
        (puede ser None o un número que se ignore internamente).
        Se utiliza el método protegido _despacho_default() de la clase base
        para calcular el tiempo y registrar el viaje.
        Actualiza la disponibilidad del vehículo a 'Disponible' y devuelve el tiempo.
        """
        self.dispoinibilidad == "Disponible"
        return self._despacho_default(distancia, nivel_trafico) 
    