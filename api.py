import pandas as pd

def comprobar_filtro_invalido(tabla_filtrada):
    if(tabla_filtrada.empty):
        print("filtro no encontrado")

def crear_filtrado(tabla_suelos, columna, filtro):
    return tabla_suelos[tabla_suelos[columna] == filtro]


def calcular_mediana(tabla_suelos,edaficas):
    tabla_suelos[edaficas] = pd.to_numeric(tabla_suelos[edaficas], errors = "coerce")
    mediana = tabla_suelos[edaficas].median()

    return mediana



def validar_enteros(mensaje):

    while True:
        try:
            return int(input(mensaje))
        
        except ValueError:
            print("ingresa un numero valido: ")



def crear_registro():
    return {
        "departamento":input("departamento: "),
        "municipio":input("municipio: "),
        "cultivo":input("cultivo: "),
        "estado":input("estado: "),
        "topografia":input("topografia: "),
        "ph":validar_enteros("ph"),
        "fosforo":validar_enteros("fosoforo"),
        "potasio":validar_enteros("potasio")
    }













