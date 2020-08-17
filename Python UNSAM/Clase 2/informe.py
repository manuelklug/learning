# informe.py

import csv

# Funcion leer_camion

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))

            cajon = {
            'nombre': record['nombre'],
            'cajones': int(record['cajones']),
            'precio': float(record['precio'])
            }

            camion.append(cajon)

    return camion

# Funcion leer precios

def leer_precios(nombre_archivo):
    precios = {}

    with open(nombre_archivo) as file:
        rows = csv.reader(file)
        
        for row in rows:
            try:
                fruta = row[0]
                precio = float(row[1])
                precios[fruta] = precio
            except:
                print("Una fila no pudo ser leída")

    return precios

# Informe

camion = leer_camion('Data/camion.csv')
precios = leer_precios('Data/precios.csv')

costo_total = 0
ventas = 0

for cajon in camion:
    fruta = cajon['nombre']
    cajones = cajon['cajones']
    costo = cajon['precio']
    
    if fruta in precios:
        costo_total += cajones * costo
        ventas += precios[fruta] * cajones

resultado_neto = round(ventas - costo_total, 2)

print(f'Costo total: ${costo_total}')
print(f'Ventas: ${ventas}')
print(f'Resultado neto: ${resultado_neto}')