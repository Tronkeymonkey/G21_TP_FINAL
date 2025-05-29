from vehiculos.Vehiculos import * 
from typing import override
import random as rnd



class Auto(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        super().__init__(velocidad_viajes, identificador)
           
        
    @override   
    def despachar(self, distancia): 
            """
            Simula el despacho del vehículo (Auto) a una determinada distancia.
            Se genera aleatoriamente un nivel de tráfico entre 0 y 3.
            Se calcula el tiempo de viaje
            El resultado se guarda en el registro de viajes con la distancia, el tráfico y el tiempo total.
            Finalmente, devuelve el tiempo total del viaje.
            """
            nivel_trafico = rnd.randint(0,3)
            if self.velocidad_viajes == 0:
                raise ValueError("La velocidad del vehículo no puede ser cero.")  # Manejo preventivo
            tiempo =  (distancia / self.velocidad_viajes) + nivel_trafico 
            self.registro_viajes.append({
                'distancia': distancia,
                'nivel_trafico': nivel_trafico,
                'tiempo': tiempo
                })
            self.dispoinibilidad == "Disponible"
            return tiempo  