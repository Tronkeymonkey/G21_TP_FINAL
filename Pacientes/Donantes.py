from pacientes.Pacientes import Pacientes
from datetime import datetime
from organos.Organos import Organos
class Donantes(Pacientes):

    def __init__(self, nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud, fhfallecimiento, organos_a_donar, fhablacion = None):

        super().__init__(nombre, DNI, sexo, nacimiento, Tsangre, telefono, centro_de_salud)
        self.fhfallecimiento = fhfallecimiento
        self.fhablacion = fhablacion # lo dejo sin valor inicial (none) hasta que se haga la ablacion 
        self.organos_a_donar: list[Organos] = [] #lista (vacia) de los organos a donar