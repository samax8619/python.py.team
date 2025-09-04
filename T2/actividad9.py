# •	Cuenta Regresiva: Implementa un temporizador de cuenta
# regresiva que tome un número ingresado por el usuario y 
# cuente hacia atrás hasta cero.

def pedirNumero():
    numero = input("ingrese un numero para iniciar la cuenta regresiva: ")       
    return int(numero)

def cuentaRegresiva(numero):
    if numero < 0:
        return "El número debe ser no negativo."
    secuencia = []
    for i in range(numero, -1, -1):
        secuencia.append(i)
    return f"La cuenta regresiva desde {numero} es: {secuencia}"



print(cuentaRegresiva(pedirNumero()))