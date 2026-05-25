from audio_io import load_audio
from dft import dividir_en_bloques, escojer_ventana

u_s, x, file_path =  load_audio()

b = dividir_en_bloques(x, 100, 50)

escojer_ventana()