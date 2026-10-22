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
# ---------- REGISTRO (Figura 2) ----------
def registrar_tramite():
    global total
    print("\n--- REGISTRAR TRÁMITE ---")
    remitente = pedir_texto("Nombre del remitente: ")
    tipo = pedir_opcion("Tipo de documento", TIPOS)
    asunto = pedir_texto("Asunto: ")
    area = pedir_opcion("Área de destino", AREAS)

    # el código correlativo es total + 1
    codigos.append(total + 1)
    remitentes.append(remitente)
    tipos.append(tipo)
    asuntos.append(asunto)
    areas.append(area)
    fechas_ingreso.append(date.today().strftime("%d/%m/%Y"))
    fechas_salida.append("pendiente")
    total = total + 1
    guardar_archivo()  # se guarda en el archivo cada vez que se registra
    mostrar_ficha(total - 1, "CARGO DE RECEPCIÓN")
def mostrar_ficha(i, titulo="FICHA DEL EXPEDIENTE"):
    print("\n===== " + titulo + " =====")
    print("Código          :", str(codigos[i]).zfill(4))
    print("Remitente       :", remitentes[i])
    print("Documento       :", tipos[i])
    print("Asunto          :", asuntos[i])
    print("Área de destino :", areas[i])
    print("Fecha de ingreso:", fechas_ingreso[i])
    print("Fecha de salida :", fechas_salida[i])
    print("==============================")
# ---------- BÚSQUEDA SECUENCIAL (Figura 3) ----------
def buscar_secuencial(codigo_buscado):
    # recorre el arreglo desde i = 0; devuelve la posición o -1
    i = 0
    while i < total:
        if codigos[i] == codigo_buscado:
            return i
        i = i + 1
    return -1
def buscar_expediente():
    print("\n--- BUSCAR EXPEDIENTE ---")
    codigo = pedir_entero("Código del expediente a buscar: ", 1, 999999)
    # ---------- ORDENAMIENTO POR SELECCIÓN (Figura 4) ----------
def intercambiar(a, b):
    # cambia la posición a con la b en TODOS los arreglos,
    # así los datos de un mismo expediente no se separan
    todos = [codigos, remitentes, tipos, asuntos, areas, fechas_ingreso, fechas_salida]
    for arreglo in todos:
        auxiliar = arreglo[a]
        arreglo[a] = arreglo[b]
        arreglo[b] = auxiliar
def ordenar_seleccion():
    i = 0
    while i < total - 1:
        minimo = i
        j = i + 1
        while j < total:
            if codigos[j] < codigos[minimo]:
                minimo = j
            j = j + 1
        if minimo != i:
            intercambiar(i, minimo)
        i = i + 1
def mostrar_reporte():
    print("\n--- REPORTE DE EXPEDIENTES (ordenado por código) ---")
    if total == 0:
        print("No hay expedientes registrados.")
        return
    print("COD   REMITENTE           DOCUMENTO    ASUNTO                    DESTINO            INGRESO")
    for i in range(total):
        print(str(codigos[i]).zfill(4).ljust(6) + remitentes[i][:18].ljust(20) +
              tipos[i].ljust(13) + asuntos[i][:24].ljust(26) +
              areas[i][:17].ljust(19) + fechas_ingreso[i])
    print("Total de expedientes:", total)
# ---------- PROGRAMA PRINCIPAL (Figura 1) ----------
def main():
    cargar_archivo()
    print("Expedientes cargados desde el archivo:", total)
    opcion = 0
    while opcion != 4:
        print("\n========== MESA DE PARTES DIGITAL ==========")
        print("1. Registrar trámite")
        print("2. Buscar expediente por código")
        print("3. Ordenar por código y mostrar reporte")
        print("4. Guardar y salir")
        opcion = pedir_entero("Elija una opción: ", 1, 4)
        if opcion == 1:
            registrar_tramite()
        elif opcion == 2:
            buscar_expediente()
        elif opcion == 3:
            ordenar_seleccion()
            mostrar_reporte()
        else:
            guardar_archivo()
            print("Datos guardados en", ARCHIVO, "- Hasta pronto.")
main()
    posicion = buscar_secuencial(codigo)
    if posicion == -1:
        print("Expediente no encontrado.")
    else:
        mostrar_ficha(posicion)
