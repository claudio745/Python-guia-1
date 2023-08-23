def main():
    while True:
        palabras = []
        palabra = str(input("Ingrese la palabra: "))
        palabras.append(palabra)
        stop = 'salir'
        if palabra == stop:
            break
        else:
            print("la palabra es: " + palabra[::-1])



if __name__ == "__main__":
    main() 