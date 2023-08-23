def main():
    articulos = []
    precios = []
    while True:
        opcion = int(input("Si desea ingresar un articulo a la lista, ingrese 1, de lo contrario, ingrese cualquier otro numero: "))
        if opcion == 1:
            articulo = str(input("Ingrese un articulo a la lista: "))
            precio = int(input("Ingrese el valor del articulo: "))
            articulos.append(articulo)
            precios.append(precio)

        else:
            print("Hasta pronto.")
            break
        largo = len(articulos)

        for i in range(0, largo):
            print("El articulo " + articulos[i] + " tiene un valor de: " + str(precios[i]))

if __name__ == "__main__":
    main() 