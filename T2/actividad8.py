# •	Secuencia de Fibonacci: Crea un programa que genere los 
# primeros n términos de la secuencia de Fibonacci.

def pedirNumero():
    numero = input("ingrese un numero para ver la secuencia de fibonacci: ")       
    return int(numero)

def fibonacci(numero):
    a, b = 0, 1
    secuencia = []
    for _ in range(numero):
        secuencia.append(a)
        a, b = b, a + b
    return f"Los primeros {numero} términos de la secuencia de Fibonacci son: {secuencia}"


print(fibonacci(pedirNumero()))