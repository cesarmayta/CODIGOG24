#ENTRADA
bandera = "si"
while(bandera == "si"):
    print("MI CALCULADORA")
    numero1 = input("Número 1 : ")
    numero2 = input("Número 2 : ")
    operacion = input("Ingrese el tipo de operación(suma|resta|multiplicacion) :")
    #PROCESO
    if(operacion == "suma"):
        resultado = int(numero1) + int(numero2)
        #SALIDA
        print("la suma de " + numero1 + " + " + numero2 + " es " + str(resultado))
    elif(operacion == "resta"):
        resultado = int(numero1) - int(numero2)
        #SALIDA
        print("la resta de ",numero1," - ",numero2," es ",resultado)
    elif(operacion == "multiplicacion"):
        resultado = int(numero1) * int(numero2)
        print(f'la multiplicación de {numero1} x {numero2} es {resultado}')
    else:
        print("la operación no existe...")
        
    bandera = input("desea ejecutar otra operación(si,no)? :")