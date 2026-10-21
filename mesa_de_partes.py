# Mesa de partes digital - I.E. Andrés Avelino Cáceres (Baños del Inca, Cajamarca)
# Alternativa A: arreglos paralelos, archivo de texto con "|", búsqueda secuencial y selección.
from datetime import date
ARCHIVO = "expedientes.txt"
TIPOS = ["solicitud", "afiche", "resolución", "oficio", "carta"]
AREAS = ["dirección", "plana docente", "padres de familia", "otro"]
# Arreglos paralelos: la posición i de todos es el mismo expediente
codigos = []
remitentes = []
tipos = []
asuntos = []
areas = []
fechas_ingreso = []
fechas_salida = []
total = 0  # cuántos expedientes hay registrados
# ---------- VALIDACIÓN (Figura 2) ----------
def pedir_texto(mensaje):
    # repite hasta que el texto no esté vacío ni tenga el símbolo |
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("  Error: este campo no puede quedar vacío.")
        elif "|" in texto:
            print("  Error: no se puede usar el símbolo |.")
        else:
            return texto
def pedir_entero(mensaje, minimo, maximo):
    # pide un número entero entre minimo y maximo
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("  Error: ingrese un número entero.")
            continue
        if numero < minimo or numero > maximo:
            print("  Error: el número debe estar entre", minimo, "y", maximo)
        else:
            return numero
def pedir_opcion(titulo, opciones):
    # muestra una lista numerada y devuelve la opción elegida
    print(titulo + ":")
    for i in range(len(opciones)):
        print("  " + str(i + 1) + ". " + opciones[i])
    numero = pedir_entero("Elija una opción: ", 1, len(opciones))
    return opciones[numero - 1]
    # ---------- ARCHIVO DE TEXTO (Figuras 1 y 2) ----------
def cargar_archivo():
    global total
    total = 0
    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        return  # todavía no existe el archivo, se empieza vacío
    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split("|")
        if len(partes) == 7 and partes[0].isdigit():
            codigos.append(int(partes[0]))
            remitentes.append(partes[1])
            tipos.append(partes[2])
            asuntos.append(partes[3])
            areas.append(partes[4])
            fechas_ingreso.append(partes[5])
            fechas_salida.append(partes[6])
            total = total + 1
        else:
            print("Aviso: se omitió una línea con formato incorrecto.")
    archivo.close()
def guardar_archivo():
    archivo = open(ARCHIVO, "w", encoding="utf-8")
    for i in range(total):
        datos = [str(codigos[i]), remitentes[i], tipos[i], asuntos[i], areas[i], fechas_ingreso[i], fechas_salida[i]]
        linea = "|".join(datos)
        archivo.write(linea + "\n")
    archivo.close()
