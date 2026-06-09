import csv


# ==========================================
# CARGAR PAISES DESDE CSV
# ==========================================
def cargar_paises():

    paises = []

    try:

        with open("paises.csv", "r", encoding="utf-8") as archivo:

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
        print("No se encontró el archivo CSV.")

    return paises


# ==========================================
# GUARDAR PAISES EN CSV
# ==========================================
def guardar_paises(paises):

    with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:

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

    for pais in paises:

        if texto in pais["nombre"].lower():

            print(pais)

            encontrado = True

    if not encontrado:
        print("No se encontraron resultados.")


# ==========================================
# FILTRAR POR CONTINENTE
# ==========================================
def filtrar_continente(paises):

    continente = input(
        "Continente: "
    ).lower()

    encontrado = False

    for pais in paises:

        if pais["continente"].lower() == continente:

            print(pais)

            encontrado = True

    if not encontrado:
        print("No hay resultados.")


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

    for pais in paises:

        if minimo <= pais["poblacion"] <= maximo:

            print(pais)


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

    for pais in paises:

        if minimo <= pais["superficie"] <= maximo:

            print(pais)


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
        round(promedio_poblacion, 2)
    )

    print(
        "Promedio superficie:",
        round(promedio_superficie, 2)
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
        print("8. Ordenar por nombre")
        print("9. Ordenar por población")
        print("10. Ordenar por superficie")
        print("11. Mostrar estadísticas")
        print("0. Salir")

        opcion = input(
            "Seleccione una opción: "
        )

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais(paises)

        elif opcion == "5":
            filtrar_continente(paises)

        elif opcion == "6":
            filtrar_poblacion(paises)

        elif opcion == "7":
            filtrar_superficie(paises)

        elif opcion == "8":
            ordenar_nombre(paises)

        elif opcion == "9":
            ordenar_poblacion(paises)

        elif opcion == "10":
            ordenar_superficie(paises)

        elif opcion == "11":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()
