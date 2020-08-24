def propagar(lista):
    
    # Propagación hacia la derecha (para adelante)
    for i in range(0, len(lista)-1):
        if lista[i] == 1 and lista[i+1] == 0:
            lista[i+1] = 1
    
    # Propagación hacia la izquierda (para atrás)
    for j in range(len(lista)-1, 0, -1):
        if lista[j] == 1 and lista[j-1] == 0:
            lista[j-1] = 1
            
    return lista


print(propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
