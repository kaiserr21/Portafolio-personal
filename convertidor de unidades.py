def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def kilometros_a_millas(km):
    return km * 0.621371

def kg_a_libras(kg):
    return kg * 2.20462

def metros_a_altura_usa(metros):
    total_pulgadas = metros * 39.3701
    pies = int(total_pulgadas // 12)
    pulgadas = round(total_pulgadas % 12)
    return pies, pulgadas


print("=== Convertidor de Unidades ===")

while True:
    print("\nSelecciona una opción:")
    print("1. Celsius a Fahrenheit")
    print("2. Kilómetros a Millas")
    print("3. Kilogramos a Libras")
    print("4. Altura metros a formato USA")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "5":
        print("Adiós")
        break

    try:
        valor = float(input("Ingresa el valor: "))

        if opcion == "1":
            print("Resultado:", celsius_a_fahrenheit(valor), "°F")

        elif opcion == "2":
            print("Resultado:", kilometros_a_millas(valor), "millas")

        elif opcion == "3":
            print("Resultado:", kg_a_libras(valor), "libras")

        elif opcion == "4":
            pies, pulgadas = metros_a_altura_usa(valor)
            print(f"Resultado: {pies}'{pulgadas}\"")

        else:
            print("Opción inválida")

    except:
        print("Ingresa un número válido")