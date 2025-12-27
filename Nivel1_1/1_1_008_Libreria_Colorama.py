"""
Colorama
Es una libreria escrita en python que me permite cambiar los colores y el formato
de fuente en mis programas de consola
"""
from colorama import Fore, Back, Style, init

init(autoreset=True)


def ejemplo_uso_colorama():
    # todo Inicializar colorama para que funciones correctamente en todas las plabras

    # todo Cambiar el color del Texto
    print(Fore.RED + "Esto es un texto Rojo")
    # todo cambiar el color de fondo
    print(Back.GREEN + 'Este texto tiene un fondo Verde')
    # todo cambiar texto y el fondo
    print(Fore.BLACK + Back.BLUE + 'Texto amarillo en condo azul')
    # todo aplicar estilo de negrita (resaltado)
    print(Style.BRIGHT + "Texto en negrita")
    # todo resetear estilos despues de una cadena
    print(Fore.WHITE + Back.BLACK + 'Texto en blanco sobre fondo negro' + Style.RESET_ALL)


def menu_opciones():
    borde_superior = f"{Fore.YELLOW}{Back.BLUE}+" + " -" * 30 + "+"
    opciones = [
        f"{Fore.CYAN}{Back.BLACK} | 1. Opción 1         |",
        f"{Fore.CYAN}{Back.BLACK} | 2. Opción 2         |",
        f"{Fore.CYAN}{Back.BLACK} | 3. Opción 3         |",
    ]
    borde_inferior = f"{Fore.YELLOW}{Back.BLUE}+" + " -" * 30 + "+"
    print(borde_superior)
    for opcion in opciones:
        print(opcion)
    print(borde_inferior)

menu_opciones()
seleccion = int(input(f"{Fore.GREEN} Seleccioe una opción:"))
if seleccion ==1:
    print(f"{Fore.GREEN} Has seleccionado la opción 1")
elif seleccion ==2:
    print(f"{Fore.GREEN} Has seleccionado la opción 2")
elif seleccion ==3:
    print(f"{Fore.GREEN} Has seleccionado la opción 3")
else:
    print(f"{Fore.RED}Opción no válida. Inténtalo de nuevo.")