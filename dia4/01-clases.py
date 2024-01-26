class Automovil:
    #atributos
    def __init__(self,aa,pl,col,mar):
        self.__anio = aa
        self.placa = pl
        self.color = col
        self.marca = mar
        
    def getAnio(self):
        return self.__anio
    
    def setAnio(self,aa):
        self.__anio = aa
    #metodos
    def encender(self):
        print('encender ' + self.marca)
        
    def avanzar(self):
        print('avanzar ' + self.marca)
        
    def acelerar(self):
        print('acelerar' + self.marca)
        
    def frenar(self):
        print('frenar' + self.marca)
        

## objetos
vw = Automovil(1970,'CH-1234','Amarillo','Volkswagen')
print('se crel objeto vw con los siguientes atributos')
print('año : ' + str(vw.getAnio()))
print('color : ' + vw.color)
print('placa : ' + vw.placa)

nuevo_anio = input('ingrese nuevo año :')
vw.setAnio(int(nuevo_anio))
print('nuevo año : ' + str(vw.getAnio()))

vw.encender()
tico = Automovil(1990,'CH-5678','Rojo','Daewo')
tico.encender()