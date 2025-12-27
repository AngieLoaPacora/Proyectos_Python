"""
Calcular el cambio de una Transacción
"""

def calcular_cambio(costo, pagado):
    # Paso 1: calcular el cambio total
    cambio = pagado - costo

    # Paso 2: billetes y monedas disponibles
    billetes_y_monedas = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

    desglose = {}

    # Paso 3: desglosar el cambio
    for valor in billetes_y_monedas:
        cantidad = int(cambio // valor)
        cambio = round(cambio % valor, 2)

        if cantidad > 0:
            desglose[valor] = cantidad

    return desglose


# Pruebas (esto va FUERA de la función)
costo = 23.75
pagado = 50
print(calcular_cambio(costo, pagado))