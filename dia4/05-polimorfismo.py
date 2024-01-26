class Persona:
    
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema
        
    def mostrar(self):
        print("*"*10 + " DATOS PERSONALES" + "*"*10)
        print("NOMBRE : " + self.nombre)
        print("EMAIL : " + self.email)
    
class Alumno(Persona):
    
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota = nota
        
    def mostrar(self):
        super().mostrar()
        print(("NOTA : " + str(self.nota)))
        
class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp
        
    def mostrar(self):
        super().mostrar()
        print("ESPECIALIDAD :" + self.especialidad)
        
class Empleado(Persona):
    pass
        

alumno1 = Alumno('CESAR','cesar@gmail.com',20)
alumno1.mostrar()

profesor1 = Profesor('GUILLERMO','guille@gmail.com','REACT')
profesor1.mostrar()

empleado = Empleado('JULIO','julio@gmail.com')
empleado.mostrar()
