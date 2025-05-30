from pacientes.Pacientes import *
from pacientes.Receptores import *
from organos.Organos import Organos #consultarselo a Sol
from incucai.INCUCAI import *
from vehiculos.Auto import *
from vehiculos.Avion import *
from vehiculos.Helicoptero import * 
from centro_salud.Centro_Salud import *
import datetime

# --------- Funciones para el menu ---------
def validar_fecha(fecha_str, formato="%Y-%m-%d", anios_max=100):
    try:
        fecha = datetime.datetime.strptime(fecha_str, formato)
        hoy = datetime.datetime.now()
        fecha_minima = hoy - datetime.timedelta(days=anios_max*365)
        if fecha_minima <= fecha <= hoy:
            return fecha
        else:
            print("Fecha fuera de rango lógico.")
    except ValueError:
        print("Formato de fecha inválido, Ingrese correctamente: Año, Mes, Dia.")
    return None

def obtener_centro_salud(incucai: INCUCAI, nombre_centro: str):
    for centro in incucai.centros_salud:
        if centro.nombre.strip().lower() == nombre_centro.strip().lower():
            return centro
    return None

def input_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número válido.")

def dni_donante_ya_existe(incucai: INCUCAI, dni: int) -> bool:
    return any(d.dni == dni for d in incucai.lista_donantes) 

def calcular_edad(nacimiento: datetime.datetime) -> int:
    hoy = datetime.datetime.now()
    return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))          
            

def listas_receptores_por_centro(incucai: INCUCAI): #ver si hacer un if y crear listas vacias asi puedo ir agregando
    print("\n---- LISTA RECEPTORES POR CENTRO DE SALUD -----")
    if not incucai.centros_salud:
        print("No hay centros de salud registrados")
        return
    
    listas_centros_salud(incucai)  # va a mostrar todos los centros de salud
    
    receptores_filtrados = [r for r in incucai.lista_receptores if r.centro_de_salud.nombre.lower() == centro.nombre.lower()]
    
    if not receptores_filtrados:
        print(f"No hay receptores registrados en el centro de salud: {centro.nombre}")
    else:
        for idx, i in enumerate(receptores_filtrados):
            print(f"{idx}. Nombre: {i.nombre} - Órgano: {i.organo_a_recibir} - Sangre: {i.Tsangre} - Partido: {i.partido} - Provincia: {i.provincia}")



    
    nombre_centro = input("\nIngrese el nombre del centro de salud para ver sus receptores: ")
    centro = obtener_centro_salud(incucai, nombre_centro)
    
    if not centro:
        print("Centro no encontrado. Verifique el nombre.")
        return
    
    # Ordena por prioridad y luego por edad( depende si es 1, 2, 3)
    receptores_ordenados = sorted(
        receptores_filtrados,
        key=lambda r: (r.prioridad, calcular_edad(r.nacimiento))
    )

    print(f"\nReceptores en {centro.nombre} (ordenados por prioridad y edad):")
    for idx, i in enumerate(receptores_ordenados, start=1):
        print(f"{idx}. Nombre: {i.nombre} - Órgano: {i.organo_a_recibir} - Sangre: {i.Tsangre} - Prioridad: {i.prioridad} - Edad: {calcular_edad(i.nacimiento)} - Partido: {i.partido} - Provincia: {i.provincia}")
        
def listas_donantes(incucai:INCUCAI):
    print("\n----- LISTA DONANTES ----")
    for idx, i in enumerate(incucai.lista_donantes):
        print(f"{idx}. Nombre: {i.nombre} - Tipo de sangre: {i.Tsangre} - Centro de salud en el que se encunetra: {i.centro_de_salud}") #falta agregar algun dato
        
def listas_centros_salud(incucai: INCUCAI):
    print("\n ---- CENTROS DE SALUD ----")
    for i in incucai.centros_salud:
        print(f" Nombre: {i.nombre} - Partido: {i.partido} - Provincia: {i.provincia} - Tel: {i.telefono} ") 

      
