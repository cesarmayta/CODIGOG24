import os
import time
import tabulate
"""
SISTEMA DE MATRICULA DE ALUMNOS
C = CREATE | R = READ | U = UPDATE | D = DELETE
"""
lista_alumnos = []

ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "PROGRAMA DE MATRICULA DE ALUMNOS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNOS
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO
          [5] SALIR
          """)
    print("="*ANCHO)
    
    opcion = int(input("INGRESE UNA OPCIÓ DEL MENU:"))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR ALUMNO")
        print("="*ANCHO)
        nombre = input("NOMBRE : ")
        email = input("EMAIL :")
        celular = input("CELULAR :")
        dic_nuevo_alumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        lista_alumnos.append(dic_nuevo_alumno)
        print("="*ANCHO)
        print(" " * 10 + "ALUMNO REGISTRADO CON EXITO")
        print("="*ANCHO)
        time.sleep(1)
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR ALUMNOS")
        print("="*ANCHO)
        """for alumno in lista_alumnos:
            print('*'*ANCHO)
            for clave,valor in alumno.items():
                print(f'{clave} : {valor}')"""
        cabeceras = ["NOMBRE","EMAIL","CELULAR"]
        data = [alumno.values() for alumno in lista_alumnos]
        print(tabulate.tabulate(data,headers=cabeceras,tablefmt="grid"))
        
        
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR ALUMNO")
        print("="*ANCHO)
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA....")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!!")
        print("="*ANCHO)
    
    
    time.sleep(1)
    