import csv


def cargar_estudiantes():
    estudiantes_validos = []

    try:
        with open('estudiantes.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    nota = float(fila['nota'])
                    if 0.0 <= nota <= 5.0:
                        estudiantes_validos.append({
                            'nombre': fila['nombre'],
                            'nota': nota
                        })
                except ValueError:
                    continue

        return estudiantes_validos

    except FileNotFoundError:
        return []


def mostrar_estudiantes_tabla(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda est: est['nombre'])

    print(f"{'Nombre':<20} {'Nota':>5}")
    print("-" * 26)

    for est in estudiantes_ordenados:
        print(f"{est['nombre']:<20} {est['nota']:>5.2f}")


def mostrar_promedio_general(estudiantes):
    if not estudiantes:
        print("No hay estudiantes válidos para calcular el promedio.")
        return

    suma_notas = sum(est['nota'] for est in estudiantes)
    promedio = suma_notas / len(estudiantes)
    print(f"\nPromedio general de notas: {promedio:.2f}")
