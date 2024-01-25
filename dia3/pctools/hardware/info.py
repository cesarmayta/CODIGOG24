import platform
ANCHO = 15
def capturar_info():
    pc_data =  ('='*ANCHO) + ' INFO DE PC' + ('='*ANCHO) +'\n'
    pc_data += f'sistema operativo  : {platform.system()} {platform.version()} \n'
    pc_data += f'arquitectura       : {platform.machine()} \n'
    pc_data += f'procesador         : {platform.processor()} \n'

    return pc_data