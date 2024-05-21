class User:
    def __init__(self, id, nombre, apellido, fecha_nacimiento, contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.contrasena = contrasena

class Supervisor(User):
    def __init__(self, id, nombre, apellido, fecha_nacimiento, contrasena):
        super().__init__(id, nombre, apellido, fecha_nacimiento, contrasena)

class Operario(User):
    def __init__(self, id, estacion, nombre, apellido, fecha_nacimiento, contrasena):
        super().__init__(id, nombre, apellido, fecha_nacimiento, contrasena)
        self.estacion = estacion
