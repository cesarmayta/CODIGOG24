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
        valor_busqueda = input('INGRESE EL EMAIL DE ALUMNO A ACTUALIZAR :')
        posicion_busqueda = -1
        for posicion in range(len(lista_alumnos)):
            dic_alumno = lista_alumnos[posicion]
            if valor_busqueda in dic_alumno.values():
                posicion_busqueda = posicion
                break
            
        if(posicion_busqueda == -1):
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            print(f' ALUMNO A ACTUALIZAR : {lista_alumnos[posicion_busqueda].get("nombre")}')
            print('INGRESE NUEVOS DATOS PARA EL ALUMNO:')
            print('NOTA: SI PRESIONA ENTER NO SE ACTUALIZARA EL VALOR')
            nombre = input(f'NOMBRE({lista_alumnos[posicion_busqueda].get("nombre")}) :')
            if (nombre == ""):
                nombre = lista_alumnos[posicion_busqueda].get("nombre")
            email = input(f'EMAIL({lista_alumnos[posicion_busqueda].get("email")}) :')
            if (email == ""):
                email = lista_alumnos[posicion_busqueda].get("email")
            celular = input(f'CELULAR ({lista_alumnos[posicion_busqueda].get("celular")}) : ')
            if (celular == ""):
                celular = lista_alumnos[posicion_busqueda].get("celular")
            
            dic_alumno = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            lista_alumnos[posicion_busqueda] = dic_alumno
            print("="*ANCHO)
            print(" " * 10 + "ALUMNO ACTUALIZADO CON EXITO!!!")
            print("="*ANCHO)
            
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE EL EMAIL DE ALUMNO A ELIMINAR :')
        posicion_busqueda = -1
        for posicion in range(len(lista_alumnos)):
            dic_alumno = lista_alumnos[posicion]
            if valor_busqueda in dic_alumno.values():
                posicion_busqueda = posicion
                break
            
        if(posicion_busqueda == -1):
            print("NO SE ENCONTRO EL ALUMNO SOLICITADO")
        else:
            lista_alumnos.pop(posicion_busqueda)
            print(' ALUMNO ELIMINADO!!!')
        
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA....")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!!")
        print("="*ANCHO)
    
    
    time.sleep(1)
    