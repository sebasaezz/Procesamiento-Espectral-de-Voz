import numpy as np

def dividir_en_bloques(x, M, hop):
    if len(x) < M:
        print("La señal es más corta que el tamaño de bloque.")
        return None

    bloques = []
    n_bloques = (len(x)-M)//hop + 1

    for m in range(n_bloques):
        bloque = x[m*hop : m*hop + M]
        bloques.append(bloque)
    
    return np.array(bloques)

def aplicar_ventana(bloques, expresion_ventana):

    if bloques is None:
        return None

    return bloques*expresion_ventana
    
def calcular_dft(bloques):
    if bloques is None:
        return None

    # Como cada bloque tiene duracion M-1 para que sean pares, se hacee un pequeño zero padding
    # se agrega un cero al final de cada bloque
    bloques_padded = np.pad(bloques, ((0, 0), (0, 1)), mode="constant")

    #Calculamos usando np
    dft = np.fft.fft(bloques_padded, axis=1)

    return dft