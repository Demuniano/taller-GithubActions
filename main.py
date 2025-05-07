from estudiantes.registro import cargar_estudiantes, mostrar_estudiantes_tabla, mostrar_promedio_general

def main():
    estudiantes = cargar_estudiantes()

    if not estudiantes:
        print("No se encontraron estudiantes válidos.")
        return
    
    mostrar_estudiantes_tabla(estudiantes)
    mostrar_promedio_general(estudiantes)


if __name__ == "__main__":
    main()