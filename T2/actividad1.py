# • actividad  :	Números Pares e Impares: Escribe un programa que solicite al usuario
# un número y luego imprima si es par o impar.

def calcular(numero):
    if numero % 2 == 0:
        return "El numero es par"
    else: 
        return "el numero es impar"
    
def pedirNumero():
    numero =input("ingrese un numero: ")
    return int(numero)




print(calcular(pedirNumero()))
