import fileparse

# Funcion leer_camion

def leer_camion(nombre_archivo):
    return fileparse.parse_csv(nombre_archivo, select=['nombre','cajones','precio'], types=[str,int,float], has_headers=True)

# Funcion leer precios

def leer_precios(nombre_archivo):
    return dict(fileparse.parse_csv(nombre_archivo, types=[str, float], has_headers=False))

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