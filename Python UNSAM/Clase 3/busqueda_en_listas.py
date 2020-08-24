# busqueda_en_listas.py

#%%

# Ejercicio 3.6. Búsqueda de un elemento

def buscar_u_elemento(lista, elemento):
    posicion = -1
    
    for i, num in enumerate(lista):
        if num == elemento:
            posicion = i

    return posicion

# 
    
def buscar_n_elemento(lista, elemento):
    cuenta = 0
    
    for num in lista:
        if num == elemento:
            cuenta += 1
    
    return cuenta

print(buscar_n_elemento([1,2,3,2,3,4,5,7,5,8,9,5,10], 5))


#%%

# Ejercicio 3.7. Búsqueda de máximo y mínimo

def maximo(lista):
    maximo = lista[0]
    
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
            
    return maximo


print(maximo([1,2,7,2,3,4]))
print(maximo([-5,-4]))

# 

def minimo(lista):
    minimo = lista[0]
    
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    
    return minimo

print(minimo([1,2,7,2,3,4]))
print(minimo([-5,-4]))
