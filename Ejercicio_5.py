def main():
    palabra = str(input("Ingrese una palabra: "))
    letra = str(input("Ingrese una letra: "))
    contador = 0
    for letras in palabra:
        if letras == letra:
            contador += 1 

    if contador == 1:
        print("La letra " + letra + " aparece " + str(contador) + " vez en la palabra " + palabra)
    else:
        print("La letra " + letra + " aparece " + str(contador) + " veces en la palabra " + palabra)
    



if __name__ == "__main__":
    main()
    