# •	Serie Matemática Personalizada: Crea un programa que genere
# una serie matemática personalizada basada en las preferencias
# del usuario, utilizando bucles y condicionales.

def pedirNumero():
    numero = input("Ingrese un número para generar la serie matemática personalizada: ")       
    return int(numero)

def serie(numero):
    resultado = "Serie matemática personalizada:\n"
    for i in range(1, numero + 1):
        if i % 2 == 0:
            resultado += f"{i}^2 = {i**2}\n"
        else:
            resultado += f"{i}^3 = {i**3}\n"
    return resultado


print(serie(pedirNumero()))