import csv   # Importamos el módulo csv para trabajar con archivos CSV
import os # Importamos el módulo os para trabajar con rutas de archivos y directorios, permitiendonos trabajar con la ruta absoluta del archivo CSV de manera compatible entre diferentes sistemas operativos.


print("\n======== TRABAJO PRACTICO INTEGRADOR ========")
print("             ----Programacion 1----           \n")
print("¡Bienvenido al programa de gestión de países!\n")

print("Alumnos integrantes: Mateo Fernández, Nayla Benitez - Grupo 17\n")

# ==========================================
# CARGAR PAISES DESDE CSV
# ==========================================
# En esta funcion se carga la informacion de los paises extraida del archivo CSV y se almacena en una lista 
# de diccionarios.
def cargar_paises():

    paises = []  # Creamos una lista vacía para almacenar los países cargados desde el archivo CSV

    try:
        # Guardamos la ruta absoluta del archivo CSV utilizando el módulo os para asegurarnos de que funcione correctamente
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        # Construimos la ruta completa al archivo CSV utilizando os.path.join para garantizar la compatibilidad entre sistemas operativos
        ruta_csv = os.path.join(ruta_script, "..", "data", "paises.csv") 

        # Abrimos el CSV en modo lectura.
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            
            # Se crea un lector de CSV utilizando csv.DictReader, que leerá cada fila del archivo como un diccionario, donde las claves son los nombres de las columnas y los 
            # valores son los datos correspondientes...
            lector = csv.DictReader(
                archivo,
                delimiter=";"
            )

            for fila in lector:  # iteramos sobre cada fila del archivo CSV utilizando el lector de CSV

                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": normalizar_continente(fila["continente"])
                }

                paises.append(pais)

    # Estructura except en caso el archivo CSV no se encuentre, haya un error con la conversion de los numeros, o cualquier otro error al cargar el archivo.
    except FileNotFoundError: 
        print("Error: No se encontró el archivo CSV.")
    except ValueError as e:
        print(f"Error: Problema al convertir datos numéricos: {e}")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")

    return paises

# Funcion auxilir que normaliza el nombre de los continentes ingresados, para evitar diferencias de mayúsculas/minúsculas, espacios adicionales, o cualquier otra variación 
# que pueda dificultar la comparación a los efectos estadisticos y comparativos.
def normalizar_continente(continente):
    """Normaliza el nombre del continente para evitar diferencias de mayúsculas/minúsculas."""
    return continente.strip().title()


# ==========================================
# GUARDAR PAISES EN CSV
# ==========================================
# Funcion que se encarga de guardar la informacion de los paises en el archivo CSV, utilizando el modulo csv para escribir los datos en el formato correcto.
def guardar_paises(paises):

    # Obtener la ruta absoluta del archivo CSV
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(ruta_script, "..", "data", "paises.csv")

    # Abrimos el CSV en modo escritura, lo que sobrescribirá el contenido existente. Si el archivo no existe, se creará uno nuevo.
    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:

        # Valores que representan los nombres de las columnas en el archivo CSV, que corresponden a las CLAVES de los diccionarios que representan cada país.
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

        escritor.writeheader() # Escribimos la fila de encabezado en el archivo CSV utilizando el método writeheader() del escritor de CSV.

        # Se itera sobre la lista de países y se escribe cada país en el archivo CSV utilizando el método writerow() del escritor de CSV, que toma un diccionario como 
        # argumento y escribe los valores correspondientes a las claves especificadas en fieldnames.
        for pais in paises:
            escritor.writerow(pais)


# ==========================================
# MOSTRAR TODOS LOS PAISES
# ==========================================
# Funcion que nos trae en la terminal la informacion de todos los paises registrados, mostrando su nombre, poblacion, superficie y continente al que pertenecen.

