import numpy as np
import matplotlib.pyplot as plt

def plot_espectrograma(X, M, hop, u_s):
    S = np.abs(X)
    k_n = M//2
    S = S[:, : k_n+1]
    S = 20*np.log10(S)
    S = np.transpose(S)
    S = np.flip(S, axis=0)

    n_bloques = X.shape[0]
    T_s = 1/u_s
    t_max = T_s*((n_bloques)*hop + M/2)
    plt.figure(figsize=(10,5))
    img = plt.imshow(S, 
                     aspect="auto", 
                     extent=(T_s*M/2, t_max, 0, u_s/2),
                     cmap = "magma"
                     )
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Frecuencia [Hz]")
    plt.yscale("symlog", linthresh=100)
    plt.colorbar(img, label="Magnitud relativa [dB]")
    plt.show(block=False)

def plot_audio_y_reconstruccion(audio, reconstruccion, u_s):
    L = min(len(audio), len(reconstruccion))

    audio_plot = audio[:L]
    reconstruccion_plot = reconstruccion[:L]

    t = np.arange(L) / u_s

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, audio_plot)
    plt.title("Audio original")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(t, reconstruccion_plot)
    plt.title("Audio reconstruido")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show(block=False)