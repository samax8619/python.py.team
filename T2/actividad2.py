# • actividad  :	 	Tabla de Multiplicar: Crea un programa que solicite al usuario un número
# y luego imprima la tabla de multiplicar de ese número del 1 al 10.

def tablaMultiplicar (numero):
    for i in range(1,11):
        resultado = numero*i
        print(f"{numero} x {i} = {resultado}") 

def pedirNumero():
    numero = input("ingrese un numero para ver su tabla de multiplicar: ")       
    return int(numero)



print(tablaMultiplicar(pedirNumero()))
