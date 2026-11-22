import datos


def intercambiar(a, b):
    # cambia la posición a con la b en TODOS los arreglos,
    # así los datos de un mismo expediente no se separan
    todos = [datos.codigos, datos.remitentes, datos.tipos, datos.asuntos,
             datos.areas, datos.fechas_ingreso, datos.fechas_salida]
    for arreglo in todos:
        auxiliar = arreglo[a]
        arreglo[a] = arreglo[b]
        arreglo[b] = auxiliar


def ordenar_seleccion():
    total = datos.cantidad()
    i = 0
    while i < total - 1:
        minimo = i
        j = i + 1
        while j < total:
            if datos.codigos[j] < datos.codigos[minimo]:
                minimo = j
            j = j + 1
        if minimo != i:
            intercambiar(i, minimo)
        i = i + 1