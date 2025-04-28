# Calculadora Basica
# Espero seguir mejorandola a futuro 
def pedir_numero():
    while True:
        n =  input("Ingrese un numero: ")
        try:
            numero = float(n)
            return numero
        except ValueError:
            print("ERROR: Ingreso un Valor No Valido")

def pedir_operacion():
    operadores_validos = ["+", "-", "*", "/"]
    while True:
        operador = input("Ingrese la operacion (+, -, *, /): ")
        if operador in operadores_validos:
            return operador
        else:
            print("ERROR: Operador No Valido")

def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "Error: division por cero"
        return num1 / num2
    else:
        return "Operacion no valida"
    
def main():
    while True:
        num1 = pedir_numero()
        num2 = pedir_numero()
        operacion = pedir_operacion()

        resultado = calcular(num1, num2, operacion)
        print(f"Resultado de {num1} {operacion} {num2} es: {resultado}")

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            print("Gracias por usar la calculadora")
            break

main()