# figuritas.py

# librerías necesarias:
import random
import numpy

#%%
# Ejercicio 4.15
def crear_album(figus_total):
    return np.zeros(figus_total, dtype=np.int64)

#%%
# Ejercicio 4.16
def album_incompleto(A):
    return 0 in A

#%%
# Ejercicio 4.17
def comprar_figu(figus_total):
    figu_comprada = random.randint(1, figus_total)
    return figu_comprada

#%%
# Ejercicio 4.18
def cuantas_figus(figus_total):
    album = np.zeros(figus_total, dtype=np.int64)
    figuritas = 0
    
    while 0 in album:
        figu_comprada = random.randint(1, figus_total)
        album[figu_comprada-1] += 1
        figuritas += 1
    
    return figuritas

#%%
# Ejercicio 4.19
n_repeticiones = 1000

lista = [cuantas_figus(6) for x in range(n_repeticiones)]

promedio = np.mean(lista)
print(promedio)

#%%
n_repeticiones = 100

lista = [cuantas_figus(670) for x in range(n_repeticiones)]

promedio = np.mean(lista)
print(promedio)