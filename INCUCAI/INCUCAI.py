from pacientes.Receptores import Receptores
from pacientes.Donantes import Donantes
from cirujanos.Cirujanos import Cirujanos
from centro_salud.Centro_Salud import CentroSalud
from organos.Organos import *
from datetime import datetime
class INCUCAI:

    def __init__(self, centros = []):
        """
        Inicializa una instancia de INCUCAI con una lista de centros de salud proporcionada.
        Además, crea listas vacías para almacenar receptores y donantes.
        """
        self.lista_receptores: list[Receptores] = [] #listas para almacenar los receptores y donantes (vacias) 
        self.lista_donantes: list[Donantes] = []
        self.centros_salud: list[CentroSalud] = centros
    
    def recibir_Centros_Salud(self): #FUNCION QUE RECIBE TODAS LAS FUNCIONES, APROVECHANDO QUE RECIBE A LOS CENTROS DE SALUD COMO ARGUMENTO
        """
        Procesa todos los pacientes registrados en los centros de salud.
        Clasifica a cada paciente como receptor o donante, los agrega a sus respectivas listas
        y gestiona todo el proceso de búsqueda de compatibilidad, asignación de vehículo,
        y ejecución de la cirugía por parte del centro de salud.
        """
        for centro in self.centros_salud: #por cada lista de centro de salud, se verifica si los pacientes son receptor o donante y se agrega a la lista correspondiente
            for paciente in centro.lista_pacientes:
                if isinstance(paciente, Receptores): #verificar si es receptor o donante en base a la clase
                    self.lista_receptores.append(paciente)
                    self.buscar_compatibilidad_receptor_a_donante(paciente) #busca compatibilidad entre el receptor y los donantes
                    tiempo = centro.asignar_y_mandar_vehiculo(paciente)
                    centro.asignar_cirujano_y_operar(paciente, tiempo)
                    

                elif isinstance(paciente, Donantes):
                    self.lista_donantes.append(paciente)
                    receptor_encontrado = self.buscar_compatibilidad_donante_a_receptor(paciente)
                    tiempo = centro.asignar_y_mandar_vehiculo(receptor_encontrado) #busca compatibilidad entre el donante y los receptores y manda el vehiculo
                    centro.asignar_cirujano_y_operar(receptor_encontrado, tiempo)

                else:
                    raise ValueError("El paciente debe ser un receptor o un donante.")
    ''' '''            

    def buscar_compatibilidad_receptor_a_donante(self, receptor: Receptores):  # Verificar si el órgano que el receptor necesita está en la lista de órganos que el donante puede donar    
            """
            Busca donantes compatibles para un receptor dado.
            Si el receptor está en estado 'inestable', se le da prioridad.
            Si encuentra un donante con el órgano requerido y tipo de sangre compatible,
            transfiere el órgano al receptor, registra la fecha de ablación y lo elimina
            de la lista de órganos del donante.
            """
            if receptor.estado.lower() == "inestable": #primero verifico si el receptor esta inestable para darle prioridad al trasplante, es indistinto el tiempo de espera, la situacion es critica y todos necesitan de la operacion
                for donante in self.lista_donantes:
                    if receptor.organo_a_recibir == donante.organos_a_donar and receptor.Tsangre == donante.Tsangre:
                        for i in range(len(donante.organos_a_donar)): #entro a la lista de organos a donar del donante
                            donante.organos_a_donar[i].fecha_ablacion = datetime.now() #seteamos la fecha de ablacion del organo en "0"
                            receptor.organos_a_disposicion.append(donante.organos_a_donar)  #coloco el organo del donante en la lista de organos a disposicion del receptor
                            donante.organos_a_donar.remove(donante.organos_a_donar) #el donante no puede donar el organo que ya dono
                            return donante

            elif receptor.estado.lower() == "estable": #misma logica que el anterior, pero para los receptores estables
                for donante in self.lista_donantes:
                    if receptor.organo_a_recibir == donante.organos_a_donar and receptor.Tsangre == donante.Tsangre:
                        for i in range(len(donante.organos_a_donar)):
                            donante.organos_a_donar[i].fecha_ablacion = datetime.now() 
                            receptor.organos_a_disposicion.append(donante.organos_a_donar)
                            donante.organos_a_donar.remove(donante.organos_a_donar) 
                            return donante

    def buscar_compatibilidad_donante_a_receptor(self, donante: Donantes): 
            #verifico si el donante es compatible con el receptor
            #logica exactamente igual a la del receptor, pero sin incluir la prioridad del estado
            """
            Busca receptores compatibles para un donante dado.
            Compara los órganos disponibles del donante con lo que necesitan los receptores
            y también verifica el tipo de sangre.
            Si hay compatibilidad, transfiere los órganos, registra la fecha de ablación,
            los elimina de la lista del donante y remueve al donante si ya no tiene órganos.
            Retorna el receptor compatible encontrado.
            """
            for receptor in self.lista_receptores:
                if donante.organos_a_donar == receptor.organo_a_recibir and donante.Tsangre == receptor.Tsangre:
                    for i in range(len(donante.organos_a_donar)):
                        donante.organos_a_donar[i].fecha_ablacion = datetime.now()
                        receptor.organos_a_disposicion.append(donante.organos_a_donar)                   
                        donante.organos_a_donar.remove(donante.organos_a_donar)
                    if donante.organos_a_donar == []: 
                        self.lista_donantes.remove(donante) #si el donante se queda sin organos, se va de la lista de donantes
            return self.lista_receptores[receptor] #retorna el receptor que coincide con el donante, esta hecho asi a diferencia de la otra funcion de compatibilidad, ya que la funcion del Centro de Salud recibe como argumento al receptor

    def resultados_trasplante(self, cirujanos: Cirujanos, receptor: Receptores): #recibe, como dice el nombre, el resultado del trasplante de ese cirujano con ese paciente
        """
        Informa el resultado de una cirugía.
        Si la operación fue exitosa, elimina al receptor de la lista de espera y devuelve un mensaje de éxito.
        Si falló, actualiza el estado del receptor a 'Inestable' y le asigna máxima prioridad en la lista.
        """
        if CentroSalud.asignar_cirujano_y_operar(): #chequea lo que retorna, al estar escrito asi, Python entiende que es True, osea, operacion exitosa
            self.lista_receptores.remove(receptor)
            return f"La cirujia fue todo un exito y el paciente {receptor.nombre} pasa a estado {receptor.estado}. Se ha quitado de la lista de espera."
        else: #caso inverso al de if (logicamente)
            receptor.estado == "Inestable"
            return f"La cirujia ha fallado y el paciente {receptor.nombre} pasa a estado {receptor.estado}. Se le ha puesto la maxima prioridad en la lista de espera."


