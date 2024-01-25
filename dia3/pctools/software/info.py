import subprocess


def capturar_info():
    data = subprocess.check_output(['wmic','product','get','name'])
    data_programas = str(data)
    lista_programas = data_programas.split("\\r\\r\\n")
    str_programa = ''
    for programa in lista_programas:
        str_programa += programa + '\n'
        
    return str_programa