def agregar_receptor(incucai: INCUCAI):
    print("\n CARGAR NUEVO RECEPTOR")
    
       # Solicitar DNI primero
    while True:
        dni_input = input("DNI (8 dígitos): ").strip()
        if not dni_input.isdigit():
            print("El DNI debe contener solo números.")
        elif len(dni_input) != 8:
            print("El DNI debe tener exactamente 8 dígitos.")
        else:
            dni = int(dni_input)
            if dni_donante_ya_existe(incucai, dni):
                print( "Ya existe un donante con ese DNI. Cancelando ingreso.")
                return  # corta la función
            break  # DNI válido y no repetido
        
    #bucle nombre
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío. Ingrese nuevamente un nombre:")
        elif any(char.isdigit() for char in nombre):
            print("El nombre no puede contener números. Ingrese nuevamente un nombre:")
        else:
            break
        
    #bucle sexo
    sexo = input("Sexo: M para masculino, F para femenino: ")
    while sexo.upper() not in ("M", "F"):
        print("Sexo inválido. Ingrese M o F.")
        sexo = input("Sexo (M/F): ")
    sexo = sexo.upper()
    
    #bucle nacimiento
    #Inicializo nacimiento en none, no hay una fecha valida todavia
    #que la edad sea mayor o igual a tal edad para perfeccionarlo
    nacimiento = None
    while not nacimiento: #se ejecuta el bucle mientras la variable nacimiento siga siendo none, mientras que no tengamos una fecha valida
        nacimiento_input = input("Fecha de nacimiento (YYYY-MM-DD): ") #Ingresa el usuario una fecha en el formato adecuado
        nacimiento = validar_fecha(nacimiento_input, "%Y-%m-%d") #Se llama a la funcion validar fecha para hacer la validacion real. Se escribe en el formato correcto y la fecha es logica, la funcion devuelve un objeto datetime, sino muestra error y el while sigue.
    
    #bucle grupos sanguineos
    grupos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:     
        grupo_sanguineo = input("Grupo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
        if grupo_sanguineo in grupos_validos:
            break
        else:
            print("Grupo sanguíneo inválido. Ingrese uno de estos grupos: (A+, A-, B+, B-, AB+, AB-, O+, O-).")
    
    telefono = input_entero("Telefono:") #ver cuantos digitos tiene que poner
    
    #bucle centro de salud
    centro_de_salud = None
    while not centro_de_salud:
        nombre_centro = input("Nombre del centro de salud: ")
        centro_de_salud = obtener_centro_salud(nombre_centro) #llama a mi funcion obtener centro para que coincidan lo que tengo en las listas con lo que ingreso
        if not centro_de_salud:
            print("Centro no encontrado. Verifique el nombre.")
    
    #bucle organos        
    organos_validos = ["corazon", "pulmon", "piel", "corneas", "huesos", "higado", "riñon", "intestinos"]
    while True:
        organo_a_recibir = input("Órgano que necesita: ").strip().lower()
        if organo_a_recibir in organos_validos:
            break
        else:
            print(f"Órgano inválido. Debe ser uno de: {', '.join(organos_validos)}")
            
                       
    #bucle fecha en esperadel receptor
    fecha_en_espera = None
    while not fecha_en_espera:
        espera_input = input("Fecha de espera (YYYY-MM-DD HH:MM): ")
        fecha_en_espera = validar_fecha(espera_input, "%Y-%m-%d %H:%M")
    
    prioridad = input_entero("Prioridad (1 = alta, 2 = media, 3 = baja: ") #chequear???
    
    
    nuevo = Receptores(nombre, dni, sexo, nacimiento, grupo_sanguineo, telefono, centro_de_salud, organo_a_recibir, fecha_en_espera, prioridad, partido, provincia)
    incucai.lista_receptores.append(nuevo)
    print("Receptor agregado correctamente.")   
    
    
    
def agregar_donante(incucai: INCUCAI): #chequeado 
    print("\nCARGAR NUEVO DONANTE:")

    #bucle nombre
    nombre = input("Nombre: ").strip()
    while True:
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif any(char.isdigit() for char in nombre):
            print("El nombre no puede contener números.")
        else:
            break
        
    #bucle dni    
    dni_input = input("DNI (8 dígitos): ").strip()    
    while True:
        if not dni_input.isdigit():
            print("El DNI debe contener solo números.")
        elif len(dni_input) != 8:
            print("El DNI debe tener exactamente 8 dígitos.")
        else:
            dni = int(dni_input)
        break
    
    #bucle sexo
    sexo = input("Sexo (M/F): ")
    while sexo.upper() not in ("M", "F"):
        print("Sexo inválido. Ingrese M o F.")
        sexo = input("Sexo (M/F): ")
    sexo = sexo.upper()
    
    #bucle nacimiento (debe ingresar una fecha coherente)
    fecha_nacimiento = None
    while not fecha_nacimiento:
        nacimiento_input = input("Fecha de nacimiento (YYYY-MM-DD): ")
        fecha_nacimiento = validar_fecha(nacimiento_input, "%Y-%m-%d")
    
    #bucle grupo sanguineo     
    grupos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:     
        grupo_sanguineo = input("Grupo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
        if grupo_sanguineo in grupos_validos:
            break
        else:
            print("Grupo sanguíneo inválido. Intente nuevamente.")
    
    #bucle centro de salud
    centro_salud = None #El bucle se repite mientras centro_salud siga siendo None. Es decir, hasta que encuentre un centro válido.
    while not centro_salud:
        nombre_centro = input("Nombre del centro de salud: ")
        centro_salud = obtener_centro_salud(nombre_centro)
        if not centro_salud:
            print("Centro no encontrado. Verifique el nombre.")
    
    #bucle fecha hora ablacion        
    fecha_hora_ablacion = None
    while not fecha_hora_ablacion:
        ablacion_input = input("Fecha de ablación (YYYY-MM-DD HH:MM): ")
        fecha_hora_ablacion = validar_fecha(ablacion_input, "%Y-%m-%d %H:%M")
    
    nuevo_donante = Donantes(nombre, dni, sexo, fecha_nacimiento, grupo_sanguineo, centro_salud, fecha_hora_ablacion)
    incucai.lista_donantes.append(nuevo_donante)
    print("Donante agregado correctamente.")
    
def consultar_resultado_trasplante(centros_salud: CentroSalud):
    dni_buscado = int(input("Ingrese el DNI del paciente: "))
    for centro in centros_salud:
        for paciente in centro.pacientes_exitosos:
            if paciente.DNI == dni_buscado:
                print("El trasplante fue exitoso.")
                return
        for paciente in centro.pacientes_fallidos:
            if paciente.DNI == dni_buscado:
                print("El trasplante falló.")
                return
    print("No se encontró un trasplante asociado a ese DNI.")
                

def menu(incu:INCUCAI):
    
    print(f'''
-----INCUCAI SISTEMA DE TRANSPLANTES-----

        \n1. Ver lista de receptores
        \n2. Ver lista de donantes
        \n3. Ver centros de salud
        \n4. Agregar nuevo receptor
        \n5. Agregar nuevo donante
        \n6. Resultado transplante
        \n7. Salir del programa''')
    
    
    while True:
        opcion = input("\nElija una opcion: ")

        if opcion == "1":
            listas_receptores_por_centro(incu)
        elif opcion == "2":
            listas_donantes(incu)    
        elif opcion == "3":
            listas_centros_salud(incu)
        elif opcion == "4":
            agregar_receptor(incu)
        elif opcion == "5":
            agregar_donante(incu)
        elif opcion == "6":
            consultar_resultado_trasplante(incu.centros_salud)
        elif opcion == "7":
            print("Saliendo del sistema...")  
            break
        else:
            print("Opción no válida. Elegí nuevamente.")       
                
                