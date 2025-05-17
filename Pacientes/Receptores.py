from pacientes.Pacientes import Pacientes

class Receptores(Pacientes):

    def __init__(self, nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud, organo_a_recibir, fecha_en_espera, prioridad, patologia, partido, provincia, estado = None):
      
        super().__init__(nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud)
        self.organo_a_recibir = organo_a_recibir
        self.fecha_en_espera = fecha_en_espera
        self.prioridad = prioridad #que esto dependa de la edad y patologia (obviamente si su estado es inestable es maxima prioridad)
        self.patologia = patologia #que organo necesita
        self.partido = partido.lower()
        self.provincia = provincia.lower()
        self.estado = "Estable" #siempre va a estar estable, a menos que falle el trasplante 
        self.organos_a_disposicion=[] # lista de organos que el receptor puede recibir, en caso de que haya compatibilidad con el donante