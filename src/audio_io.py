from scipy.io import wavfile
import numpy as np
import os

def load_audio():
    files = os.listdir(os.path.join("audios"))
    for i, f in enumerate(files):
        if not f.endswith(".wav"):
            files.pop(i)
    
    #Primero, le pedimos al usuario que escoja un archivo
    file = ""
    if files == []:
        return False
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
                file = os.path.join("audios", files[eleccion])
                break
            else:
                print("Elección fuera de rango, intente de nuevo")
    
    u_s, x = wavfile.read(file)

    #asegurarse de estar en float
    x = x.astype(np.float32)

    #pasar a mono con promedio
    if x.ndim == 2:
        x = x.mean(axis=1)

    if np.max(np.abs(x)) != 0:
        x = x/np.max(np.abs(x))

    return u_s, x


        