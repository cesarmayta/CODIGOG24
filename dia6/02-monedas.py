"""
CREAR UN PROGRMAA QUE CONVIERTA MONEDAS DE SOLES A DOLARES
"""
#ENTRADA
TIPO_CAMBIO = 3.786
opcion_1 = {
    'moneda_origen':'soles',
    'moneda_destino':'dolares',
    'operador':'/'
}
opcion_2 = {
    'moneda_origen':'dolares',
    'moneda_destino':'soles',
    'operador':'*'
}
#FUNCIONES
def convertir_monto(convertir_opcion):
    #ENTRADA
    moneda_origen = convertir_opcion.get('moneda_origen')
    moneda_destino = convertir_opcion.get('moneda_destino')
    operador = convertir_opcion.get('operador')
    #PROCESO
    monto_origen = float(input(f'Ingrese monto en {moneda_origen} :'))
    if operador == "/":
        monto_destino = monto_origen / TIPO_CAMBIO
    elif operador == "*":
        monto_destino = monto_origen * TIPO_CAMBIO
    #SALIDA
    print(f'El monto en {moneda_destino} es {monto_destino}')

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
            convertir_monto(opcion_1)
        elif opcion == 2:
            convertir_monto(opcion_2)
        else:
            print("LA OPCIÓN NO ES VALIDA : ingrese 1 o 2")
    except Exception as error:
        print("Error : ",error)
    

        