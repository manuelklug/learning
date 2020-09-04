#arboles.py

import csv

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

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#%%

# Ejercicio 3.19. Lista de altos de Jacarandá

H_Jacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']


#%%

# Ejercicio 3.20.Lista de altos y diámetros de Jacarandá.

H_diam_jacaranda = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']










