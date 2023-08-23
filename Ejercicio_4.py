def main():
    

        palabra_1 = str(input("Ingrese la 1ra palabra: "))
        palabra_2 = str(input("Ingrese la 2da palabra: "))

        if len(palabra_1) < 3 or len(palabra_2) < 3:
            print("Error, la palabra debe contener más de 3 letras!!")
        else:
            if palabra_1[-3:] == palabra_2[-3:]:
                print("Las palabras riman")
            elif palabra_1[-2:] == palabra_2[-2:]:
                print("Las palabras riman solo un poco")
            else:
                print("Las palabras no riman para nada, intente con otra.")

        



if __name__ == "__main__":
    main() 