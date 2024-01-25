def suma(numero1,numero2):
    resultado = numero1 + numero2
    return resultado

s1 = suma(3,4)
s2 = suma(s1,10)
print(s2)

def suma_infinito(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

s3 = suma_infinito(1,2,3,4,5)
print(s3)

def login(**kwargs):
    if kwargs.get('u') == 'admin' and kwargs.get('p') == '123':
        print("BIENVENIDO")
    else:
        print("DATOS INCORRECTOS")
        
print("LOGIN DE USUARIOS")
usuario = input("ingrese usuario : ")
password = input("ingrese password :")
login(p=password,u=usuario)

