from scipy.io import wavfile
import numpy as np
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
                file_path = os.path.join(audio_dir, files[eleccion])
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

    return u_s, x, file_path

def elegir_N_hop():

    N_def, hop_def = 2048, 1024

    print("\n\n\n\n\n\n")
    print(f"Escoja un valor para N, o presione Enter para valor por defecto: {N_def}")
    while True:
        numero_elegido = input("Escoja un número: ")
        if numero_elegido == "":
            N = N_def
            break
        try:
            numero_elegido = int(numero_elegido)
        except ValueError:
            print("Asegúrese de escribir un número")
            continue
        if numero_elegido > 0:
            N = numero_elegido
            break
        else:
            print("Elección fuera de rango, intente de nuevo")

    print("\n\n\n\n\n\n")
    print(f"Escoja un valor para H (hop), o presione Enter para valor por defecto: {hop_def}")
    while True:
        numero_elegido = input("Escoja un número: ")
        if numero_elegido == "":
            hop = hop_def
            break
        try:
            numero_elegido = int(numero_elegido)
        except ValueError:
            print("Asegúrese de escribir un número")
            continue
        if numero_elegido > 0:
            hop = numero_elegido
            break
        else:
            print("Elección fuera de rango, intente de nuevo")

    return N, hop
    