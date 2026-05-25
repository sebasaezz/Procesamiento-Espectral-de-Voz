import numpy as np

def dividir_en_bloques(x, N, hop):
    if len(x) < N:
        print("La señal es más corta que el tamaño de bloque.")
        return None

    bloques = []
    n_bloques = (len(x)-N)//hop + 1

    for m in range(n_bloques):
        bloque = x[m*hop : m*hop + N]
        bloques.append(bloque)
    
    return np.array(bloques)

