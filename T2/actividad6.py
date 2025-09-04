#	Contador de Dígitos: Escribe un programa que cuente la 
# cantidad de dígitos en un número entero ingresado por el 
# usuario.

def pedirNumero():
    numero = input("ingrese un numero para contar sus digitos: ")       
    return int(numero)

def contador(numero):
    contador = 0
    while numero != 0:
        numero //= 10
        contador += 1
    return f"el numero tiene {contador} digitos"

print(contador(pedirNumero()))