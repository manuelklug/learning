#solucion_de_errores.py

#%%

#Ejercicio 3.1. Función tiene_a()

#Comentario:
'''
El problema está en utilizar 'return': Python al leer este comando por primera vez
corta la ejecución de la función. Entonces, el resultado de la función iba a quedar 
condicionado por la primer letra de la expresión, no importando si luego sí había una letra 'a'
Error: líneas 20 y 22 (return).
Solución: cambiar 'return' por 'print':
'''

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            print(True)
        else:
            print(False)
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%

#Ejercicio 3.2. Función tiene_a()

#Comentario:
'''
El código posee varios errores:
1) No se usan los : 
2) Utilizar del operador de asignación (=) cuando se quiere 
realizar una comparación (==).
3) Utilizar 'Falso' en vez de 'False'
Error al no utilizar ":": línea 43, 46, 47
Error al usar = en vez de ==: 48.
Error al usar Falso en vez de False: 54.
Solución: incorporar los :, cambiar el = por == y Falso por False.
'''

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')


#%%

# Ejercicio 3.3. Tipos.

# Comentario:
'''
La función no funciona cuando sus argumentos no son strings.
Error: línea 85, el argumento es de tipo int.
Solución: convertir el argumento de la línea 85 a tipo string. 
'''


def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(str(1984))

#%%

# Ejercicio 3.4. Alcances

# Comentario:
'''
La función no devuelve ningún valor porque no utiliza ni print ni return.
Error: no se devuelve el valor de c.
Solución: Agregar una nueva línea dentro de la función que devuelva el valor de c ('return c')
'''

def suma(a,b):
    c = a + b
    return c
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%

# Ejercicio 3.5. Pisando memoria

# Comentario:
'''
El problema es que la función devolverá una lista (camión) con 7 diccionarios, pero que 
todos tendrán los mismos datos (keys y values iguales) debido a el lugar en donde se 
definió la variable registro.
Error: Línea 124. Diccionario registro.
Solución: Definirlo dentro del ciclo for.
'''

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)
