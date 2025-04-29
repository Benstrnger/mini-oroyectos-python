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
    numero_secreto = random.randint(1,100)
    intentos = 0
    while True:
        n = pedir_numero() 
        if n > numero_secreto:
            print(f"Menor que {n}")
            intentos += 1
        elif n < numero_secreto:
            print(f"Mayor que {n}")
            intentos += 1
        else:
            print(f"¡CORRECTO! Adivinaste el número en {intentos} intentos.")
            break

main()