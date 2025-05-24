from vehiculos.Vehiculos import * 
from typing import override
import random



class Auto(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        super().__init__(velocidad_viajes, identificador)
           
        
    @override   
    def despachar(self, distancia): 
        # VER COMO HACE EL PRFE CON DIVISION X CERO!!
            nivel_trafico = random.randint(0,3)
            tiempo =  (distancia / self.velocidad_viajes) + nivel_trafico 
            self.registro_viajes.append({
                'distancia': distancia,
                'nivel_trafico': nivel_trafico,
                'tiempo': tiempo
                })
            self.dispoinibilidad == "Disponible"
            return tiempo  