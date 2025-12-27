import random


def jugar():
    opciones = ["piedra", "papel", "tijera"]
    # todo El jugador eloga una opcion
    jugador = input("Elige:piedra, papel o tijera:").lower()
    # todo asegurarse de que el jugador elija una opcion valida
    if jugador not in opciones:
        print("Opcion No valida , elija piedra, papel o tijera")
        return
    # todo la computadora elige aleatorioamente una opcion
    computadora = random.choice(opciones)
    # todo Mostrar las elecciones
    print(f"Tu elegiste:{jugador}")
    print(f"La Computadora eligió {computadora}")
    # todo determinar el resultado del juego
    if jugador == computadora:
        print("Es un Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
        print("Ganaste!")
    else:
        print("Perdiste!")

#Bucle principal del juego para seguir jugando
def juego_piedra_papel_tijera():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    while True:
        jugar()
        #todo Preguntar si el jugador quiere jugar de nuevo
        jugar_otra_vez = input("Quieres jugar otra vez? (SI/NO)").lower()
        if jugar_otra_vez != "si":
            print("Gracias por Jugar")
            break
#todo Ejecutar el juego
juego_piedra_papel_tijera()


