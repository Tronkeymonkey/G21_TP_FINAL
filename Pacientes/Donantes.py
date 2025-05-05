from Pacientes.Pacientes import *

class Donantes(Pacientes):

    def __init__(self, nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud, fhfallecimiento, fhablacion, partido, provincia):

        super().__init__(nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud)
        self.fhfallecimiento = fhfallecimiento
        self.fhablacion = fhablacion
        self.organos_a_donar = [] #lista (vacia) de los organos a donar
        self.tipo = "Donante"