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

def obtener_centro_salud(nombre):
    for centro in centros_salud:
        if centro.nombre.lower() == nombre.lower():
            return centro
    return None

def input_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número válido.")

# Crear vehículos
vehiculos = [
    Auto(velocidad_viajes=80, identificador="AD 342 SD"),
    Auto(velocidad_viajes=100, identificador="AB 134 DF"),
    Helicoptero(velocidad_viajes=250, identificador="HEL01"),
    Helicoptero(velocidad_viajes=300, identificador="HEL02"),
    Avion(velocidad_viajes=600, identificador="AE01"),
    Avion(velocidad_viajes=700, identificador="AE02") ]

centros_salud = [
    CentroSalud("Hospital Italiano", "Calle Falsa 123", "1122334455", "3 de Febrero", "Buenos Aires"),
    CentroSalud("Hospital Privado Rosario", " Pres. Roca 2440", "0341 489-3500", "Rosario", "Santa Fe"),
    CentroSalud("Hospital Zonal Dr. Ramón Carrillo", "20 de Febrero 598 ", "0294 452-5000", "Bariloche", "Rio Negro"),
    CentroSalud("Sanatorio Parque", "Blvd. Oroño 860", " 0341 420-0222", "Rosario", "Santa Fe")
]

# Asignar vehículos a los centros de salud
centros_salud[0].lista_vehiculos.extend([vehiculos[0], vehiculos[2]])
centros_salud[1].lista_vehiculos.extend([vehiculos[1], vehiculos[3]])
centros_salud[2].lista_vehiculos.append(vehiculos[4])
centros_salud[3].lista_vehiculos.append(vehiculos[5])

receptores = [
    Receptores("Ignacio Amarillo", 23456987, "M", "1973-02-09", "O+", 113334567, centros_salud[0].nombre, "Riñon", "2024-10-23", 1, "Insuficiencia renal", "Pergamino", "Buenos Aires"),
    Receptores("Maria Escalante", 34654321, "F", "1995-05-15", "A+", 11234567, centros_salud[1].nombre, "Corazon", "2025-10-02", 2, "Cardiopatía", "San Isidro", "Buenos Aires"),
    Receptores("Luis Beinlich", 45608230, "M", "2005-09-01", "O+", 270345678, centros_salud[2].nombre, "Pulmon", "2022-11-21", 1, "Neumonía", "Victoria", "Entre Rios"), #si no tengo un hospital en esa ciudad, que pasa?????
    Receptores("Ana Lavalle", 25445566, "F", "1975-03-22", "B-", 341354769, centros_salud[3].nombre, "Hígado", "2024-01-15", 3, "Hepatitis", "Rosario", "Santa Fe")
]

organos = [
    Organos("Riñón"),
    Organos("Corazón"),
    Organos("Pulmón"),
    Organos("Hígado")
    ]

donantes = [
    Donantes("Carlos Ponce", 34222333, "M", "1985-06-30", "O+", "23459385", centros_salud[0].nombre, "2025-03-21" ),
    Donantes("Elena Mariscotti", 22113344, "F", "1970-04-10", "A+", "112305739", centros_salud[1].nombre,"2025-04-07"),
    Donantes("Tomas Hourquescos", 35112244, "M", "1995-12-01", "O+", "341823045",centros_salud[2].nombre, "2025-04-25"),
    Donantes("Lucía Drappo", 44112233, "F", "1982-08-08", "B-", "1134728305", centros_salud[3].nombre, "2025-05-03"), 
    Donantes("Franca Nanni", 47034652, "F", "2006-03-24", "0+", "3412348764", centros_salud[0].nombre, "2025-05-15")
    ]

def menu():
    
    print("\n INCUCAI SISTEMA DE TRANSPLANTES") #cambiar si es necesario 
    print("\n1. Ver lista de receptores")
    print("\n2. Ver lista de donantes")
    print("\n3. Ver centros de salud")
    print("\n4. Agregar nuevo receptor")
    print("\n5. Agregar nuevo donante")
    print("\n6. Salir del programa")
    
def listas_receptores(): #ver si hacer un if y crear listas vacias asi puedo ir agregando
    print("\n---- LISTA RECEPTORES -----")
    for idx, i in enumerate(receptores):
        print(f"{idx}. Nombre: {i.nombre} - Organo a recibir: {i.organo_a_recibir} - Tipo de sangre: {i.Tsangre} - Partido: {i.partido}, Provincia: {i.provincia}") # type: ignore #si hace falta agregar el resto
def listas_donantes():
    print("\n----- LISTA DONANTES ----")
    for idx, i in enumerate(donantes):
        print(f"{idx}. Nombre: {i.nombre} - Tipo de sangre: {i.Tsangre} - Centro de salud en el que se encunetra: {i.centro_de_salud}") #falta agregar algun dato
def listas_centros_salud():
    print("\n ---- CENTROS DE SALUD ----")
    for i in centros_salud:
        print(f" Nombre: {i.nombre} - Partido: {i.partido} - Provincia: {i.provincia} - Tel: {i.telefono} ") 

