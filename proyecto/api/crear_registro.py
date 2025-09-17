from .validar_enteros import validar_enteros


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