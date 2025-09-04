# •  actividad  :		Números Primos: Desarrolla un programa que verifique si 
# un número dado por el usuario es primo o no.

def pedirNumero():
    numero = input("ingrese un numero para contar sus digitos: ")       
    return int(numero)

def numPrimo (numero):
    if numero < 2:
        return f"el numero {numero} no es primo"
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return f"el numero {numero} no es primo"
    return f"el numero {numero} es primo"



print(numPrimo(pedirNumero()))
