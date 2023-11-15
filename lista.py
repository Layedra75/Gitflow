# Proyecto: Lista de tareas

# Función para mostrar la lista de tareas
def mostrar_tareas(tareas):
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")
    print()

# Función principal
def main():
    tareas = []
    
    while True:
        # Mostrar menú
        print("Menú:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Salir")
        
        # Obtener la opción del usuario
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            # Agregar tarea
            tarea = input("Ingrese tu nueva tarea: ")
            tareas.append(tarea)
            print("Tareas agregada con éxito.")
        elif opcion == "2":
            # Marcar tarea como completada
            mostrar_tareas(tareas)
            try:
                indice = int(input("Ingrese el número de la tarea completada: ")) - 1
                tareas.pop(indice)
                print("Tarea marcada como completada.")
            except (ValueError, IndexError):
                print("Error: Ingrese un número válido.")
        elif opcion == "3":
            # Mostrar tareas
            mostrar_tareas(tareas)
        elif opcion == "4":
            # Salir del programa
            print("¡Hasta luego!!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()