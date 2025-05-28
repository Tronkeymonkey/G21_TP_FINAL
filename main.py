from pacientes.Receptores import Receptores
from organos.Organos import Organos #consultarselo a Sol
from incucai.INCUCAI import INCUCAI
from vehiculos.Auto import Auto
from vehiculos.Avion import Avion
from vehiculos.Helicoptero import Helicoptero
from centro_salud.Centro_Salud import CentroSalud
import datetime
from menu import *


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
    Receptores("Ignacio Amarillo", 23456987, "M", "1973-02-09", "O+", 113334567, centros_salud[0].nombre, "Riñon", "2024-10-23", 1, "Insuficiencia renal"),
    Receptores("Maria Escalante", 34654321, "F", "1995-05-15", "A+", 11234567, centros_salud[1].nombre, "Corazon", "2025-10-02", 2, "Cardiopatía"),
    Receptores("Luis Beinlich", 45608230, "M", "2005-09-01", "O+", 270345678, centros_salud[2].nombre, "Pulmon", "2022-11-21", 1, "Neumonía"), #si no tengo un hospital en esa ciudad, que pasa?????
    Receptores("Ana Lavalle", 25445566, "F", "1975-03-22", "B-", 341354769, centros_salud[3].nombre, "Hígado", "2024-01-15", 3, "Hepatitis")
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

pacientes = [
    # Receptores iniciales
    Receptores("Ignacio Amarillo", 23456987, "M", "1973-02-09", "O+", 113334567, "Riñon", "2024-10-23", 1, "Insuficiencia renal"),
    Receptores("Maria Escalante", 34654321, "F", "1995-05-15", "A+", 11234567, "Corazon", "2025-10-02", 2, "Cardiopatía"),
    Receptores("Luis Beinlich", 45608230, "M", "2005-09-01", "O+", 270345678, "Pulmon", "2022-11-21", 1, "Neumonía"),
    Receptores("Ana Lavalle", 25445566, "F", "1975-03-22", "B-", 341354769, "Hígado", "2024-01-15", 3, "Hepatitis"),

    # Donantes iniciales
    Donantes("Carlos Ponce", 34222333, "M", "1985-06-30", "O+", "23459385", "2025-03-21"),
    Donantes("Elena Mariscotti", 22113344, "F", "1970-04-10", "A+", "112305739", "2025-04-07"),
    Donantes("Tomas Hourquescos", 35112244, "M", "1995-12-01", "O+", "341823045",centros_salud[2].nombre, "2025-04-25"),
    Donantes("Lucía Drappo", 44112233, "F", "1982-08-08", "B-", "1134728305", centros_salud[3].nombre, "2025-05-03"),
    Donantes("Franca Nanni", 47034652, "F", "2006-03-24", "O+", "3412348764", centros_salud[0].nombre, "2025-05-15"),

    # 10 registros adicionales
    # Receptor 1
    Receptores("Ricardo Sánchez", 28901234, "M", "1980-11-10", "A-", 115678901, "Hígado", "2023-09-05", 2, "Insuficiencia hepática"),
    # Donante 1
    Donantes("Sofía Méndez", 40123456, "F", "1998-07-20", "B+", "1123456789", "2025-06-01"),
    # Receptor 2
    Receptores("Pedro Giménez", 31098765, "M", "1990-03-01", "O-", 341987654, "Corazon", "2024-02-18", 1, "Miocardiopatía dilatada"),
    # Donante 2
    Donantes("Camila Núñez", 42345678, "F", "2000-01-15", "AB-", "3517654321", "2025-07-10"),
    # Receptor 3
    Receptores("Valeria Rossi", 29876543, "F", "1983-09-25", "B+", 261876543, "Pulmon", "2023-11-30", 3, "Enfisema pulmonar"),
    # Donante 3
    Donantes("Martín Sosa", 36789012, "M", "1993-04-05", "A+", "2991234567", "2025-08-20"),
    # Receptor 4
    Receptores("Florencia Blanco", 38012345, "F", "1996-12-12", "O+", 387123456, "Riñon", "2024-05-20", 2, "Poliquistosis renal"),
    # Donante 4
    Donantes("Gustavo Pereyra", 45678901, "M", "2002-10-08", "O-", "3791122334", "2025-09-01"),
    # Receptor 5
    Receptores("Emilia Gómez", 30123456, "F", "1988-06-03", "AB+", 341456789, "Páncreas", "2023-07-10", 1, "Diabetes tipo 1"),
    Donantes("Diego Acosta", 41234567, "M", "1999-02-17", "B-", "1165432109", "2025-10-15")
]

#centros_salud[0].lista_pacientes.append([pacientes[1], pacientes[5]])
centros_salud[0].asignar_pacientes([pacientes[1], pacientes[5]])

incucai = INCUCAI(centros_salud)

incucai.recibir_Centros_Salud()

menu(incucai)