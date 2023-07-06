import os
import msvcrt
import time
import numpy as np

concierto = np.zeros((10,10),int)

def val_menu ():
    os.system("cls")
    print("""Concierto Vip "Michael Jam"
        1. Comprar Entrada
        2. Mostrar Ubicación Disponible
        3. Ver Listado Asistentes
        4. Mostrar Ganancias Totales
        5. Salir""")
    
def val_opciones ():
    while True:
        try:
            opc = int(input("Ingrese una de las opciones del menú: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! DEBE INGRESAR UN OPCIÓN VALIDA (1,2,3,4 o 5)!!")
        except:
            print("ERROR! EL NÚMERO DEBE SER ENTERO!!")

def salir ():
    os.system("cls")
    print("""\tGracias por operar con Nosotros :D
        \t Marilyn Correa 
        \t 06/07/2023""")
    time.sleep(3)
    os.system("cls")
    

def mostrar_estadio ():
    os.system("cls")
    contador = 1
    print("columna    [1]    [2]    [3]    [4]    [5]    [6]     [7]   [8]    [9]   [10]")
    for x in range(10):
        print(f"Fila {x+1}= ", end=" ")
        for y in range(10):
            print(f"{contador}: {concierto[x][y]} ", end=" ")
            contador +=1
        print()
    print("presione ENTER para continuar...")
    msvcrt.getch()

def val_rut():
    while True:
        try:
            rut = int(input("Ingrese su número de rut (SIN GUIÓN NI DIGITO VERIFICADOR): "))
            if rut >= 1111111 and rut <=99999999:
                return rut
            else:
                print("ERROR! RUT NO VALIDO Y DEBE SER SIN GUIÓN NI DIGITO VERIFICADOR!")
        except:
            print("ERROR! DEBE INGRESAR SOLO NÚMEROS!")

def ubicacion_disp ():
    os.system("cls")
    while True:
        print("Asientos disponibles: ")
        mostrar_asientos = mostrar_estadio()
        return
        

def listado_asistentes ():
    os.system("cls")
    while True:
        input("ASISTENTES: ")
        input(lista_rut)

        print("Precione ENTER para continuar...")
        msvcrt.getch()
        return
    

def ganancia_total():
    os.system("cls")
    entrada_plat = 120000
    entrada_gold = 80000
    entrada_silver = 50000
    to_cant = 0
    total_venta = 0
    total_entrada = 0
    print(f"""\t\t¡¡GANANCIA TOTAL!!\n
    TIPO DE ENTRADA             CANTIDAD      TOTAL
    PLATINUM $ {entrada_plat}                    
    GOLD     $ {entrada_gold}           
    SILVER   $ {entrada_silver}          
    TOTAL                       {to_cant}      {total_venta}     
    """)

    print("Precione ENTER para continuar...")
    msvcrt.getch()

def val_entrada():
    while True:
        try:
            com_entrada = int(input("Seleccione la cantidad de entradas a comprar (MIN 1, MÁX 3): "))
            if com_entrada in (1,2,3):
                return com_entrada
            else:
                print("RECUERDE QUE SOLO PUEDE COMPRAR 1, 2 o 3 ENTRADAS!!")
        except:
            print("ERROR!! INGRESE NÚMERO ENTERO!!")


lista_rut = []
lista_fila = []
lista_columna = []
lista_asiento = []

def valor_entrada():
    ent_plat = 120000
    ent_gold = 80000
    ent_silver = 50000
    cant_plat = 0
    cant_gold = 0
    cant_silver = 0
    acumu_plat = 0
    acumu_sil = 0
    acumu_gold = 0
    os.system("cls")
    print(f"""VALOR ENTRADAS: 
    PLATINUM $ {ent_plat}  (asientos del 01 al 20)
    GOLD     $ {ent_gold}  (asientos del 21 al 50)
    SILVER   $ {ent_silver}(asientos del 51 al 100)""")
    while True:
        try:
            tipo_entrada = int(input("Seleccione el tipo de entrada que desea (1.PLATINUM, 2.GOLD, 3.SILVER): \n"))
            if tipo_entrada in (1,2,3):
                if tipo_entrada == 1:
                    print("\nIngrese la cantidad que desa (min 1, máx 3): ")
                    cant_plat = cant_plat*ent_plat
                    acumu_plat +=1
                elif tipo_entrada == 2:
                    print("\nIngrese la cantidad que desa (min 1, máx 3): ")
                    cant_gold = cant_gold*ent_gold
                    acumu_gold +=1
                else:
                    print("\nIngrese la cantidad que desa (min 1, máx 3): ")
                    cant_silver = cant_silver*ent_silver
                    acumu_sil+=1
                    return
            else:
                print("ERROR! DEBE INGRESAR UNA OPCIÓN VALIDA!!")
        except:
            print("ERROR! SOLO PUEDE INGRESAR NÚMEROS ENTEROS!!")
                    
#def seleccion_asiento():
    #if concierto not in 0:
        #print("SIN ASIENTOS DISPONIBLES!")
        #time.sleep(3)
        #return
    #contador = 1
    #while True:
        #selec_asiento = input("Ingrese asiento: ") 
        #for x in range(10):
            #for y in range(10):
         #selec_asiento in [x][y]: 

        #time.sleep(3)
        



def comprar_entrada():
    os.system("cls")

    contador = 0
    acumulador = 0
    mostrar_estadio()
    valor_entrada()
    mostrar_estadio()
    #seleccion_asiento()
    val_rut()
    lista_rut.append()
    lista_asiento.append()
    lista_fila.append()
    lista_columna.append()

