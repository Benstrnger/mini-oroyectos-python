import random
def seleccionar_palabra(palabras):  
    palabra_secreta = random.choice(palabras)
    return palabra_secreta

def crear_tablero(palabra_secreta):
    tablero = []
    for _ in palabra_secreta:
        tablero.append("_")
    return tablero

def pedir_letra():
    while True:
        letra = input("Ingrese una letra: ").lower()
        if len(letra) == 1 and letra.isalpha():
            return letra
        else:
            print("\nEntrada invalida. Intente nuevamente.")
    
def actualizar_tablero(palabra_secreta, palabra_actual, letra):
    if letra in palabra_secreta.lower():
        for i in range(len(palabra_secreta)):
            if letra == palabra_secreta[i].lower():
                palabra_actual[i] = letra

def mostrar_tablero(palabra_actual, errores, letras_usadas):
        if len(letras_usadas) == 0:
            print(" ".join(palabra_actual), f"| Errores {errores}/6")
            print("--" * 30)
        else:
            print(" ".join(palabra_actual), f"| Errores {errores}/6")
            print("--" * 30)
            print("|","-".join(letras_usadas),"|")
            print("--" * 30)
def jugar_una_partida(palabras):
        errores = 0
        max_errores = 6
        letras_usadas = []

        palabra_secreta = seleccionar_palabra(palabras)

        tablero = crear_tablero(palabra_secreta)

        # Bucle de adivinanza
        while True:   
            mostrar_tablero(tablero, errores, letras_usadas)
            letra = pedir_letra()

            if letra in letras_usadas:
                print("Ya usaste esa letra.")
                continue
            if letra not in palabra_secreta.lower():
                errores += 1
                print(f"Errores: {errores}/6")
            actualizar_tablero(palabra_secreta, tablero, letra)
            if errores >= max_errores:
                print("Te quedaste sin intentos.")
                print()
                print(f"La palabra era: {palabra_secreta}")
                print()
                break
            if "_" not in tablero:
                print()
                print(f"Felicidades acertaste la palabra era: {palabra_secreta}")
                print()
                break

            if not letra in letras_usadas:
                letras_usadas.append(letra)

def main():
    palabras = ["Papel", "Arroz", "Tigre", "Zanahoria", "Parkour"]

    # Bucle de run
    while True:
        jugar_una_partida(palabras)

        continuar = input("Desea continuar jugando (s/n): ")
        if continuar.lower() != "s":
            print("\n" + "-" * 40)
            print(f"🎉 Gracias por jugar")
            print("¡Hasta la próxima!")
            print("-" * 40)
            break


main() 