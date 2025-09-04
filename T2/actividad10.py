# •	Calculadora Simple: Construye una calculadora básica que tome 
# dos números y un operador (+, -, *, /) ingresados por el usuario,
# y muestre el resultado de la operación.

def pedirNumero():
    numero = input("ingrese un numero: ")       
    return float(numero)

def pedirOperador():
    operador = input("ingrese un operador (+, -, *, /): ")       
    return operador

def calculadora(num1, num2, operador):  
    if operador == '+':
        return f"el resultado de {num1} + {num2} es: {num1 + num2}"
    elif operador == '-':
        return f"el resultado de {num1} - {num2} es: {num1 - num2}"
    elif operador == '*':
        return f"el resultado de {num1} * {num2} es: {num1 * num2}"
    elif operador == '/':
        if num2 != 0:
            return f"el resultado de {num1} / {num2} es: {num1 / num2}"
        else:
            return "Error: División por cero no es permitida."
    else:
        return "Operador no válido. Por favor use +, -, *, o /."        
    


print(calculadora(pedirNumero(), pedirNumero(), pedirOperador()))