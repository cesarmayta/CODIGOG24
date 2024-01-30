from moneda import Moneda

print("""
      ==============================================
                CONVERTIDOR DE MONEDAS
      ==============================================
      OPCIÓN 1 : Convertir de soles a dolares
      OPCIÓN 2 : Convertir de dolares a soles
      ==============================================
      """)
      
opcion = int(input('Ingrese la opción que desee : '))
if opcion == 1:
    #convertir de soles a dolares
    moneda1 = Moneda()
    moneda1.obtener_tipocambio()
    moneda1.moneda_origen = 'soles'
    moneda1.moneda_destino = 'dolares'
    moneda1.operacion = '/'
    moneda1.convertir()
elif opcion == 2:
    moneda2 = Moneda()
    moneda2.moneda_origen = 'dolares'
    moneda2.moneda_destino = 'soles'
    moneda2.operacion = '*'
    moneda2.convertir()
else:
    print('OPCION NO VALIDA , ingrese 1 o 2')
