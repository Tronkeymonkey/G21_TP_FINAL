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
    for centro in incucai.centros_salud:  # Recorre la lista de centros de INCUCAI
        if centro.nombre.lower() == nombre_centro.lower():  # Compara sin importar mayúsculas, PORQUEEEE NO ME TOMA EL LOWER()
            return centro
    return None  # Si no lo encuentra, devuelve None

def input_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número válido.")
            

def listas_receptores(incucai: INCUCAI): #ver si hacer un if y crear listas vacias asi puedo ir agregando
    print("\n---- LISTA RECEPTORES -----")
    for idx, i in enumerate(incucai.lista_receptores):
        print(f"{idx}. Nombre: {i.nombre} - Organo a recibir: {i.organo_a_recibir} - Tipo de sangre: {i.Tsangre} - Partido: {i.partido}, Provincia: {i.provincia}") # type: ignore #si hace falta agregar el resto

def listas_donantes(incucai:INCUCAI):
    print("\n----- LISTA DONANTES ----")
    for idx, i in enumerate(incucai.lista_donantes):
        print(f"{idx}. Nombre: {i.nombre} - Tipo de sangre: {i.Tsangre} - Centro de salud en el que se encunetra: {i.centro_de_salud}") #falta agregar algun dato
        
def listas_centros_salud(incucai: INCUCAI):
    print("\n ---- CENTROS DE SALUD ----")
    for i in incucai.centros_salud:
        print(f" Nombre: {i.nombre} - Partido: {i.partido} - Provincia: {i.provincia} - Tel: {i.telefono} ") 

# IMPORTANTE: CUANDO AGREGO RECEPTOR Y DONANTE TENGO QUE FIJAFRME COMO LO AGREGO A MIS LISTAS DE RECEPTORES Y DONANTES, chequear el menu bien.
#cuando les pido que ingresen fechas deberia haceer un if donde me figure que sea una fecha valida desde 2025 dia en el que estamos hasta xej 70 años atras(?
      
def agregar_receptor(incucai: INCUCAI):
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
        dni_input = input("DNI (Ingrese solo 8 digitos por favor): ").strip()
        if not dni_input.isdigit():
            print("ERROR. El DNI debe contener solo números.")
        elif len(dni_input) != 8:
            print("ERROR. El DNI debe tener exactamente 8 dígitos.")
        else:
            dni = int(dni_input)
        break
    
    #bucle sexo
    sexo = input("Sexo: M para masculino, F para femenino: ")
    while sexo.upper() not in ("M", "F"):
        print("Sexo inválido. Ingrese M o F.")
        sexo = input("Sexo (M/F): ")
    sexo = sexo.upper()
    
    #bucle nacimiento
    # Inicializo nacimiento en none, no hay una fecha valida todavia
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
    
    #bucle partido
    partido = input("Partido: ").strip()
    while True:
        if not partido:
            print("El partido no puede estar vacío. Ingrese nuevamente un partido:")
        elif any(char.isdigit() for char in partido):
            print("El partido no puede contener números. Ingrese nuevamente un partido:")
        else:
            break
        
    #bucle provincia
    provincia = input("Provincia: ").strip()
    while True:
        if not provincia:
            print("La provincia no puede estar vacía. Ingrese nuevamente una provincia:")
        elif any(char.isdigit() for char in provincia):
            print("La provincia no puede contener números. Ingrese nuevamente una provincia:")
        else:
            break
    provincia = provincia.title() #para que quede por ejemplo con Buenos Aires
    
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
                

def menu(incu:INCUCAI):
    
    print("\n INCUCAI SISTEMA DE TRANSPLANTES") #cambiar si es necesario 
    print("\n1. Ver lista de receptores")
    print("\n2. Ver lista de donantes")
    print("\n3. Ver centros de salud")
    print("\n4. Agregar nuevo receptor")
    print("\n5. Agregar nuevo donante")
    print("\n6. Salir del programa")
    
    opcion = input("Elija una opcion: ")
    while True:
        if opcion == "1":
            listas_receptores(incu)
        elif opcion == "2":
            listas_donantes(incu)    
        elif opcion == "3":
            listas_centros_salud(incu)
        elif opcion == "4":
            agregar_receptor(incu)
        elif opcion == "5":
            agregar_donante(incu)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Elegí nuevamente.")       
                