from Vehiculos import * 
from typing import override



class Auto(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        super().__init__(velocidad_viajes, identificador)
           
        
    @override   
    def despachar(self, distancia, nivel_trafico):  
        tiempo =  (distancia / self.velocidad_viajes) + nivel_trafico 
        self.registro_viajes.append({
            'distancia': distancia,
            'nivel_trafico': nivel_trafico,
            'tiempo': tiempo
        })
        return tiempo  