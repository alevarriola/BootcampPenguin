import random

def nivel_dificultar():
    print("Vamos a definir la dificultad!")
    print("Ingrese (F) para facil, (M) para mediano, (D) para dificil\n")
    dificultad = input("Ingrese dificultad F, M, D").lower()
    if dificultad == "f":
        print("Dificultad facil seleccionada!")
        return 5, 10
    elif dificultad == "m":
        print("Dificultad mediana seleccionada!")
        return 3, 10
    elif dificultad == "d":
        print("Dificultad dificil seleccionada!")
        return 3, 20
    else:
        print("Por hacerte el gracioso, dificultad extrema")
        return 1, 30

print("Bienvenido a 'Adivina un numero'!!! ")
print("Trata de adivinar el numero secreto\n")

while True:

    intentos, numero_maximo = nivel_dificultar()
    numero_secreto = random.randint(1, numero_maximo)

    print(f"El numero secreto va del 1 al {numero_maximo}")
    print(f"Tienes {intentos} intentos \n")

    while intentos > 0:

        try:
            numero_ingresado = int(input("Ingresa un numero: "))
        except ValueError: #En el caso de que de un VAlueError al ingresar una letra, no rompa el codigo
            print("Eso no es un numero picaron!\n")
            continue

        if numero_ingresado > numero_maximo or numero_ingresado <= 0:
            print(f"Recuerda solo ingresar numeros del 1 al {numero_maximo}\n")
        
        elif numero_ingresado == numero_secreto:
            intentos = intentos - 1
            print(f"Felicidades! haz ganado! el numero secreto era {numero_secreto}")
            print(f"Te han sobrado {intentos} intentos!")
            print("Que grande!\n")
            break

        else:
            intentos = intentos - 1
            if numero_ingresado > numero_secreto:
                print(f"El numero {numero_ingresado} es mayor al numero secreto!")
                print(f"Intentalo de vuelta, te quedan {intentos} intentos\n")
            elif numero_ingresado < numero_secreto:
                print(f"El numero {numero_ingresado} es menor al numero secreto!")
                print(f"Intentalo de vuelta, te quedan {intentos} intentos\n")

    if intentos == 0:
        print(f"Haz fallado garrafalmente. el numero secreto era {numero_secreto}")
        print("Mejor suerte la proxima!\n")

    print("Quieres jugar de nuevo? (s/n)")
    respuesta = input("Jugamos? (s/n)\n").lower()

    if respuesta != "s":
        print("Gracias por jugar! Nos vemossss")
        break
