"""
ingresar una lista de 5 numeros y retornar el numero mayor de la lista
Ejemplo:
ingrese nro 1: 10
ingrese nro 2: 13
ingrese nro 3: 15
ingrese nro 4: 1
ingrese nro 5: 5

el nro mayor es 15

[10,13,15,1,5]

numero_mayor = 15
numero = 5

"""
#ENTRADA
numeros = []
for contador in range(1,6):
    nuevo_numero = int(input(f'ingrese nro {contador} :'))
    numeros.append(nuevo_numero)
    
print(numeros)
#PROCESO
numero_mayor = numeros[0]
for numero in numeros:
    if(numero > numero_mayor):
        numero_mayor = numero

#SALIDA
print(f"El nro mayor es {numero_mayor} ")

numeros.sort(reverse=True)
print(numeros)
print(numeros[0])
        