import numpy as np
import matplotlib.pyplot as plt

def plot_espectrograma(X, M, hop, u_s, titulo):
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
    plt.title(titulo)
    plt.show(block=False)

def plot_audio_y_reconstruccion(audio, reconstruccion, u_s, t_inicio=0, t_final=None):
    L = min(len(audio), len(reconstruccion))

    if t_final is None:
        t_final = L / u_s

    i_inicio = int(t_inicio * u_s)
    i_final = int(t_final * u_s)

    i_inicio = max(0, i_inicio)
    i_final = min(L, i_final)

    audio_plot = audio[i_inicio:i_final]
    reconstruccion_plot = reconstruccion[i_inicio:i_final]

    t = np.arange(i_inicio, i_final) / u_s

    plt.figure(figsize=(12, 6))

    plt.subplot(3, 1, 1)
    plt.plot(t, audio_plot)
    plt.title("Audio original")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(t, reconstruccion_plot)
    plt.title("Audio reconstruido")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    diferencia = reconstruccion_plot - audio_plot

    rmse_relativo = (
        np.sqrt(np.mean(diferencia**2)) /
        np.sqrt(np.mean(audio_plot**2))
    )

    plt.subplot(3, 1, 3)
    plt.plot(t, diferencia)
    plt.title(f"Diferencia Audio - Reconstrucción\nRMSE relativo = {rmse_relativo:.6f}")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True)

    plt.tight_layout()
    plt.show(block=False)