# IMPORTANTE: CUANDO AGREGO RECEPTOR Y DONANTE TENGO QUE FIJAFRME COMO LO AGREGO A MIS LISTAS DE RECEPTORES Y DONANTES, chequear el menu bien.
#cuando les pido que ingresen fechas deberia haceer un if donde me figure que sea una fecha valida desde 2025 dia en el que estamos hasta xej 70 años atras(?
#hola       
def agregar_receptor():
    print("\n CARGAR NUEVO RECEPTOR")
    #bucle nombre
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío. Ingrese nuevamente un nombre:")
        elif any(char.isdigit() for char in nombre):
            print("El nombre no puede contener números. Ingrese nuevamente un nombre:")
        else:
            break
    #bucle dni   
    while True:
        dni_input = input("DNI (8 dígitos): ").strip()
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
    
    #bucle nacimiento   
    nacimiento = None
    while not nacimiento:
        nacimiento_input = input("Fecha de nacimiento (YYYY-MM-DD): ")
        nacimiento = validar_fecha(nacimiento_input, "%Y-%m-%d")
    
    #bucle grupos sanguineos
    grupos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:     
        grupo_sanguineo = input("Grupo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
        if grupo_sanguineo in grupos_validos:
            break
        else:
            print("Grupo sanguíneo inválido. Ingrese uno de estos grupos: (A+, A-, B+, B-, AB+, AB-, O+, O-).")
     
    telefono = input_entero("Telefono:")
    centro_de_salud = input("Nombre del centro de salud: ")
    organo_a_recibir = input("Órgano que necesita: ")
    fecha_en_espera = input("Fecha en lista de espera (YYYY-MM-DD): ")
    prioridad = input_entero("Prioridad (1 = alta, 2 = media, 3 = baja: ") #chequear???
    patologia = input("Diagnóstico: ")
    partido = input("Partido: ")
    provincia = input("Provincia: ")
    
    centro_de_salud = None
    while not centro_de_salud:
        nombre_centro = input("Nombre del centro de salud: ")
        centro_de_salud = obtener_centro_salud(nombre_centro)
        if not centro_de_salud:
            print("Centro no encontrado. Verifique el nombre.")

    nuevo = Receptores(nombre, dni, sexo, nacimiento, grupo_sanguineo, telefono, centro_de_salud, organo_a_recibir, fecha_en_espera, prioridad, patologia, partido, provincia)
    receptores.append(nuevo)
    print("Receptor agregado correctamente.")   
    
    
    #preguntar a sol que es lo que ella espera del main!!!!! 
def agregar_donante(): 
    print("\nCARGAR NUEVO DONANTE:")
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif any(char.isdigit() for char in nombre):
            print("El nombre no puede contener números.")
        else:
            break
    while True:
        dni_input = input("DNI (8 dígitos): ").strip()
        if not dni_input.isdigit():
            print("El DNI debe contener solo números.")
        elif len(dni_input) != 8:
            print("El DNI debe tener exactamente 8 dígitos.")
        else:
            dni = int(dni_input)
        break

    sexo = input("Sexo (M/F): ")
    while sexo.upper() not in ("M", "F"):
        print("Sexo inválido. Ingrese M o F.")
        sexo = input("Sexo (M/F): ")
    #hola
    fecha_nacimiento = None
    while not fecha_nacimiento:
        nacimiento_input = input("Fecha de nacimiento (YYYY-MM-DD): ")
        fecha_nacimiento = validar_fecha(nacimiento_input, "%Y-%m-%d")
         
    grupos_validos = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:     
        grupo_sanguineo = input("Grupo sanguíneo (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
        if grupo_sanguineo in grupos_validos:
            break
        else:
            print("Grupo sanguíneo inválido. Intente nuevamente.")
    
    centro_salud = None
    while not centro_salud:
        nombre_centro = input("Nombre del centro de salud: ")
        centro_salud = obtener_centro_salud(nombre_centro)
        if not centro_salud:
            print("Centro no encontrado. Verifique el nombre.")
            
    fecha_hora_ablacion = None
    while not fecha_hora_ablacion:
        ablacion_input = input("Fecha de ablación (YYYY-MM-DD HH:MM): ")
        fecha_hora_ablacion = validar_fecha(ablacion_input, "%Y-%m-%d %H:%M")
    
    nuevo_donante = Donantes(
        nombre,
        dni,
        sexo.upper(),
        fecha_nacimiento,
        grupo_sanguineo,
        centro_salud,
        fecha_hora_ablacion
    )
    donantes.append(nuevo_donante)
    print("Donante agregado correctamente.")
    
while True:
    menu()
    opcion = input("Elija una opcion: ")
    
    if opcion == "1":
        listas_receptores()
    elif opcion == "2":
        listas_donantes()    
    elif opcion == "3":
        listas_centros_salud()
    elif opcion == "4":
        agregar_receptor()
    elif opcion == "5":
        agregar_donante()
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Elegí nuevamente.")       
    