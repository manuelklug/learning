# envido.py

import random

def envido():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    
    mano = random.sample(naipes, k=3)
    
    valores_cartas = [mano[i][0] for i in range(len(mano))] # Primer valor de cada tupla
    
    palos_cartas = [mano[i][1] for i in range(len(mano))] # Segundo valor de cada tupla
    
    if len(set(palos_cartas)) == 3: # 3 cartas de distinto palo
        return max(valores_cartas) + 20
        
    elif len(set(palos_cartas)) == 2: # Hay 2 cartas del mismo palo
        max_rep = max(palos_cartas, key=palos_cartas.count) # Palo que se repite
        # Suma el valor de la carta si esa carta es del palo de max_rep y si no es 10, 11 y 12 (porque equivale a puntaje 0)
        return sum([mano[i][0] for i in range(len(mano)) if (max_rep in mano[i][1]) and (mano[i][0] not in [10, 11, 12])]) + 20
    
    elif len(set(palos_cartas)) == 1:
        return 0

def maximo_puntaje(puntaje):
    if puntaje in [31, 32, 33]:
        return 1
    else:
        return 0

N = 100000
G = sum([maximo_puntaje(envido()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué puntaje máximo (31, 32 o 33.')
print(f'La probabilidad de sacar mayor puntaje es {prob:.6f}.')