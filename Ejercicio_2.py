def main():
    while True:

        print("""
            ¿Que conversion desea realizar?:
            1 - Centimetros -> Pulgadas
            2 - Metros -> Kilometros
            3 - Onzas -> Gramos
            4 - Milla -> Kilometro 
            5 - Celcius -> Fharenheit
            6 - Salir
        """)
        opcion = int(input("Ingrese la opcion correspondiente: "))

        if opcion == 1:
            medida = float(input("Ingrese la cantidad de Centimetros a convertir: "))
            conversion = medida / 2.54
            print("EL valor de " + str(medida) + " Centimetros en pulgadas es: " + str(conversion))
        elif opcion == 2:
            medida = float(input("Ingrese la cantidad de Metros a convertir: "))
            conversion = medida / 1000
            print("El valor de "+ str(medida) + " Metros en Kilometros es: " + str(conversion))
        elif opcion == 3:
            medida = float(input("Ingrese la cantidad de Onzas a convertir: "))
            conversion = medida * 28.35
            print("El valor de " + str(medida) + " Onzas en Gramos es: " + str(conversion))
        elif opcion == 4:
            medida = float(input("Ingrese la cantidad de millas a convertir: "))
            conversion = medida * 1.609
            print("El valor de " + str(medida) + " Millas en Kilometros es:  " + str(conversion))
        elif opcion == 5:
            medida = float(input("Ingrese la cantidad de Celcius a convertir: "))
            conversion = (medida * (9/5)) + 32
            print("El valor de " + str(medida) + " Celcius en Fharenheit es: " + str(conversion))
        elif opcion == 6:
            break


if __name__ == "__main__":

    main()
    