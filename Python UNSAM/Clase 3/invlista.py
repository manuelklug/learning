# invlista.py

def invertir_lista(lista):
    invertida = []
    for e in lista: 
        invertida.insert(0, e)
        
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))