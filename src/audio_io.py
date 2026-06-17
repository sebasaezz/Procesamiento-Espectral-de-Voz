from scipy.io import wavfile
import numpy as np
from scipy.signal.windows import gaussian

import os

def load_audio():

    audio_dir = "audios"

    if not os.path.isdir(audio_dir):
        print("No existe la carpeta 'audios'.")
        return None
    
    files = [
        f for f in os.listdir(audio_dir)
        if f.lower().endswith(".wav")
    ]
    nombre_audio = ""
    if len(files) == 0:
        print("No se encontraron archivos .wav.")
        return None

    #Primero, le pedimos al usuario que escoja un archivo
    else:
        print("\n\n\n\n\n\n")
        print("Se encontraron los siguientes archivos .wav")
        for i, f in enumerate(files):
            print("   ", f"[{i}]" ,f)
        while True:
            try:
                eleccion = int(input("Escriba el número del archivo: "))
            except ValueError:
                print("Escoja un número")
                continue
            if eleccion in range(len(files)):
                nombre_audio = files[eleccion]
                file_path = os.path.join(audio_dir, nombre_audio)
                break
            else:
                print("Elección fuera de rango, intente de nuevo")
    
    u_s, x = wavfile.read(file_path)

    #asegurarse de estar en float
    x = x.astype(np.float32)

    #pasar a mono con promedio
    if x.ndim == 2:
        x = x.mean(axis=1)

    #normalizar en [-1, 1]
    amplitud_max = np.max(np.abs(x))
    if amplitud_max != 0:
        x = x/amplitud_max

    print("Audio cargado, frecuencia de muestreo: ",u_s,"Hz")

    return u_s, x, file_path, amplitud_max, nombre_audio[:-4]

def elegir_parametros():

    M_def= 2048 - 1

    print("\n\n\n\n\n\n")
    print(f"Escoja un valor para M, el largo de los bloques, o presione Enter para valor por defecto: {M_def}")
    print("Se recomiendan valores en forma 2^p - 1. Algunos valores recomendados son:")
    for i in range(9, 15):
        print(f"    -{2**i-1}")
    while True:
        numero_elegido = input("Escriba el valor de M o presiones enter: ")
        if numero_elegido == "":
            M = M_def
            break
        try:
            numero_elegido = int(numero_elegido)
        except ValueError:
            print("Asegúrese de escribir un número")
            continue
        if numero_elegido > 0:
            M = numero_elegido
            break
        else:
            print("Elección fuera de rango, intente de nuevo")
    
    resultado_ventana = escojer_ventana(M)

    print("Usando hop size:", resultado_ventana[0])

    return (M, *resultado_ventana)
    
def escojer_ventana(M):
    ventana = ""

    opciones = ["Sin ventana", "Gauss (reconstruccion sin COLA)", "Triangulo", "Hanning", "Hamming", "Blackman"]
    print("\n\n\n\n\n\n")
    print("Escoja una ventana a usar:")
    for i, opcion in enumerate(opciones):
        print("   ", f"[{i+1}]", opcion)
    print("O presione Enter para ventana por defecto: Hanning")
    while True:
        numero_elegido = input("Escoja un número: ")
        if numero_elegido == "":
            ventana = "Hanning"
            break
        try:
            numero_elegido = int(numero_elegido)
        except ValueError:
            print("Asegúrese de escribir un número")
            continue
        if numero_elegido in range(1,7):
            ventana = opciones[numero_elegido-1]
            break
        else:
            print("Elección fuera de rango, intente de nuevo")

    if ventana == "Sin ventana":
        return M, 1, ventana
    elif ventana == "Gauss (reconstruccion sin COLA)":
        return round((M-1)/2), gaussian(M, std=M/6), ventana
    elif ventana == "Triangulo":
        return round((M-1)/2), np.bartlett(M), ventana
    elif ventana == "Hanning":
        return round((M-1)/2), np.hanning(M), ventana
    elif ventana == "Hamming":
        return round((M-1)/2), np.hamming(M), ventana
    elif ventana == "Blackman":
        return round((M-1)/3), np.blackman(M), ventana
    
def reconstruir_audio(x, u_s, M, nombre_ventana, nombre_audio, nombre_efecto, A_max):

    #Desnormalizar la amplitud
    x = x*A_max

    if x is None:
        print("no se pudo reconstruir el audio")
        return None
    nombre_archivo = nombre_audio + "_" + nombre_ventana + "_" + nombre_efecto + "_" + str(M)

    carpeta_salida = "reconstrucciones"

    x = x.astype(np.int16)

    if not os.path.isdir(carpeta_salida):
        os.makedirs(carpeta_salida)

    ruta_salida = os.path.join(carpeta_salida, nombre_archivo) + ".wav"

    print("Reconstrucción guardada en", ruta_salida)

    wavfile.write(ruta_salida, u_s, x)