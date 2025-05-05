import random as rnd
from Receptores import Receptores # Importar la clase Receptores desde el archivo Receptores.py

class Cirujanos:
   
    def __init__(self, especialidad):
        self.especialidad = especialidad.lower() 

    def sinergias(self, receptores:Receptores):
        organo = receptores.organo_a_recibir.lower()

        tabla_sinergias = {  "cardiovascular":["corazon"],
                             "pulmonar":["pulmon"],
                             "plastico":["piel","corneas"],
                             "traumatologo":["huesos"],
                             "gastroenterologo":["higado","riñon", "intestinos"]
                          } 

    
