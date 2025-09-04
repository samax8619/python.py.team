#•	Factorial: Diseña un programa que calcule el factorial de un número
# dado por el usuario utilizando un bucle.

def calcular(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return f"El factorial de {numero} es: {factorial}"

def pedirNumero():
    numero = input("Ingrese un número para ver su factorial: ")
    return int(numero)



print(calcular(pedirNumero()))