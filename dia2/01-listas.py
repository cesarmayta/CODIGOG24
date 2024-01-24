dias = ['lunes','martes','miercoles']
print(dias)
print(dias[-1])
#agregar valor a una lista
dias.append('jueves')
dias.append('viernes')
print(dias)
#eliminar valor de una lista
dias.pop(3)
print(dias)
del dias[2:4]
print(dias)
#actualizar valor de una lista
dias[0] = "domingo"
dias[1] = "lunes"
print(dias)
dias.append("martes")
dias.append("miercoles")
dias.append("jueves")
dias.append("viernes")
print(dias)

#recorrer una lista
for contador in range(len(dias)):
    print(dias[contador])
  
for dia in dias:
    print(dia)  

