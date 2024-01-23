"""
crear un programa que ingrese un numero y cree un cuadrado con * en base al numero
ingresado

ejemplo : num = 5
resultado:

* * * * * 
*       *
*       *
*       *
* * * * *
"""
#ENTRADA
bandera = "si"
while(bandera == "si"):
    lado = int(input("Ingrese el lado del cuadrado : "))
    #PROCESO
    for contador in range(lado):
        #SALIDA
        if(contador == 0 or contador == (lado-1)):
            print('* ' * lado)
        else:
            print('*' + ('  ' * (lado-2)) + ' *')
    
    bandera = input("¿desea continuar?")
