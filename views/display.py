def mostrar_equipo(supervisor, operarios):
    print(f"Código ID: {supervisor.id} Estación: Supervisor Nombre: {supervisor.nombre} Apellido: {supervisor.apellido} Fecha Nac.: {supervisor.fecha_nacimiento} Contraseña: {supervisor.contrasena}")
    for operario in operarios:
        print(f"Código ID: {operario.id} Estación: {operario.estacion} Nombre: {operario.nombre} Apellido: {operario.apellido} Fecha Nac.: {operario.fecha_nacimiento} Contraseña: {operario.contrasena}")

def mostrar_historial(produccion_estacion1, produccion_estacion2, produccion_estacion3):
    print("Historial de producción de la última simulación:")
    print("Estación 1:", produccion_estacion1)
    print("Estación 2:", produccion_estacion2)
    print("Estación 3:", produccion_estacion3)

def mostrar_pago(operario, total_pago):
    print(f"Pago para {operario.nombre} {operario.apellido}: ${total_pago}")

def mostrar_mensaje(mensaje):
    print(mensaje)
