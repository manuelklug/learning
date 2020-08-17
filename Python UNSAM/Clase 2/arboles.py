# arboles.py

import csv
import pprint

#%%% 

## Ejercicio 2.22

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
                'altura_tot': float(record['altura_tot']),
                'diametro': record['diametro'],
                'inclinacio': int(record['inclinacio']),
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

#%%% 

## Ejercicio 2.23

def especies(lista):
    conj_especies = set()
    
    for arbol in lista:
        conj_especies.add(arbol['nombre_com'])
    
    return conj_especies

especies_gral_paz = especies(general_paz)

print(especies_gral_paz)

#%%% 

## Ejercicio 2.24

from collections import Counter

def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    
    for dic in lista_arboles:
        ejemplares[dic['nombre_com']] += 1
    
    return ejemplares

print('General Paz:')
print(contar_ejemplares(general_paz).most_common(5))

print('Los Andes:')
los_andes = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
print(contar_ejemplares(los_andes).most_common(5))

print('Centenario:')
centenario = leer_parque('Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
print(contar_ejemplares(centenario).most_common(5))

#%%%

## Ejercicio 2.25

def obtener_alturas(lista_arboles, especie):
    alturas = []
    
    for dic in lista_arboles:
        if dic['nombre_com'] == especie:
            alturas.append(dic['altura_tot'])
    
    return alturas

alturas_jac_gralpaz = obtener_alturas(general_paz, 'Jacarandá')

alturas_jac_losandes = obtener_alturas(los_andes, 'Jacarandá')

alturas_jac_centenario = obtener_alturas(centenario, 'Jacarandá')

print('General Paz:')
print('Max:', max(alturas_jac_gralpaz))
print('Prom:', round(sum(alturas_jac_losandes) / len(alturas_jac_losandes), 2))

print('Los Andes:')
print('Max:', max(alturas_jac_losandes))
print('Prom:', round(sum(alturas_jac_losandes) / len(alturas_jac_losandes), 2))

print('Los Andes:')
print('Max:', max(alturas_jac_centenario))
print('Prom:', round(sum(alturas_jac_centenario) / len(alturas_jac_centenario), 2))

#%%%

## Ejercicio 2.26

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    
    for dic in lista_arboles:
        if dic['nombre_com'] == especie:
            inclinaciones.append(dic['inclinacio'])
            
    return inclinaciones

inclinacion_jac_gralpaz = obtener_inclinaciones(general_paz, 'Jacarandá')
print('Inclinación de Jacarandás en General Paz:', inclinacion_jac_gralpaz)

inclinacion_jac_losandes = obtener_inclinaciones(los_andes, 'Jacarandá')
print('Inclinación de Jacarandás en Los Andes:', inclinacion_jac_losandes)

inclinacion_jac_centenario = obtener_inclinaciones(centenario, 'Jacarandá')
print('Inclinación de Jacarandás en Centenario:', inclinacion_jac_centenario)


#%%%

## Ejercicio 2.27

def especimen_mas_inclinado(lista_arboles):
    esps = especies(lista_arboles)
    
    inclinaciones_por_especie = {}
    
    for especie in esps:
        obt_inc = obtener_inclinaciones(lista_arboles, especie)
        inclinaciones_por_especie[especie] = obt_inc
    
    maximos = {}
    
    for key, value in inclinaciones_por_especie.items():
        maximos[max(value)] = key
        
    return maximos.get(max(maximos)), max(maximos)

print('Arbol con más inclinación en Centenario:', especimen_mas_inclinado(centenario))

print('Arbol con más inclinación en General Paz:', especimen_mas_inclinado(general_paz))

print('Arbol con más inclinación en Los Andes:', especimen_mas_inclinado(los_andes))


#%%% 

## Ejercicio 2.28

def especie_promedio_mas_inclinada(lista_arboles):
    esps = especies(lista_arboles)
    
    prom_inc_por_especie = {} # Diccionario con el promedio de inclinaciones por especie
    
    for especie in esps:
        obt_inc = obtener_inclinaciones(lista_arboles, especie)
        promedio = sum(obt_inc) / len(obt_inc)
        prom_inc_por_especie[promedio] = especie # Clave: promedio, valor: especie
        
    return prom_inc_por_especie.get(max(prom_inc_por_especie)), max(prom_inc_por_especie)

print('Arbol con el promedio de inclinación más alto en Los Andes:', especie_promedio_mas_inclinada(los_andes))
