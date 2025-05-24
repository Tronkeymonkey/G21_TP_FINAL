import random as rnd
from pacientes.Receptores import Receptores # Importar la clase Receptores desde el archivo Receptores.py de la carpeta pacientes
from organos.Organos import Organos # Importar la clase Organos desde el archivo Organos.py de la carpeta organos
from centro_salud.Centro_Salud import CentroSalud
from datetime import datetime
from datetime import timedelta

class Cirujanos:
   
    def __init__(self, especialidad, disponibilidad=None):
        self.especialidad = especialidad.lower() 
        self.disponibilidad = "Disponible"

        self.tabla_sinergias = {  "cardiovascular":["corazon"], #esto es un llamado diccionario, donde se definen las compatibilidades entre los organos y las especialidades
                             "pulmonar":["pulmon"],
                             "plastico":["piel","corneas"],
                             "traumatologo":["huesos"],
                             "gastroenterologo":["higado","riñon", "intestinos"]
                               } 
        
    def realizar_cirujia(self, organos:Organos = None):
        
        tiempo_tardado = timedelta(hours = CentroSalud.asignar_vehiculo) 
        
        if tiempo_tardado.datetime.total_seconds() > 20*3600: 
            print("Cirujia interrupida: TIEMPO DE ABLACION MAYOR A 20 HS") 
        
        elif tiempo_tardado.datetime.total_seconds() <= 20*3600: 
            
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