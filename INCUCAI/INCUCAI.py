from Pacientes.Receptores import Receptores
from Pacientes.Donantes import Donantes
class INCUCAI:

    def __init__(self):
        self.lista_receptores = [] 
        self.lista_donantes = [] 
    
    def recibir_paciente(self, *pacientes): #por cada paciente recibido, se verifica si es receptor o donante y se agrega a la lista correspondiente
        for paciente in pacientes:
            if isinstance(paciente, Receptores): #verificar si es receptor o donante en base a la clase
                self.lista_receptores.append(paciente)
            elif isinstance(paciente, Donantes):
                self.lista_donantes.append(paciente)
            else:
                raise ValueError("El paciente debe ser un receptor o un donante.")

    def buscar_compatibilidad_receptor_a_donante(self, receptor: Receptores, donante: Donantes):  # Verificar si el órgano que el receptor necesita está en la lista de órganos que el donante puede donar    
        for receptor in self.lista_receptores:
            for donante in self.lista_donantes:
                if receptor.organo_a_recibir.lower() == donante.organos_a_donar.lower() and receptor.Tsangre == donante.Tsangre:
                    return True
