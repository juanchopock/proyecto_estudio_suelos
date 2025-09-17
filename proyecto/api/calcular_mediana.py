import pandas as pd


def calcular_mediana(tabla_suelos,edaficas):
    tabla_suelos[edaficas] = pd.to_numeric(tabla_suelos[edaficas], errors = "coerce")
    mediana = tabla_suelos[edaficas].median()

    return mediana