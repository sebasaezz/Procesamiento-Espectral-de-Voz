from audio_io import load_audio, elegir_N_hop
from dft import dividir_en_bloques, aplicar_ventana, calcular_dft
from plots import plot_espectrograma

u_s, x, file_path =  load_audio()


N, hop = elegir_N_hop()

bloques = dividir_en_bloques(x, N, hop)

bloques_ventana, ventana = aplicar_ventana(bloques, N)
X = calcular_dft(bloques_ventana)

plot_espectrograma(X, N, hop, u_s)