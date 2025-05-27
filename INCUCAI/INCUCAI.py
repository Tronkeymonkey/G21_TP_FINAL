from pacientes.Receptores import Receptores
from pacientes.Donantes import Donantes
from cirujanos.Cirujanos import Cirujanos
from centro_salud.Centro_Salud import CentroSalud
from organos.Organos import Organos
from datetime import datetime
class INCUCAI:

    def __init__(self, centros = [], donantes = [], receptores = []):
        self.lista_receptores: list[Receptores] = receptores #listas para almacenar los receptores y donantes (vacias) 
        self.lista_donantes: list[Donantes] = donantes
        self.centros_salud: list[CentroSalud] = centros
    
    def recibir_Centros_Salud(self, Centro_Salud:list[CentroSalud]): #FUNCION QUE RECIBE TODAS LAS FUNCIONES, APROVECHANDO QUE RECIBE A LOS CENTROS DE SALUD COMO ARGUMENTO
        self.centros_salud = Centro_Salud

        for i in self.centros_salud: #por cada lista de centro de salud, se verifica si los pacientes son receptor o donante y se agrega a la lista correspondiente
            for paciente in CentroSalud.lista_pacientes:
                if isinstance(paciente, Receptores): #verificar si es receptor o donante en base a la clase
                    self.lista_receptores.append(paciente)
                    self.buscar_compatibilidad_receptor_a_donante(paciente) #busca compatibilidad entre el receptor y los donantes
                    tiempo = CentroSalud.asignar_y_mandar_vehiculo(paciente)
                    CentroSalud.asignar_cirujano_y_operar(paciente, tiempo)
                    

                elif isinstance(paciente, Donantes):
                    self.lista_donantes.append(paciente)
                    receptor_encontrado = self.buscar_compatibilidad_donante_a_receptor(paciente)
                    tiempo = CentroSalud.asignar_y_mandar_vehiculo(receptor_encontrado) #busca compatibilidad entre el donante y los receptores y manda el vehiculo
                    CentroSalud.asignar_cirujano_y_operar(receptor_encontrado, tiempo)

                else:
                    raise ValueError("El paciente debe ser un receptor o un donante.")

    def buscar_compatibilidad_receptor_a_donante(self, receptor: Receptores):  # Verificar si el órgano que el receptor necesita está en la lista de órganos que el donante puede donar    
        for ir in self.lista_receptores: # i r->receptor
            if receptor[ir].estado.lower() == "inestable": #primero verifico si el receptor esta inestable para darle prioridad al trasplante, es indistinto el tiempo de espera, la situacion es critica y todos necesitan de la operacion
                for donante in self.lista_donantes:
                    if receptor[ir].organo_a_recibir == donante.organos_a_donar and receptor[ir].Tsangre == donante.Tsangre:
                        for i in range(len(donante.organos_a_donar)): #entro a la lista de organos a donar del donante
                            donante.organos_a_donar[i].fecha_ablacion = datetime.now() #seteamos la fecha de ablacion del organo en "0"
                            receptor[ir].organos_a_disposicion += [donante.organos_a_donar]  #coloco el organo del donante en la lista de organos a disposicion del receptor
                            donante.organos_a_donar.remove(donante.organos_a_donar) #el donante no puede donar el organo que ya dono

            elif receptor[ir].estado.lower() == "estable": #misma logica que el anterior, pero para los receptores estables
                for donante in self.lista_donantes:
                    if receptor[ir].organo_a_recibir == donante.organos_a_donar and receptor[ir].Tsangre == donante.Tsangre:
                        for i in range(len(donante.organos_a_donar)):
                            donante.organos_a_donar[i].fecha_ablacion = datetime.now() 
                            receptor[ir].organos_a_disposicion += [donante.organos_a_donar]  
                            donante.organos_a_donar.remove(donante.organos_a_donar) 

    def buscar_compatibilidad_donante_a_receptor(self, donante: Donantes): #verifico si el donante es compatible con el receptor
        for id in self.lista_donantes: #logica exactamente igual a la del receptor, pero sin incluir la prioridad del estado
            for receptor in self.lista_receptores:
                if donante[id].organos_a_donar == receptor.organo_a_recibir and donante[id].Tsangre == receptor.Tsangre:
                    for i in range(len(donante[id].organos_a_donar)):
                        donante[id].organos_a_donar[i].fecha_ablacion = datetime.now()
                        receptor.organos_a_disposicion.append(donante[id].organos_a_donar)                   
                        donante[id].organos_a_donar.remove(donante[id].organos_a_donar)
                    if donante[id].organos_a_donar == []: 
                        self.lista_donantes.remove(donante[id]) #si el donante se queda sin organos, se va de la lista de donantes
        return self.lista_receptores[receptor] #retorna el receptor que coincide con el donante, esta hecho asi a diferencia de la otra funcion de compatibilidad, ya que la funcion del Centro de Salud recibe como argumento al receptor

    def resultados_trasplante(self, cirujanos: Cirujanos, receptor: Receptores): #recibe, como dice el nombre, el resultado del trasplante de ese cirujano con ese paciente
        if CentroSalud.asignar_cirujano_y_operar(): #chequea lo que retorna, al estar escrito asi, Python entiende que es True, osea, operacion exitosa
            self.lista_receptores.remove(receptor)
            return f"La cirujia fue todo un exito y el paciente {receptor.nombre} pasa a estado {receptor.estado}. Se ha quitado de la lista de espera."
        else: #caso inverso al de if (logicamente)
            receptor.estado == "Inestable"
            return f"La cirujia ha fallado y el paciente {receptor.nombre} pasa a estado {receptor.estado}. Se le ha puesto la maxima prioridad en la lista de espera."
