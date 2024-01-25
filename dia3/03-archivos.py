#crear un nuevo archivo
archivo = open('alumnos.txt','w')
archivo.write('cesar mayta,cesar@gmail.com,9888282')
archivo.close()



archivo_agregar = open('alumnos.txt','a')
archivo_agregar.write('\n')
archivo_agregar.write('jorge perez,jorge@gmail.com,8979879')
archivo_agregar.close()

#abrir un archivo en modo lectura
archivo_lectura = open('alumnos.txt','r')
alumnos = archivo_lectura.read()
print(alumnos)
archivo_lectura.close()