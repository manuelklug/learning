import random

def generala_no_servida():
    tirada = []
    
    for i in range(5):
        tirada.append(random.randint(1,6))
        
    maximo = max(tirada, key=tirada.count)

    for index, num in enumerate(tirada):
        if num != maximo:
            valor = 0
        
            for j in range(2):
                valor = random.randint(1,6)
                
                if valor == maximo:
                    break
        
            tirada.remove(num)
            tirada.insert(index, valor)
    
    return tirada

def es_generala(tirada):
    return min(tirada) == max(tirada)

N = 100000
G = sum([es_generala(generala_no_servida()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')