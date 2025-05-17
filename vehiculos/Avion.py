from vehiculos.Vehiculos import * 
from typing import override


class Avion(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        super().__init__(velocidad_viajes, identificador) 
     
    @override  #sobreescribo el metodo de mi clase madre
    def despachar(self, distancia, nivel_trafico=3):
        return self._despacho_default(distancia, nivel_trafico) 
       
    