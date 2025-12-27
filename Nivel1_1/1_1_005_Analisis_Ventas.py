"""
Descripcion
Realizar un Analisis de Ventas que tiene un registro de ventas, con columnas como fecha
producto, cantidad, precio. El objetivo es generar un resumen de total de ventas por producto
y el ingreso total por día.
"""

import csv
from collections import defaultdict

from django.db.models.fields import return_None


def analizar_ventas(archivo_csv):
    ventas_por_producto = defaultdict(float)
    ingresos_por_dia = defaultdict(float)

    try:
        with open(archivo_csv, mode='r') as file:
            lector_csv = csv.DictReader(file)
            for fila in lector_csv:
                    fecha = fila['Fecha']
                    producto = fila['Producto']
                    cantidad = int(fila['Cantidad'])
                    precio = float(fila['Precio'])

                    total_venta = cantidad * precio
                    ventas_por_producto[producto] += total_venta
                    ingresos_por_dia[fecha] += total_venta

    except FileNotFoundError:
        print(f"Error el archivo '{archivo_csv}'No se encuentra")
        return

    except PermissionError:
        print(f"Error No Tienes permisos para abrir el archivo '{archivo_csv}'")
    except Exception as e:
        print(f"Se produjo un error inesperado {e}")
        return

    print("Total de ventas por producto")
    for producto, total in ventas_por_producto.items():
        print(f"{producto}: ${total:.2f}")

    print("\nIngresos totales por día")
    for fecha, total in ingresos_por_dia.items():
        print(f"{fecha}: ${total:.2f}")

archivo_csv = 'ventas.csv'
analizar_ventas(archivo_csv)
