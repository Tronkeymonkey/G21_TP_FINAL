from pacientes.Pacientes import Pacientes
from organos.Organos import Organos

class Receptores(Pacientes):

    def __init__(self, nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud, organo_a_recibir, fecha_en_espera, prioridad, partido, provincia, estado = None):
      
        super().__init__(nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud)
        organo_a_recibir = organo_a_recibir.lower()
        self.organo_a_recibir = organo_a_recibir
        self.fecha_en_espera = fecha_en_espera
        self.prioridad = prioridad #que esto dependa de la edad y patologia (obviamente si su estado es inestable es maxima prioridad)
        partido = partido.lower()
        self.partido = partido
        provincia = provincia.lower()
        self.provincia = provincia
        self.estado = "Estable" #siempre va a estar estable, a menos que falle el trasplante 
        self.organos_a_disposicion: list [Organos] =[] # lista de organos que el receptor puede recibir, en caso de que haya compatibilidad con el donante