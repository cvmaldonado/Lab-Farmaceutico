import random
from models.users import Supervisor, Operario

class UserController:
    def __init__(self):
        self.supervisor = None
        self.operarios = []
        self.produccion_estacion1 = []
        self.produccion_estacion2 = []
        self.produccion_estacion3 = []

    def set_supervisor(self, id, nombre, apellido, fecha_nacimiento, contrasena):
        self.supervisor = Supervisor(id, nombre, apellido, fecha_nacimiento, contrasena)

    def ingresar_operarios(self, operarios_data):
        for data in operarios_data:
            operario = Operario(*data)
            self.operarios.append(operario)

    def simular_paso_tiempo(self):
        for _ in range(5):
            self.produccion_estacion1.append(random.randint(75, 120))
            self.produccion_estacion2.append(random.randint(75, 120))
            self.produccion_estacion3.append(random.randint(75, 120))

    def control_calidad(self):
        self.produccion_estacion1 = [int(p * 0.9) for p in self.produccion_estacion1]
        self.produccion_estacion2 = [int(p * 0.94) for p in self.produccion_estacion2]
        self.produccion_estacion3 = [int(p * 0.97) for p in self.produccion_estacion3]

    def calcular_pago_operarios(self):
        pagos = {1: self.produccion_estacion1, 2: self.produccion_estacion2, 3: self.produccion_estacion3}
        pagos_operarios = []
        for operario in self.operarios:
            estacion = int(operario.estacion[-1])
            total_pago = sum([u * 5 + 15 if u > 100 else u * 5 for u in pagos[estacion]])
            pagos_operarios.append((operario, total_pago))
        return pagos_operarios

    def restablecer_contrasena(self, codigo_id):
        for operario in self.operarios:
            if operario.id == codigo_id:
                operario.contrasena = f"{operario.nombre}.{operario.apellido}{operario.fecha_nacimiento[-4:]}"
                return True, operario.contrasena
        return False, "ID no encontrado."

    def cambiar_contrasena(self, codigo_id, contrasena_actual, nueva_contrasena):
        for operario in self.operarios:
            if operario.id == codigo_id and operario.contrasena == contrasena_actual:
                operario.contrasena = nueva_contrasena
                return True, "Contraseña cambiada exitosamente."
        return False, "ID o contraseña actual incorrecta."
