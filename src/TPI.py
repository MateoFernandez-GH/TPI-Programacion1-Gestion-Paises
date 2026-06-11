import csv
import os


# ==========================================
# CARGAR PAISES DESDE CSV
# ==========================================
def cargar_paises():

    paises = []

    try:
        # Obtener la ruta absoluta del archivo CSV
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_csv = os.path.join(ruta_script, "..", "data", "paises.csv")

        with open(ruta_csv, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(
                archivo,
                delimiter=";"
            )

            for fila in lector:

                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:
        print("Error: No se encontró el archivo CSV.")
    except ValueError as e:
        print(f"Error: Problema al convertir datos numéricos: {e}")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    return paises


# ==========================================
# GUARDAR PAISES EN CSV
# ==========================================
def guardar_paises(paises):

    # Obtener la ruta absoluta del archivo CSV
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(ruta_script, "..", "data", "paises.csv")

    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos,
            delimiter=";"
        )

        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)


# ==========================================
# MOSTRAR TODOS LOS PAISES
# ==========================================
def mostrar_paises(paises):

    print("\n===== LISTA DE PAISES =====\n")

    if not paises:
        print("No hay países registrados.\n")
        return

    for pais in paises:

        print(
            f'Nombre: {pais["nombre"]} | '
            f'Población: {pais["poblacion"]} | '
            f'Superficie: {pais["superficie"]} km² | '
            f'Continente: {pais["continente"]}'
        )


# ==========================================
# AGREGAR PAIS
# ==========================================
def agregar_pais(paises):

    nombre = input("Nombre del país: ").strip()

    while nombre == "":
        nombre = input("No puede estar vacío: ").strip()

    poblacion = int(input("Población: "))
    superficie = int(input("Superficie: "))

    continente = input("Continente: ").strip()

    while continente == "":
        continente = input("No puede estar vacío: ").strip()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    guardar_paises(paises)

    print("País agregado correctamente.")


# ==========================================
# ACTUALIZAR PAIS
# ==========================================
def actualizar_pais(paises):

    nombre = input(
        "Ingrese el nombre del país: "
    )

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            pais["poblacion"] = int(
                input("Nueva población: ")
            )

            pais["superficie"] = int(
                input("Nueva superficie: ")
            )

            guardar_paises(paises)

            print("Datos actualizados.")

            return

    print("País no encontrado.")


# ==========================================
# BUSCAR PAIS
# ==========================================
def buscar_pais(paises):

    texto = input(
        "Ingrese el nombre a buscar: "
    ).lower()

    encontrado = False

    print("\n===== RESULTADOS DE BÚSQUEDA =====\n")

    for pais in paises:

        if texto in pais["nombre"].lower():

            print(
                f'Nombre: {pais["nombre"]} | '
                f'Población: {pais["poblacion"]} | '
                f'Superficie: {pais["superficie"]} km² | '
                f'Continente: {pais["continente"]}'
            )

            encontrado = True

    if not encontrado:
        print("No se encontraron resultados.")
    print()


# ==========================================
# FILTRAR POR CONTINENTE
# ==========================================
def filtrar_continente(paises):

    continente = input(
        "Continente: "
    ).lower()

    encontrado = False

    print("\n===== RESULTADOS POR CONTINENTE =====\n")

    for pais in paises:

        if pais["continente"].lower() == continente:

            print(
                f'Nombre: {pais["nombre"]} | '
                f'Población: {pais["poblacion"]} | '
                f'Superficie: {pais["superficie"]} km² | '
                f'Continente: {pais["continente"]}'
            )

            encontrado = True

    if not encontrado:
        print("No hay resultados.")
    print()


# ==========================================
# FILTRAR POR POBLACION
# ==========================================
def filtrar_poblacion(paises):

    minimo = int(
        input("Población mínima: ")
    )

    maximo = int(
        input("Población máxima: ")
    )

    encontrado = False

    print("\n===== RESULTADOS POR POBLACIÓN =====\n")

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            print(
                f'Nombre: {pais["nombre"]} | '
                f'Población: {pais["poblacion"]} | '
                f'Superficie: {pais["superficie"]} km² | '
                f'Continente: {pais["continente"]}'
            )
            encontrado = True

    if not encontrado:
        print("No hay resultados.")
    print()


