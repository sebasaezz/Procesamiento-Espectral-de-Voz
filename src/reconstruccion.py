import numpy as np
from scipy.io import wavfile
import os

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

def reconstruir_audio(x, u_s, M, nombre_ventana, nombre_audio, A_max):

    #Desnormalizar la amplitud
    x = x*A_max

    if x is None:
        print("no se pudo reconstruir el audio")
        return None
    nombre_archivo = nombre_audio + "_" + nombre_ventana + "_" + str(M)

    carpeta_salida = "reconstrucciones"

    x = x.astype(np.int16)

    if not os.path.isdir(carpeta_salida):
        os.makedirs(carpeta_salida)

    ruta_salida = os.path.join(carpeta_salida, nombre_archivo) + ".wav"

    print("Reconstrucción guardada en", ruta_salida)

    wavfile.write(ruta_salida, u_s, x)