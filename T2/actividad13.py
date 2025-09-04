# •	 actividad  :	 Generador de Tablas de Sumar: Desarrolla un programa que 
# genere tablas de sumar para que los niños las practiquen. 
# Pide al usuario la tablas que desean y el rango de números.

def pedirNumero():
    numero = input("ingrese un numero para ver su tabla de sumar: ")       
    return int(numero)

def tabla(numero):
    resultado = f"Tabla de sumar del {numero}:\n"
    for i in range(1, 11):
        resultado += f"{numero} + {i} = {numero + i}\n"
    return resultado



print(tabla(pedirNumero()))
