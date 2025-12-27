"""
Descripcion
Dado una fecha de nacimiento, calcular la edad actual
"""

from datetime import date

def calcular_edad(fecha_nacimiento):
    # Obtener la fecha actual
    hoy = date.today()
    # Restar los años
    edad = hoy.year - fecha_nacimiento.year

    # Ajustar si el mes/día actuales son anteriores al cumpleaños de este año
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad  # 👈 ahora está fuera del if

# Crear la fecha de nacimiento correctamente
fecha_nacimiento = date(year=1990, month=10, day=15)

print(f"La edad de la persona es: {calcular_edad(fecha_nacimiento)}")