# ==========================================
# FILTRAR POR SUPERFICIE
# ==========================================
def filtrar_superficie(paises):

    minimo = int(
        input("Superficie mínima: ")
    )

    maximo = int(
        input("Superficie máxima: ")
    )

    encontrado = False

    print("\n===== RESULTADOS POR SUPERFICIE =====\n")

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            print(
                f'Nombre: {pais["nombre"]} | '
                f'Población: {pais["poblacion"]} | '
                f'Superficie: {pais["superficie"]} km² | '
                f'Continente: {pais["continente"]}'
            )
            encontrado = True

    if not encontrado:
        print("No hay resultados.")
    print()


# ==========================================
# ORDENAR POR NOMBRE
# ==========================================
def ordenar_nombre(paises):

    for i in range(len(paises)):

        for j in range(len(paises) - 1):

            if paises[j]["nombre"] > paises[j + 1]["nombre"]:

                aux = paises[j]

                paises[j] = paises[j + 1]

                paises[j + 1] = aux

    mostrar_paises(paises)


# ==========================================
# ORDENAR POR POBLACION
# ==========================================
def ordenar_poblacion(paises):

    for i in range(len(paises)):

        for j in range(len(paises) - 1):

            if paises[j]["poblacion"] > paises[j + 1]["poblacion"]:

                aux = paises[j]

                paises[j] = paises[j + 1]

                paises[j + 1] = aux

    mostrar_paises(paises)


# ==========================================
# ORDENAR POR SUPERFICIE
# ==========================================
def ordenar_superficie(paises):

    opcion = input(
        "1-Ascendente | 2-Descendente: "
    )

    for i in range(len(paises)):

        for j in range(len(paises) - 1):

            if opcion == "1":

                if paises[j]["superficie"] > paises[j + 1]["superficie"]:

                    aux = paises[j]

                    paises[j] = paises[j + 1]

                    paises[j + 1] = aux

            elif opcion == "2":

                if paises[j]["superficie"] < paises[j + 1]["superficie"]:

                    aux = paises[j]

                    paises[j] = paises[j + 1]

                    paises[j + 1] = aux

    mostrar_paises(paises)


# ==========================================
# ESTADISTICAS
# ==========================================
def mostrar_estadisticas(paises):

    mayor = paises[0]
    menor = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = (
        suma_poblacion / len(paises)
    )

    promedio_superficie = (
        suma_superficie / len(paises)
    )

    print("\n===== ESTADISTICAS =====\n")

    print(
        "Mayor población:",
        mayor["nombre"]
    )

    print(
        "Menor población:",
        menor["nombre"]
    )

    print(
        "Promedio población:",
        round(promedio_poblacion)
    )

    print(
        f"Promedio superficie: {round(promedio_superficie, 2)} km²"
    )

    print("\nPaíses por continente:")

    for continente in continentes:

        print(
            continente,
            ":",
            continentes[continente]
        )


# ==========================================
# MENU
# ==========================================
def menu():

    paises = cargar_paises()

    while True:

        print("\n===== MENU =====")

        print("1. Mostrar países")
        print("2. Agregar país")
        print("3. Actualizar país")
        print("4. Buscar país")
        print("5. Filtrar por continente")
        print("6. Filtrar por población")
        print("7. Filtrar por superficie")
        print("8. Ordenar por nombre (A-Z)")
        print("9. Ordenar por población (de menor a mayor)")
        print("10. Ordenar por superficie")
        print("11. Mostrar estadísticas")
        print("0. Salir")

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        match opcion:
            case "1":
                mostrar_paises(paises)

            case "2":
                agregar_pais(paises)

            case "3":
                actualizar_pais(paises)

            case "4":
                buscar_pais(paises)

            case "5":
                filtrar_continente(paises)

            case "6":
                filtrar_poblacion(paises)

            case "7":
                filtrar_superficie(paises)

            case "8":
                ordenar_nombre(paises)

            case "9":
                ordenar_poblacion(paises)

            case "10":
                ordenar_superficie(paises)

            case "11":
                mostrar_estadisticas(paises)

            case "0":
                print("Programa finalizado.\n")
                break

            case _:
                print("Opción inválida. Intente nuevamente")



menu()
