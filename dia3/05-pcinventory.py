from pctools.software import info as software
from pctools.hardware import info as hardware

def guardar_info(file_name,pc_data):
    pc_file = open(file_name,'w')
    pc_file.write(pc_data)
    pc_file.close()

if __name__ ==  '__main__':
    info_pc = hardware.capturar_info()
    print(info_pc)
    guardar_info('pc.txt',info_pc)
    info_programas = software.capturar_info()
    print(info_programas)
    guardar_info('programas.txt',info_programas)
