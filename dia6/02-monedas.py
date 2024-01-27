"""
CREAR UN PROGRMAA QUE CONVIERTA MONEDAS DE SOLES A DOLARES
"""
#ENTRADA
TIPO_CAMBIO = 3.786
print("""
      ==============================================
                CONVERTIDOR DE MONEDAS
      ==============================================
      OPCIÓN 1 : Convertir de soles a dolares
      OPCIÓN 2 : Convertir de dolares a soles
      ==============================================
      """)
opcion = 0
while(opcion != 1 and opcion != 2):
    try:
        opcion = int(input("Ingrese la opción que desee : "))
        if opcion == 1:
            monto_origen = float(input('Ingrese monto en soles:'))
            monto_destino = monto_origen / TIPO_CAMBIO
            #SALIDA
            print(f'El monto en dolares es {monto_destino}')
        elif opcion == 2:
            monto_origen = float(input('Ingrese monto en dolares:'))
            monto_destino = monto_origen * TIPO_CAMBIO
            print(f'El monto en soles es {monto_destino}')
        else:
            print("LA OPCIÓN NO ES VALIDA : ingrese 1 o 2")
    except:
        print("Debe ingresar un número ")
    

        