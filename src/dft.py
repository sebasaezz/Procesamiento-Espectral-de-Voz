import numpy as np
from scipy.signal.windows import gaussian

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

def aplicar_ventana(bloques, N):
    ventana = escojer_ventana(N)

    return bloques*ventana, ventana

def escojer_ventana(N):
    ventana = ""

    opciones = ["Sin ventana", "Gauss", "Triangulo", "Hanning", "Hamming", "Blackman"]

    print("Escoja una ventana a usar:")
    for i, opcion in enumerate(opciones):
        print("   ", f"[{i+1}]", opcion)

    while True:
        try:
            numero_elegido = int(input("Escoja un número: "))
        except ValueError:
            print("Asegúrese de escribir un número")
            continue
        if numero_elegido in range(1,7):
            ventana = opciones[numero_elegido-1]
            break
        else:
            print("Elección fuera de rango, intente de nuevo")

    if ventana == "Sin ventana":
        return 1
    elif ventana == "Gauss":
        return gaussian(N, std=N/6)
    elif ventana == "Triangulo":
        return np.bartlett(N)
    elif ventana == "Hanning":
        return np.hanning(N)
    elif ventana == "Hamming":
        return np.hamming(N)
    elif ventana == "Blackman":
        return np.blackman(N)