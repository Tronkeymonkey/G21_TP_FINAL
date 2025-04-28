from Receptores import *
from Donantes import *
class INCUCAI:

    def __init__(self):
        self.lista_receptores = []
        self.lista_donantes = [] 

    def recibir_paciente(self, *pacientes):
        for paciente in pacientes:
            if isinstance(paciente, Receptores): #verificar si es receptor o donante en base a la clase
                self.lista_receptores.append(paciente)
            elif isinstance(paciente, Donantes):
                self.lista_donantes.append(paciente)
            else:
                raise ValueError("El paciente debe ser un receptor o un donante.")