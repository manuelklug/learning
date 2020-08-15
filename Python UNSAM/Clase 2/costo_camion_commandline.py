# costo_camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0
    
    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)
        
        for row in rows:
        	ncajones = int(row[1])
        	precio = float(row[2])
        	costo += ncajones * precio
    
    return costo
        
        
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
	nombre_archivo = 'Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)