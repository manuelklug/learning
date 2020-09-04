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

# Función hacer informe

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


#%%
    
# Función imprimir informe con formato
    
def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
imprimir_informe(informe)