def mostrar_paises(paises):

    print("\n===== LISTA DE PAISES =====\n")

    if not paises:  
        print("No hay países registrados.\n")
        return

    # Bloque que itera sobre la informacion de cada pais en la lista de paises, e imprime en pantalla su nombre, poblacion, superficie y continente al que pertenecen.
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
# Funcion que se encarga de agregar un nuevo pais a la lista de paises, solicitando al usuario que ingrese el nombre, poblacion, superficie y continente del nuevo pais, 
# y luego guardando la informacion actualizada en el archivo CSV.
def agregar_pais(paises):

    nombre = input("Nombre del país: ").strip()
    continente = normalizar_continente(input("Continente: ").strip())

    # Validaciones con bloques try/except para asegurarnos de que el usuario ingrese datos válidos, como un nombre y continente no vacíos, y que la población y superficie 
    # sean números enteros positivos.
    try:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if not continente:
            raise ValueError("El continente no puede estar vacío.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    while True:
        try:
            poblacion = int(input("Población: "))
        except ValueError:
            print("Error: La población debe ser un número entero válido.")
            continue

        if poblacion <= 0:
            print("Error: La población debe ser un número entero positivo.")
            continue

        break

    while True:
        try:
            superficie = int(input("Superficie: "))
        except ValueError:
            print("Error: La superficie debe ser un número entero válido.")
            continue

        if superficie <= 0:
            print("Error: La superficie debe ser un número entero positivo.")
            continue
        break  

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais) # Se agrega el nuevo país a la lista de países utilizando el método append().

    guardar_paises(paises) # Se llama a guardar_paises() para guardar la lista ACTUALIZADA de países en el archivo CSV, que contiene el nuevo ingresado. 

    print("País agregado correctamente.")


# ==========================================
# ACTUALIZAR PAIS
# ==========================================
# Funcion que actualiza informacion de un pais determinado, solicitando nuevos datos de poblacion y superficie. 
def actualizar_pais(paises):

    while True:
        nombre = input(
            "Ingrese el nombre del país: "
        ).strip()

        if not nombre: # Si el usuario ingresa un dato vacio, arroja un mensaje de error.
            print("Error: el nombre no puede estar vacío.")
            continue 

        for pais in paises:
            # Se compara el nombre ingresado por el usuario con el nombre de cada país en la lista de países, utilizando una comparación que ignora mayúsculas y minúsculas para 
            # facilitar la búsqueda. 
            if pais["nombre"].lower() == nombre.lower():
                while True:
                    try:
                        poblacion = int(input("Nueva población: "))
                    except ValueError:
                        print("Error: La población debe ser un número entero válido.")
                        continue

                    # Validación para asegurarnos de que la población ingresada sea un número entero positivo. Si no lo es, se muestra un mensaje de error y se detiene la 
                    # ejecución de la función.
                    if poblacion <= 0:
                        print("Error: La población debe ser un número entero positivo.")
                        continue
                    break

                while True:
                    try:
                        superficie = int(input("Nueva superficie: "))
                    except ValueError:
                        print("Error: La superficie debe ser un número entero válido.")
                        continue

                    # Validación para asegurarnos de que la superficie ingresada sea un número entero positivo. Si no lo es, se muestra un mensaje de error y se detiene la ejecución de 
                    # la función.
                    if superficie <= 0:
                        print("Error: La superficie debe ser un número entero positivo.")
                        continue
                    break

                # Se actualizan los valores de poblacion y superficie en la lista de paises. 
                pais["poblacion"] = poblacion
                pais["superficie"] = superficie

                guardar_paises(paises) # Se llama a guardar_paises() para guardar la lista ACTUALIZADA de países en el archivo CSV, que contiene los nuevos datos del país actualizado.

                print("Datos actualizados.")

                return
        break

    print("País no encontrado.")


# ==========================================
# BUSCAR PAIS
# ==========================================
# Funcion que busca un pais por su nombre, solicitando al usuario que ingrese el nombre del pais a buscar.
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

    # En caso la variable bandera "encontrado" siga siendo False, significa que no se encontraró el pais ingresado por el usuario, y se muestra un mensaje.
    if not encontrado:
        print("No se encontraron resultados.")
    print()


