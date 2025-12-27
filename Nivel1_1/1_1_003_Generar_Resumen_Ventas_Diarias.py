"""
Descripcion
Dado un registro de ventas diarias en una lista de diccionarios, lo que vamos a generar es un resumen con el total de
ventas y la cantuidad de articulos vendidos
"""

def resumen_ventas(ventas):
    total_venta = 0
    total_articulos = 0

    for venta in ventas:
        total_venta += venta['precio'] * venta['cantidad']
        total_articulos += venta['cantidad']

    return total_venta, total_articulos


ventas = [
    {'precio': 10, 'cantidad': 3}, #10*2=20
    {'precio': 5, 'cantidad': 2}, #5*4=20
    {'precio': 10, 'cantidad': 2} #10*2=20
]

print(resumen_ventas(ventas))

