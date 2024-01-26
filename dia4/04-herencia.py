class Persona:
    
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema
        
    def mostrar(self):
        print("="*30)
        print("NOMBRE : " + self.nombre)
        print("EMAIL : " + self.email)
    
class Alumno(Persona):
    
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota = nota
        
class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp

    

alumno1 = Alumno('CESAR','cesar@gmail.com',20)
alumno1.mostrar()

profesor1 = Profesor('GUILLERMO','guille@gmail.com','REACT')
profesor1.mostrar()