# ==========================================
# FILTRAR POR CONTINENTE
# ==========================================
# Funcion que filtra los paises por continente, solicitando al usuario que ingrese el nombre del continente a filtrar, y luego mostrando en pantalla la informacion de 
# sus paises correspondientes. 
def filtrar_continente(paises):

    continente = input(
        "Continente: "
    ).strip().casefold()

    # Variable bandera para verificar si se encontraron países que coincidan con el continente ingresado por el usuario. Si al finalizar la iteración sigue siendo False, se
    # muestra un mensaje indicando que no se encontraron resultados.
    encontrado = False

    print("\n===== RESULTADOS POR CONTINENTE =====\n")

    for pais in paises:

        if pais["continente"].casefold() == continente:

            print(
                f'Nombre: {pais["nombre"]} | '
                f'Población: {pais["poblacion"]} | '
                f'Superficie: {pais["superficie"]} km² | '
                f'Continente: {pais["continente"]}'
            )

            encontrado = True

    # En caso la variable bandera "encontrado" siga siendo False, significa que no se encontrarón países que coincidan con el continente ingresado por el usuario, y se muestra 
    # un mensaje.
    if not encontrado:
        print("No hay resultados.")
    print()


# ==========================================
# FILTRAR POR POBLACION
# ==========================================
# Funcion que filtra en pantalla los paises que tengan una poblacion dentro de un rango determinado, solicitando al usuario un valor minimo y maximo de rango.
def filtrar_poblacion(paises):

    while True : # Insistimos al usuario en ingresar un numero entero valido, para proseguir con el programa.
        try: 
            minimo = int(input("Población mínima: ") )
        except ValueError: 
            print("Error: La población debe ser un número entero válido.")
            continue
        if minimo < 0 : 
            print("Error: El numero minimo tiene que ser un entero positivo.")
            continue
        break

    while True: 
        try: 
            maximo = int(input("Población máxima: "))
        except ValueError:
            print("Error: La población debe ser un número entero válido.")
            continue
        if maximo < 0 : 
            print("Error: El numero maximo tiene que ser un entero positivo.")
            continue
        break


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
# Funcion que filtra en pantalla los paises que tengan una superficie dentro de un rango determinado, solicitando al usuario un valor minimo y maximo de rango.
def filtrar_superficie(paises):

    while True: 
        try:
            minimo = int(input("Superficie mínima: "))
        except ValueError: 
            print("Error: La superficie debe ingresarse con un número entero válido.")
            continue
        if minimo < 0 : 
            print("Error: La superficie minima tiene que ingresarse con un entero positivo.")
            continue
        break

    while True:
        try: 
            maximo = int(input("Superficie máxima: "))
        except ValueError:
            print("Error: La superficie debe ingresarse con un número entero válido.")
            continue
        if maximo < 0 : 
            print("Error: La superficie maxima tiene que ingresarse con un entero positivo.")
            continue
        break
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
# Funcion que ordena la lista de paises por su nombre en orden alfabetico, utilizando el metodo de ordenamiento BURBUJA, y luego muestra la lista ordenada en pantalla.
def ordenar_nombre(paises):

    for i in range(len(paises)):

        for j in range(len(paises) - 1):

            if paises[j]["nombre"] > paises[j + 1]["nombre"]:

                aux = paises[j]

                paises[j] = paises[j + 1]

                paises[j + 1] = aux

    # Se llama a la funcion mostrar_paises() para que retorne la lista de paises y los muestre en pantalla, pero esta vez ordenados por su nombre en orden alfabetico.
    mostrar_paises(paises)


# ==========================================
# ORDENAR POR POBLACION
# ==========================================
# Funcion que ordena la lista de paises por su poblacion en orden ascendente, utilizando el metodo de ordenamiento BURBUJA, y luego muestra la lista ordenada en pantalla.
def ordenar_poblacion(paises):

    for i in range(len(paises)):

        for j in range(len(paises) - 1):

            if paises[j]["poblacion"] > paises[j + 1]["poblacion"]:

                aux = paises[j]

                paises[j] = paises[j + 1]

                paises[j + 1] = aux
    # Se llama a la funcion mostrar_paises() para que retorne la lista de paises y los muestre en pantalla, pero esta vez ordenados por su poblacion en orden ascendente.
    mostrar_paises(paises)


