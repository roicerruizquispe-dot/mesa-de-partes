import datos


def mostrar_ficha(i, titulo="FICHA DEL EXPEDIENTE"):
    print("\n===== " + titulo + " =====")
    print("Código          :", str(datos.codigos[i]).zfill(4))
    print("Remitente       :", datos.remitentes[i])
    print("Documento       :", datos.tipos[i])
    print("Asunto          :", datos.asuntos[i])
    print("Área de destino :", datos.areas[i])
    print("Fecha de ingreso:", datos.fechas_ingreso[i])
    print("Fecha de salida :", datos.fechas_salida[i])
    print("==============================")


def mostrar_reporte():
    print("\n--- REPORTE DE EXPEDIENTES (ordenado por código) ---")
    total = datos.cantidad()
    if total == 0:
        print("No hay expedientes registrados.")
        return
    print("COD   REMITENTE           DOCUMENTO    ASUNTO                    DESTINO            INGRESO")
    for i in range(total):
        print(str(datos.codigos[i]).zfill(4).ljust(6) + datos.remitentes[i][:18].ljust(20) +
              datos.tipos[i].ljust(13) + datos.asuntos[i][:24].ljust(26) +
              datos.areas[i][:17].ljust(19) + datos.fechas_ingreso[i])
    print("Total de expedientes:", total)