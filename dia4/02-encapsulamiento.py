## LOGIN DE USUARIO
class Usuario:
     
     __email = 'cesar@gmail.com'
     __password = 'qwerty123'
    
     def __init__(self):
         pass
     
     def login(self,email,password):
        if(self.__email == email and self.__password == password):
            print('Bienvenido ' + self.__email)
        else:
            print('datos incorrectos')
            
            
print("LOGIN DE USUARIOS")
email = input("Ingrese email :") 
pwd = input("Ingrese Password :")

usuario = Usuario()
usuario.login(email,pwd)
         