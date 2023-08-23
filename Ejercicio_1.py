import random

def main():
    numero = random.randint(1, 100)
    

    while True:
        
        adivinar = input("Ingrese un numero: ")
        if int(adivinar) < numero:
            print("El número es menor al generado, inténtalo de nuevo.")
        elif int(adivinar) > numero:
            print("El número es mayor que el generado, inténtalo de nuevo.")
        elif int(adivinar) == numero:
            print("¡Has adivinado el número!,¡FELICIDADES!")
            break
            

    
if __name__ == "__main__":
    main()