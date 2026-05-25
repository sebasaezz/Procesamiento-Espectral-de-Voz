from audio_io import load_audio
from dft import dividir_en_bloques, aplicar_ventana, calcular_dft

u_s, x, file_path =  load_audio()

N = 100
hop = 50

bloques = dividir_en_bloques(x, N, hop)

aplicar_ventana(bloques, N)
dft = calcular_dft(bloques)

print(dft)