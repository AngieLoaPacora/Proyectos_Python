# todo Calcular el porcentaje de propina en un restaurante
"""
Descripción
Dado un total de cuenta y un porcentaje de propina, calcular cuanto se debe dar de propina y el total a pagar
"""


def calcular_propina(total_cuenta, porcentaje_propina):
    """
    Esta funcion calcula la propina en u restaurante y el total a pagar:
    :param total_cuenta:
    :param porcentaje_propina:
    :return:
    """

    propina = total_cuenta * porcentaje_propina / 100
    total_a_pagar = total_cuenta + propina
    return propina, total_a_pagar


total_cuenta = 100
porcentaje_propina = 15
propina, total_a_pagar = calcular_propina(total_cuenta, porcentaje_propina)
print(f"La propina es: ${propina: .2f} , Total a Pagar ${total_a_pagar: .2f}")
