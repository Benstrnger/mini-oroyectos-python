# Mini proyecto ADIVINA EL NUMERO
# Se genera un numero aleatorio entre 1 a 100 y el usuario debe adivinar el numero
import random

def pedir_numero():
    while True:
        n = input("Ingrese un numero: ")
        try:
            numero = int(n)
            if 1 <= numero <=100:
                return numero
            else:
                print("ERROR: El numero debe estar entre 1 y 100.")
        except ValueError:
            print("ERROR: Ingresó un valor no válido")

def main():
    print("-" * 40)
    print("🎯 ¡Bienvenido a Adivina el Número! 🎯")
    print("Estoy pensando en un número entre 1 y 100.")
    print("-" * 40)

    while True:
        numero_secreto = random.randint(1,100)
        intentos = 0
        minimo = 1
        maximo = 100
        modo_dificil = False

        modo = input("¿Desea jugar en modo difícil (s/n)? ").lower()
        if modo == "s":
            modo_dificil = True
        else:
            modo_dificil = False

        print("\n" + "-" * 40)
        print("¡Nueva partida! ¡Buena suerte!")
        print("-" * 40)

        # Bucle de adivinanza
        while True:
            n = pedir_numero()
            intentos += 1
            if n > numero_secreto:
                print(f"Menor que {n}")
                maximo = n - 1
                print(f"Pista: el número está entre {minimo} y {maximo}.")
            elif n < numero_secreto:
                print(f"Mayor que {n}")
                minimo = n + 1
                print(f"Pista: el número está entre {minimo} y {maximo}.")
            else:
                if intentos <= 5:
                    print(f"¡Increíble! ¡Adivinaste el número secreto: {numero_secreto}, en apenas {intentos} intentos!")
                else:
                    print(f"¡CORRECTO! Adivinaste el número secreto: {numero_secreto}, en {intentos} intentos.")
                break
            if modo_dificil == True and intentos >= 10:
                print("No lograste Adivinar antes de los 10 intentos. PERDISTE😈😈😈")
                break
            
        continuar = input("Desea continuar jugando (s/n): ")
        if continuar.lower() != "s":
            print("\n" + "-" * 40)
            print("🎉 Gracias por jugar Adivina el Número 🎉")
            print("¡Hasta la próxima!")
            print("-" * 40)

            break

main()