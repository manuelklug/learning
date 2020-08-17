# tabla_informe.py

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

# Hacer informe

def hacer_informe(cajones, precios):
    lista = []
    
    for dic in cajones:
        nombre = dic['nombre']
        cajones = dic['cajones']
        precio = dic['precio']
        cambio = precios[nombre] - dic['precio']
        
        tupla = (nombre, cajones, precio, cambio)
        
        lista.append(tupla)
    
    return lista

camion = leer_camion('Data/camion.csv')
precios = leer_precios('Data/precios.csv')
informe = hacer_informe(camion, precios)

# Tabla

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')


header_espaciado = ''

for valor in headers:
    header_espaciado += f'{valor:>10s} '
    
separacion = ''
    
for x in range(len(headers)):
    separacion += '---------- '

print(header_espaciado)
print(separacion)

for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')