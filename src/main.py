from audio_io import load_audio
from dft import dividir_en_bloques, aplicar_ventana, calcular_dft

u_s, x, file_path =  load_audio()

N = 2000
hop = 200

bloques = dividir_en_bloques(x, N, hop)

bloques_ventana = aplicar_ventana(bloques, N)
calcular_dft(bloques_ventana)
