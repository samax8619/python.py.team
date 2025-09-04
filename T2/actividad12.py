# •	Juego de Piedra, Papel o Tijeras: Crea el juego clásico en el que un 
# jugador elige piedra, papel o tijeras, y luego se compara con la elección 
# de la computadora para determinar el ganador.

import random

def pedirOpcion():
    opciones = ["piedra", "papel", "tijeras"]
    eleccion = input("Elige piedra, papel o tijeras: ").lower()
    while eleccion not in opciones:
        eleccion = input("Opción inválida. Elige piedra, papel o tijeras: ").lower()
    return eleccion

def juego(eleccion_jugador):
    opciones = ["piedra", "papel", "tijeras"]
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió: {eleccion_computadora}")
    
    if eleccion_jugador == eleccion_computadora:
        return "Empate"
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_jugador == "tijeras" and eleccion_computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "Perdiste"
    

print(juego(pedirOpcion()))