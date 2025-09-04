# •  actividad  :		Generador de Patrones: Escribe un programa que genere patrones
# interesantes utilizando bucles anidados y condicionales. Por ejemplo,
# un triángulo de números o asteriscos.

def pedirNumero():
    numero = input("ingrese un numero para generar el patron: ")       
    return int(numero)

def patron(numero):
    resultado = ""
    for i in range(1, numero + 1):
        for j in range(1, i + 1):
            resultado += str(j) + " "
        resultado += "\n"
    return resultado



print(patron(pedirNumero()))
