from Pacientes.Pacientes import *
from Pacientes.Receptores import *
#from Pacientes.Donantes import *
from Organos.Organos import *
from INCUCAI.INCUCAI import *
#from vehiculos.Vehiculos import *

paciente1 = Receptores("Juan", 12345678, "M", "1990-01-01", "O+", 123456789, "Hospital Central", "Riñon", "2023-10-01", 1, "Insuficiencia renal", "3 de Febrero", "Buenos Aires")
paciente2 = Receptores("Maria", 87654321, "F", "1985-05-15", "A+", 987654321, "Hospital Norte", "Corazon", "2023-10-02", 2, "Cardiopatía", "3 de Febrero", "Buenos Aires")
paciente3 = Receptores("Luis", 45608230, "M", "2000-01-01", "O+", 123456789, "Hospital Italiano", "Pulmon", "2022-11-21", 1, "Neumonia", "CABA", "Buenos Aires")
#vehiculo1 = Vehiculos(100, "terrestre", "AMB123")
#vehiculo2 = Vehiculos(300,"helicoptero", "HELI01")
#vehiculo3 = Vehiculos(500, "avion","AV01")

organo1= Organos("corazon")
organo2= Organos("corazon")
lista_organos = Organos= { organo1, organo2 }

incucai = INCUCAI()
# despacho el vehiculo forma de prueba
#print(vehiculo1.despachar(60, 3))
#print(vehiculo2.despachar(200)) #no les pongo nada pq no consideran trafico
#print(vehiculo3.despachar(500))

incucai.recibir_paciente(paciente1)
print(incucai.resultados_trasplante)