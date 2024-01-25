import platform
import subprocess

ANCHO = 15
def capturar_info():
    pc_data =  ('='*ANCHO) + ' INFO DE PC' + ('='*ANCHO) +'\n'
    pc_data += f'sistema operativo  : {platform.system()} {platform.version()} \n'
    pc_data += f'arquitectura       : {platform.machine()} \n'
    pc_data += f'procesador         : {platform.processor()} \n'

    return pc_data

def guardar_info(file_name,pc_data):
    pc_file = open(file_name,'w')
    pc_file.write(pc_data)
    pc_file.close()
    
def capturar_programas():
    data = subprocess.check_output(['wmic','product','get','name'])
    data_programas = str(data)
    lista_programas = data_programas.split("\\r\\r\\n")
    str_programa = ''
    for programa in lista_programas:
        str_programa += programa + '\n'
        
    return str_programa
    
if __name__ ==  '__main__':
    info_pc = capturar_info()
    print(info_pc)
    guardar_info('pc.txt',info_pc)
    info_programas = capturar_programas()
    print('='*ANCHO*3)
    print("PROGRAMAS INSTALADOS : ")
    print(info_programas)
    guardar_info('programas.txt',info_programas)