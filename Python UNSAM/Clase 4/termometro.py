import random
import numpy

#% Ejercicio 4.11

temperatura = 37.5
mu = 0
sigma = 0.2
n = 99

resultado = []
for x in range(n):
    resultado.append(temperatura + random.normalvariate(mu, sigma))

print('El valor máximo es:', max(resultado))
print('El valor mínimo es:', min(resultado))
print('El promedio es:', sum(resultado)/n)
print('La mediana es:', sorted(resultado)[(len(resultado)//2)])

#% Ejercicio 4.13

temperatura = 37.5
mu = 0
sigma = 0.2
n = 999

resultado = []
for x in range(n):
    resultado.append(temperatura + random.normalvariate(mu, sigma))

print('El valor máximo es:', max(resultado))
print('El valor mínimo es:', min(resultado))
print('El promedio es:', sum(resultado)/n)
print('La mediana es:', sorted(resultado)[(len(resultado)//2)])


array = np.array(resultado)
np.save('../Data/Temperaturas.npy', array)