from pacientes.Receptores import Receptores
from pacientes.Donantes import Donantes
from cirujanos.Cirujanos import Cirujanos
from organos.Organos import Organos
from datetime import datetime
class INCUCAI:

    def __init__(self):
        self.lista_receptores: list[Receptores] = [] #listas para almacenar los receptores y donantes (vacias) 
        self.lista_donantes: list[Donantes] = [] 
    
    def recibir_paciente(self, *pacientes): #por cada paciente recibido, se verifica si es receptor o donante y se agrega a la lista correspondiente
        for paciente in pacientes:
            if isinstance(paciente, Receptores): #verificar si es receptor o donante en base a la clase
                self.lista_receptores.append(paciente)
                self.buscar_compatibilidad_receptor_a_donante(paciente, self.lista_donantes) #busco compatibilidad entre el receptor y los donantes

            elif isinstance(paciente, Donantes):
                self.lista_donantes.append(paciente)
                self.buscar_compatibilidad_donante_a_receptor(paciente, self.lista_receptores) #busco compatibilidad entre el donante y los receptores
            
            else:
                raise ValueError("El paciente debe ser un receptor o un donante.")

    def buscar_compatibilidad_receptor_a_donante(self, receptor: Receptores, donante: Donantes):  # Verificar si el órgano que el receptor necesita está en la lista de órganos que el donante puede donar    
        for receptor in self.lista_receptores:
            if receptor.estado.lower() == "inestable": #primero verifico si el receptor esta inestable para darle prioridad al trasplante
                for donante in self.lista_donantes:
                    if receptor.organo_a_recibir == donante.organos_a_donar and receptor.Tsangre == donante.Tsangre:
                        for i in range(len(donante.organos_a_donar)): #entro a la lista de organos a donar del donante
                            donante.organos_a_donar[i].fecha_ablacion = datetime.now() #seteamos la fecha de ablacion del organo en "0"
                            receptor.organos_a_disposicion.append(donante.organos_a_donar)  #coloco el organo del donante en la lista de organos a disposicion del receptor
                            donante.organos_a_donar.remove(donante.organos_a_donar) #el donante no puede donar el organo que ya dono

            elif receptor.estado.lower() == "estable": #misma logica que el anterior, pero para los receptores estables
                for donante in self.lista_donantes:
                    if receptor.organo_a_recibir == donante.organos_a_donar and receptor.Tsangre == donante.Tsangre:
                        for i in range(len(donante.organos_a_donar)):
                            donante.organos_a_donar[i].fecha_ablacion = datetime.now() 
                            receptor.organos_a_disposicion.append(donante.organos_a_donar)  
                            donante.organos_a_donar.remove(donante.organos_a_donar) 

    def buscar_compatibilidad_donante_a_receptor(self, donante: Donantes, receptor: Receptores): #verifico si el donante es compatible con el receptor
        for donante in self.lista_donantes: #logica exactamente igual a la del receptor, pero sin incluir la prioridad del estado
            for receptor in self.lista_receptores:
                if donante.organos_a_donar == receptor.organo_a_recibir and donante.Tsangre == receptor.Tsangre:
                    for i in range(len(donante.organos_a_donar)):
                        donante.organos_a_donar[i].fecha_ablacion = datetime.now()
                        receptor.organos_a_disposicion.append(donante.organos_a_donar)                   
                        donante.organos_a_donar.remove(donante.organos_a_donar)
                    if donante.organos_a_donar == []: 
                        self.lista_donantes.remove(donante) #si el donante se queda sin organos, se va de la lista de donantes

    def resultados_trasplante(self, receptor: Receptores):
        if Cirujanos.realizar_cirujia:
            self.lista_receptores.remove(receptor)
            return f"La cirujia fue todo un exito y el paciente {receptor.nombre} pasa a estado {receptor.estado}. Se ha quitado de la lista de espera."
        else:
            receptor.estado == "Inestable"
            return f"La cirujia ha fallado y el paciente {receptor.nombre} pasa a estado {receptor.estado}. Se le ha puesto la maxima prioridad en la lista de espera."
