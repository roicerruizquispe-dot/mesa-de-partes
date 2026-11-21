import datos


def cargar_archivo():
    for arreglo in (datos.codigos, datos.remitentes, datos.tipos, datos.asuntos,
                    datos.areas, datos.fechas_ingreso, datos.fechas_salida):
        arreglo.clear()
    try:
        archivo = open(datos.ARCHIVO, "r", encoding="utf-8")
    except FileNotFoundError:
        return  # todavía no existe el archivo, se empieza vacío
    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split("|")
        if len(partes) == 7 and partes[0].isdigit():
            datos.codigos.append(int(partes[0]))
            datos.remitentes.append(partes[1])
            datos.tipos.append(partes[2])
            datos.asuntos.append(partes[3])
            datos.areas.append(partes[4])
            datos.fechas_ingreso.append(partes[5])
            datos.fechas_salida.append(partes[6])
        else:
            print("Aviso: se omitió una línea con formato incorrecto.")
    archivo.close()


def guardar_archivo():
    archivo = open(datos.ARCHIVO, "w", encoding="utf-8")
    for i in range(datos.cantidad()):
        campos = [str(datos.codigos[i]), datos.remitentes[i], datos.tipos[i],
                  datos.asuntos[i], datos.areas[i],
                  datos.fechas_ingreso[i], datos.fechas_salida[i]]
        archivo.write("|".join(campos) + "\n")
    archivo.close()