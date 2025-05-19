from pacientes.Pacientes import *
from pacientes.Receptores import *
from organos.Organos import Organos #consultarselo a Sol
from incucai.INCUCAI import *
from vehiculos.Auto import *
from vehiculos.Avion import *
from vehiculos.Helicoptero import * 
from centro_salud.Centro_Salud import *



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
    Donantes("Carlos Ponce", 34222333, "M", "1985-06-30", "O+", "23459385", centros_salud[0].nombre),
    Donantes("Elena Mariscotti", 22113344, "F", "1970-04-10", "A+", "112305739", centros_salud[1].nombre),
    Donantes("Tomas Hourquescos", 35112244, "M", "1995-12-01", "O+", "341823045",centros_salud[2].nombre),
    Donantes("Lucía Drappo", 44112233, "F", "1982-08-08", "B-", "1134728305", centros_salud[3].nombre), 
    Donantes("Franca Nanni", 47034652, "F", "2006-03-24", "0+", "3412348764", centros_salud[0].nombre),
    Donantes()]

