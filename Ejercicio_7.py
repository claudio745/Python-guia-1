

def factorial(n):
    if n == 0 or n == 1:
        resultado  = 1
    elif n > 1:
        resultado = n*factorial(n-1)
    return resultado


def main():
    num = int(input("Ingrese el numero a calcular su factorial: "))
    fact = factorial(num)
    print("El facotorial del numero " + str(num) + " es: " + str(fact))


if __name__ == "__main__":
    main()