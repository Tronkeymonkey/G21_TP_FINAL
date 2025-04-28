
class Vehiculos():
    def __init__(self, velocidad_viajes, tipo, identificador):
        self.velocidad_viajes = velocidad_viajes
        self.tipo = tipo #terrestre, helicoptero, avion 
        self.identificador = identificador #El número de patente de una ambulancia. Un nombre de helicóptero ("HELI01", "HELI02") ,Código de un avión de transporte.
        self.registro_viajes = []
        
        
    def despachar(self, distancia, nivel_trafico = 3): #metodfo que sirve para identificar que tipo de despacho debo utilizar. 
        if self.tipo == 'terrestre': 
            tiempo = (distancia / self.velocidad_viajes) + nivel_trafico
        else:
            tiempo = distancia / self.velocidad_viajes  
              
        self.registro_viajes.append({
            'distancia': distancia,
            'nivel_trafico': nivel_trafico,
            'tiempo': tiempo
        })

        return tiempo    
    
    def __str__(self): #metodo magico que ayuda al orden del codigo si quiero imprimirlo: print(vehiculo1) tengo que crear un vehiculo
        return f"Vehiculo {self.identificador} ({self.tipo}) - Velocidad: {self.velocidad} km/h"