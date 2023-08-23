def palabra_mas_larga(palabras):
    longitud_palabra = 0
    palabra_larga = ""
    for palabra in palabras:
        longitud = len(palabra)
        if longitud > longitud_palabra:
            longitud_palabra = longitud
            palabra_larga = palabra
    return palabra_larga

def main():
    num = int(input("Ingrese la cantidad de palabras que desea ingresar: "))
    palabras = []

    for i in range(num):
        palabra = input("Ingrese la palabra que desee: ")
        palabras.append(palabra)
    
    palabra_larga = palabra_mas_larga(palabras)
    
    print("Palabras ingresadas:" + str(palabras))
    print("Palabra más larga:" + palabra_larga)

if __name__ == "__main__":
    main() 