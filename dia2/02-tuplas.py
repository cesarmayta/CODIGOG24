dias = ('lunes','martes','miercoles','jueves','viernes','sabado')
print(dias)
dias = list(dias)
print(dias)
dias.append('domingo')
dias = tuple(dias)
for dia in dias:
    print(dia)