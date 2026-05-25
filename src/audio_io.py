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
    file = ""
    if files == []:
        return None
    else:
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
                file = os.path.join(audio_dir, files[eleccion])
                break
            else:
                print("Elección fuera de rango, intente de nuevo")
    
    u_s, x = wavfile.read(file)

    #asegurarse de estar en float
    x = x.astype(np.float32)

    #pasar a mono con promedio
    if x.ndim == 2:
        x = x.mean(axis=1)

    #normalizar en [-1, 1]
    amplitud_max = np.max(np.abs(x))
    if amplitud_max != 0:
        x = x/amplitud_max

    return u_s, x


        