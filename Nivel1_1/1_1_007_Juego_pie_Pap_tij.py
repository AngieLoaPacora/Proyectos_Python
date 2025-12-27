import random


def jugar(victorias_jugador, victorias_computadora):
    opciones = {
        "piedra": "🪨",
        "papel": "📄",
        "tijera": "✂️"}

    # todo El jugador eloga una opcion
    jugador = input("Elige:piedra, papel o tijera:").lower()
    # todo asegurarse de que el jugador elija una opcion valida
    if jugador not in opciones:
        print("Opcion No valida , elija piedra, papel o tijera")
        return victorias_jugador, victorias_computadora
    # todo la computadora elige aleatorioamente una opcion
    computadora = random.choice(list(opciones.keys()))
    # todo Mostrar las elecciones
    print(f"Tu elegiste:{opciones[jugador]} ({jugador})")
    print(f"La Computadora eligió {opciones[computadora]} ({computadora}")
    # todo determinar el resultado del juego
    if jugador == computadora:
        print("Es un Empate! 😐")
    elif (jugador == "piedra" and computadora == "tijera") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijera" and computadora == "papel"):
        print("Ganaste!🥳")
        victorias_jugador += 1  # todo Incrementar el conteo de victorias del jugador
    else:
        print("Perdiste! 🥲")
        victorias_computadora += 1  # todo Incrementar el conteo de victorias de la computadora
    return victorias_jugador, victorias_computadora


# Bucle principal del juego para seguir jugando
def juego_piedra_papel_tijera():
    print("Bienvenido al juego de Piedra 🪨, Papel 📄 o Tijera ✂️!")

    # todo Variables para almacenar las victorias
    victorias_computadora = 0
    victorias_jugador = 0

    while True:
        victorias_jugador, victorias_computadora=jugar(victorias_jugador, victorias_computadora)
        # todo Preguntar si el jugador quiere jugar de nuevo
        jugar_otra_vez = input("Quieres jugar otra vez? (SI/NO)").lower()
        if jugar_otra_vez != "si":
            #todo Mostrar las estadisticas
            print("\n--Estadisticas Finales---")
            print(f"Victorias del jugador:{victorias_jugador}")
            print(f"Victorias de la Computadora:{victorias_computadora}")
            #todo compara quien gano mas veces
            if victorias_jugador > victorias_computadora:
                print("Felicidades, Ganaste mas veces! 🎊")
            elif victorias_jugador <victorias_computadora:
                print("La computadora Gano Mas veces No te Rindas es solo un Robot 🤖")
            else:
                print("Fue Un Empate Total 👀")
            print("Gracias por Jugar 👏🏽")
            break

# todo Ejecutar el juego
juego_piedra_papel_tijera()