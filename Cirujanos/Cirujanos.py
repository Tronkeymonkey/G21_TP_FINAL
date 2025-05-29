import random as rnd
from pacientes.Receptores import Receptores # Importar la clase Receptores desde el archivo Receptores.py de la carpeta pacientes
from organos.Organos import Organos # Importar la clase Organos desde el archivo Organos.py de la carpeta organos
from datetime import datetime
from datetime import timedelta

class Cirujanos:
   
    def __init__(self, especialidad, disponibilidad=None):
        """
        Constructor de la clase Cirujanos.
        Recibe como argumento la especialidad del cirujano 
        La disponibilidad se setea por defecto como 'Disponible'. También se inicializa una tabla de sinergias,
        que define qué especialidades están capacitadas para operar qué órganos.
        """
        self.especialidad = especialidad.lower() 
        self.disponibilidad = "Disponible"

        self.tabla_sinergias = {  "cardiovascular":["corazon"], #esto es un llamado diccionario, donde se definen las compatibilidades entre los organos y las especialidades
                             "pulmonar":["pulmon"],
                             "plastico":["piel","corneas"],
                             "traumatologo":["huesos"],
                             "gastroenterologo":["higado","riñon", "intestinos"]
                               } 
        
    def realizar_cirujia(self, tiempo, organos:Organos = None):
        """
        Simula el proceso de una cirujia y determina el exito de esta. El parametro tiempo es la diferencia entre 
        la hora actual y la hora de ablacion del organo. El parametro organos, es e organo que se desea transplantar.
        
        Si el organo ha pasado  mas de 20hs desde la ablación, la cirujia se cancela automaticamente. Si el organo es compatible con la especialidad
        del cirujano, la probabilidad de exito es mayor, pero si no es compatible, la cirujia puede seguir adelante pero con menor probabilidad de exito.
        La disponibilidad del cirujano se mantiene en "disponible" tras la operacion (ya sea exito o fracaso).
        Devuelve True si la cirujia fue exitosa. False si la cirujia falló. Y muestra un mensaje si el tiempo de ablacion supera las 20hs. 
        """
        tiempo_tardado = tiempo
        
        if tiempo_tardado > 20: 
            print("Cirujia interrupida: TIEMPO DE ABLACION MAYOR A 20 HS") 
        
        elif tiempo_tardado <= 20: 
            
            if organos in self.tabla_sinergias[self.especialidad]: #si el organo que se quiere trasplantar es compatible con la especialidad del cirujano
                exito = rnd.randint(0, 10) #simulamos el exito de la cirujia con un random
                if exito >= 3:
                    self.disponibilidad == "Disponible"
                    return True #salio bien
                else:
                    self.disponibilidad == "Disponible"
                    return False #salio mal

            elif organos not in self.tabla_sinergias[self.especialidad]:
                exito = rnd.randint(0, 10) 
                if exito >= 5:
                    self.disponibilidad == "Disponible"
                    return True
                else:
                    self.disponibilidad == "Disponible"
                    return False