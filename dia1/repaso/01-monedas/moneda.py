import requests
from bs4 import BeautifulSoup

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
            
    def obtener_tipocambio(self):
        url_sbs = 'https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx'
        requests_sbs = requests.get(url_sbs)
        #print(f'{requests_sbs.status_code}')
        if (requests_sbs.status_code == 200):
            html = BeautifulSoup(requests_sbs.text,'html.parser')
            fila_dolares = html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__0'})
            lista_tipo_cambio = fila_dolares.find_all('td',{'class':'APLI_fila2'})
            print(f'TIPO CAMBIO VENTA : {lista_tipo_cambio[1].get_text()}')
            self.tipo_cambio = float(lista_tipo_cambio[1].get_text())
        else:
            print('error : '+ str(requests_sbs.status_code))
            
#moneda = Moneda()
#moneda.obtener_tipocambio()
            

        
        