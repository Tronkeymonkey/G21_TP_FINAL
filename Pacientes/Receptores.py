from Pacientes.Pacientes import *

class Receptores(Pacientes):

    def __init__(self, nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud, organo_a_recibir, fecha_en_espera, prioridad, patologia, estado = None):
      
        super().__init__(nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud)
        self.organo_a_recibir = organo_a_recibir
        self.fecha_en_espera = fecha_en_espera
        self.prioridad = prioridad #que esto dependa de la edad y patologia (obviamente si su estado es inestable es maxima prioridad)
        self.patologia = patologia #que organo necesita
        self.estado = "Estable" #siempre va a estar estable, a menos que falle el trasplante 
        self.tipo = "Receptor"