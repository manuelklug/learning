import informe_funciones as informe

def costo_camion(nombre_archivo):
    costo = 0
    
    camion = informe.leer_camion(nombre_archivo)
    
    for fila in camion:
        costo += int(fila['cajones']) * float(fila['precio'])
    
    return costo

costo_total = costo_camion('../Data/camion.csv')
print('Costo total:', costo_total)