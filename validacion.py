def pedir_texto(mensaje, minimo=1, exigir_letras=False):
    # repite hasta que el texto sea válido: no vacío, sin "|", con longitud mínima
    # y (si se pide) con al menos una letra
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("  Error: este campo no puede quedar vacío.")
        elif "|" in texto:
            print("  Error: no se puede usar el símbolo |.")
        elif len(texto) < minimo:
            print("  Error: escriba al menos", minimo, "caracteres.")
        elif exigir_letras and not any(c.isalpha() for c in texto):
            print("  Error: el dato debe contener letras.")
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
