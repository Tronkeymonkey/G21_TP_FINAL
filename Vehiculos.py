
class Vehiculos():
    def __init__(self, velocidad_viajes, identificador):
        self.velocidad_viajes = velocidad_viajes
        self.identificador = identificador #El número de patente de una ambulancia. Un nombre de helicóptero ("HELI01", "HELI02") ,Código de un avión de transporte.
        self.registro_viajes = [] #lista donde guardo los datos de cada viaje que hace el vehiculo
        
    def despachar(self, distancia, nivel_trafico=3):
        # se ignora el tráfico (lo manejan las clases hijas)
        tiempo = distancia / self.velocidad_viajes 
        
        self.registro_viajes.append({ #guardo datos en mi lista de registro viajes
            'distancia': distancia,
            'nivel_trafico': nivel_trafico,
            'tiempo': tiempo
        })
        return tiempo
    
    def __str__(self): #metodo magico que ayuda al orden del codigo si quiero imprimirlo: print(vehiculo1) tengo que crear un vehiculo
        return f"Vehículo {self.identificador} - Velocidad: {self.velocidad_viajes} km/h"