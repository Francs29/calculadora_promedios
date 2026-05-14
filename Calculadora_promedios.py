# Francisco Javier Herrera Piedra.
# Calculadora_promedios.


def ingresar_calificaciones():

    materias = []
    calificaciones = []

    while True:
        materia = input("\nIngresa una materia (o escribe 'fin' para terminar): ")

        # Palabra para finalizar proceso de materias
        if materia.lower() == "fin":
            break

        # Error en nombre vacío
        if materia.strip() == "":
            print("La materia no puede estar vacía.")
            continue

        # Función para ingresar la calificación
        while True:
            try:
                calificacion = float(input("Ingresa la calificación (0-10): "))

                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: la calificación debe estar entre 0 y 10.")

            except ValueError:
                print("Error: debes ingresar un número válido.")

        # Agregar datos a las listas
        materias.append(materia)
        calificaciones.append(calificacion)

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Calcula el promedio general.
    """

    if len(calificaciones) == 0:
        return 0

    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)

    return promedio


# Calificación mínima para aprobación >= 6.0
def determinar_estado(calificaciones, umbral=6.0):

    aprobadas = []
    reprobadas = []

    for i in range(len(calificaciones)):

        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):

    indice_max = 0
    indice_min = 0

    for i in range(len(calificaciones)):

        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i

        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i

    return indice_max, indice_min


# Determinar Alumno aprobo o reprobo
def estado_general(promedio, umbral=6.0):

    if promedio >= umbral:
        return "APROBADO"
    else:
        return "REPROBADO"


def mostrar_resumen(nombre, materias, calificaciones, promedio,
                     estado,
                     aprobadas, reprobadas,
                     indice_max, indice_min):

    print("\n" + "=" * 40)
    print("RESUMEN FINAL")
    print("=" * 40)

    print(f"\nAlumno: {nombre}")

    print("\nMaterias y calificaciones:")

    for i in range(len(materias)):
        print(f"{i+1}. {materias[i]}: {calificaciones[i]}")

    print(f"\nPromedio general: {promedio:.2f}")

    # Mostrar estado general
    print(f"\nEstado general del alumno: {estado}")

    print("\nMaterias aprobadas:")

    if len(aprobadas) > 0:
        for i in aprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")

    print("\nMaterias reprobadas:")

    if len(reprobadas) > 0:
        for i in reprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")

    print("\nMateria con mejor calificación:")
    print(f"{materias[indice_max]} ({calificaciones[indice_max]})")

    print("\nMateria con peor calificación:")
    print(f"{materias[indice_min]} ({calificaciones[indice_min]})")


def main():

    print("-" * 50)
    print("     CALCULADORA DE PROMEDIOS")
    print("-" * 50)

    # Nombre del alumno
    nombre = input("\nIngresa el nombre del alumno: ")

    # Ingreso de datos
    materias, calificaciones = ingresar_calificaciones()

    # Validar lista vacía
    if len(materias) == 0:
        print("\nNo se ingresaron materias.")
        print("Fin del programa.")
        return

    # Procesar datos
    promedio = calcular_promedio(calificaciones)

    aprobadas, reprobadas = determinar_estado(calificaciones)

    indice_max, indice_min = encontrar_extremos(calificaciones)

    # Determinar estado general
    estado = estado_general(promedio)

    # Mostrar resultados
    mostrar_resumen(
        nombre,
        materias,
        calificaciones,
        promedio,
        estado,
        aprobadas,
        reprobadas,
        indice_max,
        indice_min
    )




# Ejecutar programa
if __name__ == "__main__":
    main()