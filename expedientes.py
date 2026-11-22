# expedientes.py - Registro y búsqueda secuencial de expedientes (Figuras 2 y 3).
from datetime import date

import datos
from validacion import pedir_texto, pedir_entero, pedir_opcion
from archivo import guardar_archivo
from reportes import mostrar_ficha


def generar_codigo():
    # máximo código existente + 1: sigue siendo único aunque se haya omitido una línea dañada
    mayor = 0
    for c in datos.codigos:
        if c > mayor:
            mayor = c
    return mayor + 1


def registrar_tramite():
    print("\n--- REGISTRAR TRÁMITE ---")
    remitente = pedir_texto("Nombre del remitente: ", 3, True)
    tipo = pedir_opcion("Tipo de documento", datos.TIPOS)
    asunto = pedir_texto("Asunto: ", 5, True)
    area = pedir_opcion("Área de destino", datos.AREAS)

    datos.codigos.append(generar_codigo())
    datos.remitentes.append(remitente)
    datos.tipos.append(tipo)
    datos.asuntos.append(asunto)
    datos.areas.append(area)
    datos.fechas_ingreso.append(date.today().strftime("%d/%m/%Y"))
    datos.fechas_salida.append("pendiente")
    guardar_archivo()  # se guarda en el archivo cada vez que se registra
    mostrar_ficha(datos.cantidad() - 1, "CARGO DE RECEPCIÓN")


def buscar_secuencial(codigo_buscado):
    # recorre el arreglo desde i = 0; devuelve la posición o -1
    i = 0
    while i < datos.cantidad():
        if datos.codigos[i] == codigo_buscado:
            return i
        i = i + 1
    return -1


def buscar_expediente():
    print("\n--- BUSCAR EXPEDIENTE ---")
    codigo = pedir_entero("Código del expediente a buscar: ", 1, 999999)
    posicion = buscar_secuencial(codigo)
    if posicion == -1:
        print("Expediente no encontrado.")
    else:
        mostrar_ficha(posicion)