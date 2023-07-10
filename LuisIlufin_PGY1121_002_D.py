import os
os.system("cls")

platinum = 120000
gold = 80000
silver = 50000
listaentradas = []
listarut = []
listaasientosplat = []
listaasientosgold = []
listaasientossilver = []



menu = """
Bienvenido a Creativos.cl
Por favor, ingrese su opción:
-----------------------------------------------------------
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
"""
while True:
    try:
        opc = int(input(menu))
        if opc == 5:
            break
            print("Ha elegido salir, gracias por preferirnos :)")
            print("LUIS ILUFIN VENTAS SYSTEM 1.0")
            print("10 de Julio del 2023")
        
        elif opc == 1:
            while True:
                try:
                    entradas = int(input("Ingrese cuantas entradas desea (1 mín/3 máx)"))
                    if entradas >= 1 and entradas <= 3:
                        listaentradas.append(entradas)
                        print(listaentradas)
                        break
                    else:
                        print("Ingrese nuevamente su cantidad de entradas")
                except:
                    print("Ocurrió una excepción")
            while True:
                try:
                        asiento = input("""
                        PRECIOS DE ASIENTOS:
                        ---------------------------------------------------
                        PLATINUM $120.000 (desde asiento 1 al 20)
                        GOLD $80.000 (desde asiento 21 al 50)
                        SILVER $50.000 (desde asiento 51 al 100)
                        ---------------------------------------------------
                        Ingrese su asiento:
                        """)
                        if asiento == "platinum":
                            cantplatinum = int(input("""
                            Ha escogido PLATINUM ($120.000)
                            ------------------------------------------
                            Ingrese sus asientos (1 al 20):
                            """))
                            if cantplatinum >= 1 and cantplatinum <= 20:
                                listaasientosplat.append(cantplatinum)
                                print(listaasientosplat)
                            else:
                                print("Ingrese nuevamente")
                            run = int(input("Ingrese su RUN para confirmar asiento:"))
                            if run >= 100000 and run < 100000000:
                                    break
                                    print("Compra exitosa")
                            else:
                                 print("Ingrese nuevamente su RUN")
                                
                        elif asiento == "gold":
                                cantgold = int(input("""
                                Ha escogido GOLD ($80.000)
                                ------------------------------------------
                                Ingrese sus asientos (21 al 50):
                                """))
                                if cantgold >= 21 and cantgold <= 50:
                                    listaasientosgold.append(cantgold)
                                    print(listaasientosgold)
                                else:
                                    print("Ingrese nuevamente")
                                run = int(input("Ingrese su RUN para confirmar asiento:"))
                                if run >= 100000 and run < 100000000:
                                    break
                                    print("Compra exitosa")
                                else:
                                 print("Ingrese nuevamente su RUN")
                                
                        elif asiento == "silver":
                                cantsilver = int(input("""
                                Ha escogido SILVER ($50.000)
                                ------------------------------------------
                                Ingrese sus asientos (51 al 100):
                                """))
                                if cantsilver >= 51 and cantsilver <= 100:
                                    listaasientossilver.append(cantsilver)
                                    print(listaasientossilver)
                                else:
                                    print("Ingrese nuevamente")
                                run = int(input("Ingrese su RUN para confirmar asiento:"))
                                if run >= 100000 and run < 100000000:
                                    break
                                    print("Compra exitosa")
                                else:
                                 print("Ingrese nuevamente su RUN")
                                
                    
                    
                except:
                    print("Ocurrió una excepción")
        elif opc == 2:
                    print("""
                    ||          ASIENTOS DISPONIBLES         ||
                    --------------------------------------------------
                    ||               ESCENARIO                 ||
                    |    1   2   3   4   5   6   7   8   9   10 |   
                    |    11  12  13  14  15  16  17  18  19  20 |
                    |    21  22  23  24  25  26  27  28  29  30 |
                    |    31  32  33  34  35  36  37  38  39  40 |
                    |    41  42  43  44  45  46  47  48  49  50 |
                    |    51  52  53  54  55  56  57  58  59  60 |
                    |    61  62  63  64  65  66  67  68  69  70 |
                    |    71  72  73  74  75  76  77  78  79  80 |
                    |    81  82  83  84  85  86  87  88  89  90 |
                    |    91  92  93  94  95  96  97  98  99  100|
                    """)
        elif opc == 3:
                while True:
                    print(f"""NÚMERO DE ASISTENTES -> {asiento * (cantsilver + cantgold + cantplatinum)}
                    """)
                    break
        elif opc == 4:
             while True:
                  
                print(f"""GANANCIAS TOTALES
                --------------------------------------
                PLATINUM = {platinum * cantplatinum}
                GOLD = {gold * cantgold}
                SILVER = {(silver * cantsilver)}
                ------------------------------------------------
                CANTIDAD DE ENTRADAS = {cantsilver + cantplatinum + cantgold}
                TOTAL VENDIDO = {(platinum * cantplatinum) + (gold * cantgold) + silver * cantsilver}
                """)
                break

                        

        
    except:
        print("Excepción de menú :o ")

