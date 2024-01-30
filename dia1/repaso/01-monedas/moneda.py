class Moneda:
    
    def __init__(self):
        self.tipo_cambio = 3.8
        self.monto_origen = 0
        self.monto_destino = 0
        self.moneda_origen = ''
        self.moneda_destino = ''
        self.operacion = ''
        
    def convertir(self):
        self.monto_origen = int(input((f'Ingrese el monto en {self.moneda_origen} : ')))
        if self.operacion == '/':
            self.monto_destino = self.monto_origen / self.tipo_cambio
            print(f' El monto es {self.moneda_destino} es {self.monto_destino}')
        elif self.operacion == '*':
            self.monto_destino = self.monto_origen * self.tipo_cambio
            print(f' El monto es {self.moneda_destino} es {self.monto_destino}')
        else:
            print(f' {self.operacion} no es valida')
            

        
        