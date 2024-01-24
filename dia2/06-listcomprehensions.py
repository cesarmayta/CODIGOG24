"""
de  la siguiente lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,10]

retorna una lista solo con los numeros pares

para sacar el residuo de un numero se usa %
4 % 2 = 0
"""
#ENTRADA
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
#PROCESO
pares = []
for numero in numeros:
    if(numero % 2 == 0):
        pares.append(numero)
#SALIDA
print(pares)

#USANDO LIST COMPREHENSIONS
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)