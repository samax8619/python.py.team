#•	Adivina el Número: Crea un juego en el que la computadora
# elige un número aleatorio y el jugador intenta adivinarlo. 
# La computadora debe proporcionar pistas como "más alto" o 
# "más bajo" según el intento del jugador
import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)  # Número entre 1 y 100
    intentos = 0
    print("¡Bienvenido al juego de Adivina el Número!")
    print("He elegido un número entre 1 y 100. Trata de adivinarlo.")

    while True:
        intento = int(input("Ingresa tu intento: "))
        intentos += 1

        if intento < numero_secreto:
            print("Más alto.")
        elif intento > numero_secreto:
            print("Más bajo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

# Ejecutar el juego
adivina_el_numero()
