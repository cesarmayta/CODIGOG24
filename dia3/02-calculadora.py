def calculadora(**kwargs):
    ope = kwargs.get('ope')
    n1 = int(kwargs.get('n1'))
    n2 = int(kwargs.get('n2'))
    if (ope == "suma"):
        resultado = n1 + n2
    elif(ope == "resta"):
        resultado = n1 - n2
    elif(ope == "multiplicacion"):
        resultado = n1 * n2
    elif(ope == "division"):
        resultado = n1 / n2
    else:
        resultado = 'operador incorrecto'
        
    return resultado

numero1 = input("Ingrese 1er número : ")
numero2 = input("Ingrese 2do número : ")
operaciones = ('suma','resta','multiplicacion','division')

for operacion in operaciones:
    resultado = calculadora(n1=numero1,n2=numero2,ope=operacion)
    print(f'la {operacion} de {numero1} y {numero2} es  {resultado}')
