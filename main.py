from Pacientes import *
from Receptores import *
from Donantes import *
from INCUCAI import *

paciente1 = Receptores("Juan", 12345678, "M", "1990-01-01", "O+", 123456789, "Hospital Central", "Riñón", "2023-10-01", 1, "Insuficiencia renal")
paciente2 = Receptores("Maria", 87654321, "F", "1985-05-15", "A+", 987654321, "Hospital Norte", "Corazón", "2023-10-02", 2, "Cardiopatía")
paciente3 = Receptores("Juan", 12345678, "M", "1990-01-01", "O+", 123456789, "Hospital Central", "Riñón", "2023-10-01", 1, "Insuficiencia renal")
incucai = INCUCAI()

incucai.recibir_paciente(paciente1)