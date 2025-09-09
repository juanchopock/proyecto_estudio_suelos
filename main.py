import ui
import api
import pandas as pd

def main():

    tabla_suelos = pd.read_excel("suelo_estudio.xlsx", sheet_name="Hoja 1")
    while True:
        ui.menu()
        opcion = int(input("elije una opcion: "))

        if(opcion == 5):
            print("saliendo...")
            break

        if(opcion == 1):
            registro_nuevo = api.crear_registro()
            tabla_suelos = pd.concat([tabla_suelos,pd.DataFrame([registro_nuevo])], ignore_index=True)
            tabla_suelos.to_excel("suelo_estudio.xlsx", sheet_name="Hoja 1", index=False)
            print("valores cargados")
        
        if(opcion == 2):
            ui.submenu_op2()
            sub_opcion2 = int(input("seleccion: "))

            if(sub_opcion2 == 1):
                numero_registros = int(input("ingresa el numero de registros que quieras ver: "))
                tabla_numero_registros = tabla_suelos.head(numero_registros)
                tabla_numero_registros.to_excel("auxiliar.xlsx", sheet_name="Hoja 1", index = False)
                print("valores cargados")

            if(sub_opcion2 == 2):
                numero_registros = int(input("ingresa el numero de registros que quieras ver: "))
                tabla_numero_registros = tabla_suelos.tail(numero_registros)
                tabla_numero_registros.to_excel("auxiliar.xlsx", sheet_name="Hoja 1", index = False)
                print("valores cargados")
            
            else:
                print("valor incorrecto")
        
        if(opcion == 3):
            ui.submenu_op3()
            sub_opcion3 = int(input("seleccion: "))

            if(sub_opcion3 == 1):
                print("la mediana del ph es: ",api.calcular_mediana(tabla_suelos,"ph"))
            
            if(sub_opcion3 == 2):
                print("la mediana del fosforo es: ",api.calcular_mediana(tabla_suelos,"fosforo"))
            
            if(sub_opcion3 == 3):
                print("la mediana del potasio es: ",api.calcular_mediana(tabla_suelos,"potasio"))
        
        if(opcion == 4):
            ui.submenu_op4()
            sub_opcion4 = int(input("seleccion: "))
            filtro = input("bajo que departamento desea filtrar: ")
            
            if(sub_opcion4 == 1):
                tabla_filtrada = api.crear_filtrado(tabla_suelos, "departamento", filtro)
                api.comprobar_filtro_invalido(tabla_filtrada)
                tabla_filtrada.to_excel("auxiliar.xlsx", sheet_name = "Hoja 1", index = False)

                

                
            
            







        


        
    




 





            




main()

            






