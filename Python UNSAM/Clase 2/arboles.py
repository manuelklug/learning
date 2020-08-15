# arboles.py

import csv
import pprint

## Ejercicio 2.22

import csv
import pprint

def leer_parque(nombre_archivo, parque):
    parks = []
    
    with open('Data/arbolado-en-espacios-verdes.csv', encoding="utf8") as file:
        data = csv.reader(file)
        header = next(data)
        
        for row in data:
            record = dict(zip(header, row))
            
            park = {
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
            
            parks.append(park)
    
    busqueda = []
    
    for park in parks:
        if park['espacio_ve'] == parque:
            busqueda.append(park)
    
    return busqueda

general_paz = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

pprint.pprint(general_paz)

## Ejercicio 2.23

def especies(lista):
    conj_especies = set()
    
    for arbol in lista:
        conj_especies.add(arbol['nombre_com'])
    
    return conj_especies

especies_gral_paz = especies(general_paz)

print(especies_gral_paz)