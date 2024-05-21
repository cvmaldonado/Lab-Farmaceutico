from controllers import Controller
import views

def main():
    controller = Controller()

    # Solicitar información del supervisor al inicio del programa
    print("Ingrese la información del supervisor de planta:")
    id = input("ID: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    contrasena = input("Contraseña: ")
    controller.set_supervisor(id, nombre, apellido, fecha_nacimiento, contrasena)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Ingresar operarios")
        print("2. Mostrar equipo de trabajo")
        print("3. Simular paso del tiempo")
        print("4. Historial de producción")
        print("5. Control de calidad")
        print("6. Pago a operarios")
        print("7. Restablecer contraseña")
        print("8. Cambiar contraseña")
        print("9. Salida")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            n = int(input("Ingrese el número de operarios: "))
            operarios_data = []
            for _ in range(n):
                id = input("ID: ")
                estacion = input("Estación: ")
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
                contrasena = input("Contraseña: ")
                operarios_data.append((id, estacion, nombre, apellido, fecha_nacimiento, contrasena))
            controller.ingresar_operarios(operarios_data)
        elif opcion == '2':
            views.mostrar_equipo(controller.supervisor, controller.operarios)
        elif opcion == '3':
            controller.simular_paso_tiempo()
            views.mostrar_mensaje("Simulación de 5 días completada.")
        elif opcion == '4':
            views.mostrar_historial(controller.produccion_estacion1, controller.produccion_estacion2, controller.produccion_estacion3)
        elif opcion == '5':
            controller.control_calidad()
            views.mostrar_mensaje("Control de calidad aplicado.")
        elif opcion == '6':
            pagos_operarios = controller.calcular_pago_operarios()
            for operario, total_pago in pagos_operarios:
                views.mostrar_pago(operario, total_pago)
        elif opcion == '7':
            codigo_id = input("Ingrese el código ID del operario: ")
            success, message = controller.restablecer_contrasena(codigo_id)
            views.mostrar_mensaje(message)
        elif opcion == '8':
            codigo_id = input("Ingrese el código ID del operario: ")
            contrasena_actual = input("Ingrese la contraseña actual: ")
            nueva_contrasena = input("Ingrese la nueva contraseña: ")
            success, message = controller.cambiar_contrasena(codigo_id, contrasena_actual, nueva_contrasena)
            views.mostrar_mensaje(message)
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            views.mostrar_mensaje("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
