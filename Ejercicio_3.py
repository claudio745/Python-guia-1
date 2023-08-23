def primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("no es primo " + str(n) + " es divisor")
            return False
    print("Su numero es primo")
    return True


def main():
    num = int(input("Ingrese un numero para saber si este es primo: "))
    primo(num)


if __name__ == "__main__":
    main()