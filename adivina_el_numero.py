# Mini proyecto ADIVINA EL NUMERO
# Se genera un numero aleatorio entre 1 a 100 y el usuario debe adivinar el numero
import random
import time

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
    puntaje_total = 0

    print("-" * 40)
    print("🎯 ¡Bienvenido a Adivina el Número! 🎯")
    print("Estoy pensando en un número entre 1 y 100.")
    print("-" * 40)
    
    # Bucle de la run
    while True:
        numero_secreto = random.randint(1,100)
        intentos = 0
        minimo = 1
        maximo = 100
        max_intentos = 0
        
        nivel = input("Elige dificultad: (f)ácil, (n)ormal, (d)ifícil, (i)mposible: ").lower()

        if nivel == "f":
            max_intentos = 20
        elif nivel == "n":
            max_intentos = 15
        elif nivel == "d":
            max_intentos = 10
        elif nivel == "i":
            max_intentos = 5
        else:
            max_intentos = 15


        print("\n" + "-" * 40)
        print("¡Nueva partida! ¡Buena suerte!")
        print("-" * 40)

        print("Pensando un numero", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()

        # Bucle de la adivinanza
        while True:
            n = pedir_numero()
            intentos += 1
            if n == numero_secreto:
                if 1 <= intentos <= 3:
                    print(f"¡Increíble! ¡Adivinaste el número secreto: {numero_secreto}, en apenas {intentos} intentos!")
                    puntaje_total += 5
                elif 4 <= intentos <= 7:
                    print(f"¡Increíble! ¡Adivinaste el número secreto: {numero_secreto}, en apenas {intentos} intentos!")
                    puntaje_total += 3
                elif intentos >= 8:
                    print(f"¡CORRECTO! Adivinaste el número secreto: {numero_secreto}, en {intentos} intentos.")
                    puntaje_total += 1
                break
            elif n < numero_secreto:
                print(f"Mayor que {n}")
                minimo = n + 1
                print(f"Pista: el número está entre {minimo} y {maximo}.")
            else:
                print(f"Menor que {n}")
                maximo = n - 1
                print(f"Pista: el número está entre {minimo} y {maximo}.")

            
            diferencia = abs(numero_secreto - n)
            if diferencia <= 5:
                print("🔥 Muy caliente")
            elif diferencia <= 15:
                print("🔥 Caliente")
            elif diferencia <= 30:
                print("❄️ Frío")
            else:
                print("🥶 Muy frío")

            if intentos >=  max_intentos:
                print(f"No lograste Adivinar antes de {max_intentos} intentos. PERDISTE😈😈😈")
                break
            


        continuar = input("Desea continuar jugando (s/n): ")
        if continuar.lower() != "s":
            print("\n" + "-" * 40)
            print(f"🎉 Gracias por jugar Adivina el Número, Tu Puntaje fue de: {puntaje_total} 🎉")
            print("¡Hasta la próxima!")
            print("-" * 40)

            break

main()