# ==========================================
# ORDENAR POR SUPERFICIE
# ==========================================
# Funcion que ordena la lista de paises por su superficie, solicitando al usuario si desea ordenarlos en orden ascendente o descendente, utilizando el metodo de 
# ordenamiento BURBUJA, y luego muestra la lista ordenada en pantalla.
def ordenar_superficie(paises):

    
    opcion = input(
        "1-Ascendente | 2-Descendente: "
    ).strip()

    for i in range(len(paises)):

        for j in range(len(paises) - 1):

            match opcion :
                case "1":

                    if paises[j]["superficie"] > paises[j + 1]["superficie"]:

                        aux = paises[j]

                        paises[j] = paises[j + 1]

                        paises[j + 1] = aux

                case "2":

                    if paises[j]["superficie"] < paises[j + 1]["superficie"]:

                        aux = paises[j]

                        paises[j] = paises[j + 1]

                        paises[j + 1] = aux
                case _:
                    print("Opción inválida. Vuelva a intentarlo ingresando 1 o 2 (1-Ascendente | 2-Descendente).")
                    return
    # Se llama a la funcion mostrar_paises() para que retorne la lista de paises y los muestre en pantalla, pero esta vez ordenados por su superficie, ya sea en orden 
    # ascendente o descendente segun la opcion ingresada por el usuario.
    mostrar_paises(paises)


# ==========================================
# ESTADISTICAS
# ==========================================
# Funcion que muestra estadisticas sobre los paises registrados, como el pais con mayor y menor poblacion, el promedio de poblacion y superficie, y la cantidad de paises 
# por continente.
def mostrar_estadisticas(paises):

    # Valores comparativos iniciales para encontrar los paises con mayor y menor poblacion, utilizando el primer pais de la lista como referencia inicial. Luego se itera sobre 
    # la lista de paises para comparar cada uno con los valores actuales de mayor y menor poblacion, y actualizar estos valores si se encuentra un pais con una poblacion mayor 
    # o menor respectivamente.
    mayor = paises[0] 
    menor = paises[0]

    # Variables acumuladoras para calcular el promedio de poblacion y superficie, sumando los valores de cada pais durante la iteración, y luego dividiendo por la cantidad 
    # total de paises para obtener el promedio.
    suma_poblacion = 0
    suma_superficie = 0

    # Diccionario para contar la cantidad de paises por continente, donde las claves son los nombres de los continentes y los valores son los contadores que se incrementan 
    # cada vez que se encuentra un pais que pertenece a ese continente durante la iteración.
    continentes = {}

    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = normalizar_continente(pais["continente"])

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

    print("Mayor población:", mayor["nombre"])

    print("Menor población:", menor["nombre"])  
    

    print("Promedio población:", round(promedio_poblacion))

    print(f"Promedio superficie: {round(promedio_superficie, 2)} km²" )

    print("\nPaíses por continente:")

    # Imprimimos la cantidad de paises por continente iterando sobre el diccionario de continentes, donde cada clave es un continente y su valor 
    # es la cantidad de paises que pertenecen a ese continente.
    for continente in continentes: 

        print(continente,":", continentes[continente]) 


# ==========================================
# MENU
# ==========================================
# Funcion que muestra las opciones principales del menu a ejecutarse. 
def menu():

    paises = cargar_paises() # Guadamos en esta variable la lista de paises cargada desde el CSV - esta variable se pasará como argumento a las funciones que necesiten acceder 
    # a la lista de paises para mostrar, agregar, actualizar, buscar, filtrar, ordenar o mostrar estadisticas sobre los paises registrados. Es el "corazon" de la aplicacion, 
    # ya que de ella dependen todas las demas funciones que la tienen como argumento. 


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


# Punto de entrada del programa, donde se llama a la funcion menu() para iniciar la aplicacion.
menu()
