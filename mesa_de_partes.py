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
