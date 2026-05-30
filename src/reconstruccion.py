import numpy as np

def ola(X, M, hop, C = 1):
    
    if X is None:
        return None

    bloques_reconstruidos = np.fft.ifft(X, axis = 1) # Cálculo de inversa
    bloques_reconstruidos = np.real(bloques_reconstruidos) # Quitar ruido de fase

    # Asegurarse de volver al largo
    bloques_reconstruidos = bloques_reconstruidos[:, :M]
    n_bloques = bloques_reconstruidos.shape[0]
    largo_x_r = hop*(n_bloques - 1) + M

    #Lista de ceros
    reconstruccion = np.zeros(largo_x_r)

    for m in range(n_bloques):
        inicio = m*hop
        final = inicio + M
        # Sumar en las posiciones de cada bloque
        reconstruccion[inicio:final] += bloques_reconstruidos[m]

    # Constante de Cola, por defecto 1.    
    reconstruccion = reconstruccion/C
    return reconstruccion

