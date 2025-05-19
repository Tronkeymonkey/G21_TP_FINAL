import random as rnd
from pacientes.Receptores import Receptores # Importar la clase Receptores desde el archivo Receptores.py de la carpeta pacientes
from organos.Organos import Organos # Importar la clase Organos desde el archivo Organos.py de la carpeta organos
from centro_salud.Centro_Salud import CentroSalud
from datetime import datetime
from datetime import timedelta

class Cirujanos:
   
    def __init__(self, especialidad):
        self.especialidad = especialidad.lower() 

    def sinergias(self, receptores:Receptores = None):
        self.organo = receptores.organo_a_recibir.lower()

        self.tabla_sinergias = {  "cardiovascular":["corazon"], #esto es un llamado diccionario, donde se definen las compatibilidades entre los organos y las especialidades
                             "pulmonar":["pulmon"],
                             "plastico":["piel","corneas"],
                             "traumatologo":["huesos"],
                             "gastroenterologo":["higado","riñon", "intestinos"]
                               } 
        
    def realizar_cirujia(self, organos:Organos = None):
        
        tiempo_tardado = timedelta(hours = CentroSalud.asignar_vehiculo) 
        
        if tiempo_tardado.datetime.total_seconds() > 20*3600: # esto debe complejizarse agregando la funcion date
            print("Cirujia interrupida: TIEMPO DE ABLACION MAYOR A 20 HS") 
        
        elif horas.total_seconds() <= 20*3600:
            
            if self.organo in self.tabla_sinergias[self.especialidad]: #si el organo que se quiere trasplantar es compatible con la especialidad del cirujano
                exito = rnd.randint(0, 10) #simulamos el exito de la cirujia con un random
                if exito >= 3:
                    return True #salio bien
                else:
                    return False #salio mal

            elif self.organo not in self.tabla_sinergias[self.especialidad]:
                exito = rnd.randint(0, 10) 
                if exito >= 5:
                    return True
                else:
                    return False