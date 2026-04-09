def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


print("=== Calculadora ===")

while True:
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "5":
        print("Adiós")
        break

    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))

            if opcion == "1":
                print("Resultado:", sumar(num1, num2))

            elif opcion == "2":
                print("Resultado:", restar(num1, num2))

            elif opcion == "3":
                print("Resultado:", multiplicar(num1, num2))

            elif opcion == "4":
                print("Resultado:", dividir(num1, num2))

        except:
            print("Ingresa números válidos")

    else:
        print("Opción inválida")

        