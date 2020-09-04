# arboles.py

# Importando librerías y módulos necesarios:

import csv
import os
import numpy as np
import matplotlib.pyplot as plt

def leer_arboles(nombre_archivo):
    arboles = []
    
    with open(nombre_archivo, encoding="utf8") as file:
        data = csv.reader(file)
        header = next(data)
        
        for row in data: 
            record = dict(zip(header, row))
            
            arbol = {
                'long': record['long'],
                'lat': record['lat'],
                'id_arbol': record['id_arbol'],
                'altura_tot': record['altura_tot'],
                'diametro': record['diametro'],
                'inclinacio': record['inclinacio'],
                'nombre_com': record['nombre_com'],
                'nombre_cie': record['nombre_cie'],
                'tipo_folla': record['tipo_folla'],
                'espacio_ve': record['espacio_ve'],
                'ubicacion': record['ubicacion'],
                'nombre_fam': record['nombre_fam'],
                'nombre_gen': record['nombre_gen'],
                'origen': record['origen'],
                'coord_x': record['coord_x'],
                'coord_y': record['coord_y'],
            }
            
            arboles.append(arbol)

    return arboles

#%%
# Ejercicio 4.30

os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)

altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

plt.hist(altos, bins=10)
plt.title('Alturas de árboles Jacarandás en CABA')
plt.show()

#%%
# Ejercicio 4.31

altos_diametros = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

medidas = np.array(altos_diametros)

plt.scatter(medidas[:,1], medidas[:,0], alpha=0.3)

plt.title('Altura y diámetro de Jacarandás en CABA')
plt.xlabel('Altura del árbol')
plt.ylabel('Diamétro del árbol')
plt.show()
