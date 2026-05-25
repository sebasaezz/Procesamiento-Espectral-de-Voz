import numpy as np
import matplotlib.pyplot as plt

def plot_espectrograma(X, N, hop, u_s):
    S = np.abs(X)
    k_n = N//2
    S = S[:, : k_n+1]
    S = 20*np.log10(S)
    S = np.transpose(S)
    S = np.flip(S, axis=0)

    n_bloques = X.shape[0]
    T_s = 1/u_s
    t_max = T_s*((n_bloques)*hop + N/2)
    plt.figure(figsize=(10,5))
    plt.imshow(S, aspect="auto", extent=(T_s*N/2, t_max, 0, u_s/2))
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Frecuencia [Hz]")
    plt.yscale("symlog", linthresh=100)
    plt.show()