capitales = {
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Colombia':'Bogota'
}

#recorrido por claves
for clave in capitales.keys():
    print(clave)
    
print('*'*30)
#recorrido por valores
for valor in capitales.values():
    print(valor)
print('*'*30)
#recorrido por clave y valor
for clave,valor in capitales.items():
    print(f'la capital de {clave} es {valor}')