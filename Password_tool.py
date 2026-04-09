import random
import string

def generar_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(longitud):
        password += random.choice(caracteres)

    return password


def validar_password(password):
    tiene_longitud = len(password) >= 8
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_minuscula = any(c.islower() for c in password)
    tiene_numero = any(c.isdigit() for c in password)
    tiene_simbolo = any(c in string.punctuation for c in password)

    puntuacion = sum([
        tiene_longitud,
        tiene_mayuscula,
        tiene_minuscula,
        tiene_numero,
        tiene_simbolo
    ])

    if puntuacion == 5:
        return "Fuerte"
    elif puntuacion >= 3:
        return "Media"
    else:
        return "Débil"


print("=== Generador y Validador de Contraseñas ===")

while True:
    try:
        longitud = int(input("Longitud de la contraseña (8-32 caracteres): "))

        if 8 <= longitud <= 32:
            break
        else:
            print("La longitud debe estar entre 8 y 32. Inténtalo de nuevo.")

    except ValueError:
        print("Ingresa un número válido.")

password = generar_password(longitud)

print("\nContraseña generada:")
print(password)

seguridad = validar_password(password)

print("\nNivel de seguridad:", seguridad)