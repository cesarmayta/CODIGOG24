"""
crear un juego en donde el participante debe adivinar un numero entre 1 y 10
para esto tendra 3 intento y si no lo adivina le saldra el mensaje
fallaste
y si lo adivina le debe salir el mensaje adivinaste
cada vez que falle un intento le debe dar pistas diciendo
el nro es mayor o el numero es menor dependiente si el nro secreto es mayor o menor al numero que ingreso
"""
import random
numero_secreto = random.randint(1, 10)
print("adivina el nro secreto entre 1 y 10")

total_intentos = 3
intento = 1
while(intento <= total_intentos):
    try:
        numero = input(f"intento {intento} :")
        numero = int(numero)
        if numero >= 1 and numero <= 10:
            if numero == numero_secreto:
                print("ADIVINASTE!!!")
                break
            else:
                if intento == 3:
                    print(f"FALLASTE, el número secreto era {numero_secreto}")
                    break
                else:
                    if numero > numero_secreto:
                        print('Intenta nuevamente, el número es menor')
                    else:
                        print('Intenta nuevamente, el número es mayor')
        else:
            print('El número debe ser entre 1 y 10')

        intento += 1
    except Exception as error:
        if type(numero) == str:
            print('Debes ingresar un número')
        else:
            print('ERROR : ',error)
    