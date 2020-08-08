# inclusive.py

frase = 'todos somos programadores'
palabras = frase.split()

for palabra in palabras:
    if palabra.endswith("os"):
        indice = palabras.index(palabra) # Busca el index de la palabra
        palabra_inclusiva = palabra.replace("os", "es") # Modifica la palabra a lenguaje inclusivo
        del palabras[indice] # Elimina la palabra vieja de la lista
        palabras.insert(indice, palabra_inclusiva) # Inserta la palabra en lenguaje inclusivo

frase_t = " ".join(palabras)
print(frase_t)