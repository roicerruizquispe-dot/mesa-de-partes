ARCHIVO = "expedientes.txt"
TIPOS = ["solicitud", "afiche", "resolución", "oficio", "carta"]
AREAS = ["dirección", "plana docente", "padres de familia", "otro"]

codigos = []
remitentes = []
tipos = []
asuntos = []
areas = []
fechas_ingreso = []
fechas_salida = []


def cantidad():
    # cuántos expedientes hay registrados (reemplaza a la variable global "total")
    return len(codigos)