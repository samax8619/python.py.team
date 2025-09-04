#•	 actividad  :	 Suma de Números: Pide al usuario que ingrese una serie de números. Cuando el usuario
# ingrese un número negativo, muestra la suma de los números ingresados hasta ese punto.

def sumarNumeros():
    suma = 0
    while True:
        numero = input("Ingrese un número para sumar (un número negativo para terminar): ")
        numero = int(numero)
        if numero < 0:
            break
        suma += numero
    return "El total de la suma es: ",suma



print(sumarNumeros())
