class CentroSalud:
    
    def __init__(self, nombre, direccion, telefono, partido, provincia):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.partido = partido
        self.provincia = provincia
        self.lista_cirujanos = [] #lista vacia
        self.lista_vehiculos = [] #lista vacia