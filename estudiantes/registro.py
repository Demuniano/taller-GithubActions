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