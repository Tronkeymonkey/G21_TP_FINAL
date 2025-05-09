from vehiculos.Vehiculos import *



class Helicoptero(Vehiculos):
    
    
    def __init__(self, velocidad_viajes, identificador):
        super().__init__(velocidad_viajes, identificador) 
        
    # no uso la funcion despachar ya que es la misma que la clase madre 