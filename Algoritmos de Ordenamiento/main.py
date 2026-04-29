import time


def leer_archivo():
    

    with open("datos.txt", "r") as archivo:
        numeros = archivo.read().split()

    numeros = [int(num) for num in numeros]

    return numeros


def menu():
    

    while True:
        print("\n ")
        print("  ORDENAMIENTO -> ALGORITMO DE MEZCLA NATURAL")
        print(" ")
        print("Se extraerán los números del archivo")
        print("datos.txt y serán ordenados de forma ascendente o descendente. Elegir Opción.\n")

        print("Seleccione el tipo de orden para ordenarlos:")
        print("1. Ascendente")
        print("2. Descendente")

        opcion = input("\nSeleccione una opción 1 o 2: ").strip()

        if opcion == "1":
            return "ascendente"

        elif opcion == "2":
            return "descendente"

        else:
            print("\nHubo un error en la selección del tipo de orden.")
            print("Por favor intenta de nuevo.\n")


def dividir_corridas(lista):
    

    corridas = []
    corrida_actual = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            corrida_actual.append(lista[i])
        else:
            corridas.append(corrida_actual)
            corrida_actual = [lista[i]]

    corridas.append(corrida_actual)

    return corridas


def mezclar(lista1, lista2):
    

    resultado = []
    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])

    return resultado


def mezcla_natural(lista):
    

    while True:
        corridas = dividir_corridas(lista)

        if len(corridas) == 1:
            break

        nueva_lista = []

        for i in range(0, len(corridas), 2):
            if i + 1 < len(corridas):
                fusionada = mezclar(corridas[i], corridas[i + 1])
                nueva_lista.extend(fusionada)
            else:
                nueva_lista.extend(corridas[i])

        lista = nueva_lista

    return lista


def guardar_resultado(lista, tiempo, tipo_orden):
    

    with open("numeros_ordenados.txt", "w") as archivo:
        archivo.write("NUMEROS ORDENADOS\n")
        archivo.write(" \n")
        archivo.write(f"Tipo de orden: {tipo_orden.capitalize()}\n")
        archivo.write(f"Tiempo de ejecución: {tiempo:.2f} milisegundos\n\n")

        for numero in lista:
            archivo.write(f"{numero}\n")


opcion = menu()

numeros = leer_archivo()

print(f"\nSe leyeron {len(numeros)} números correctamente.")

inicio = time.time()

numeros_ordenados = mezcla_natural(numeros)

if opcion == "descendente":
    numeros_ordenados.reverse()

fin = time.time()

tiempo_ms = (fin - inicio) * 1000


guardar_resultado(numeros_ordenados, tiempo_ms, opcion)

print("\nOrdenamiento completado.")
print(f"El orden seleccionado fue: {opcion.capitalize()}")
print(f"El tiempo de ejecución fue: {tiempo_ms:.2f} milisegundos")
print("Archivo generado correctamente: numeros_ordenados.txt")