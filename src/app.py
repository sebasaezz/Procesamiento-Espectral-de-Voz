from audio_io import load_audio, elegir_parametros, reconstruir_audio
from dft import dividir_en_bloques, aplicar_ventana, calcular_dft
from plots import plot_espectrograma, plot_audio_y_reconstruccion
from reconstruccion import ola
from efectos import efectos, aplicar_efecto

def fujo_consola():
    u_s, x, file_path, A_max, nombre_audio =  load_audio()
    M, hop, expresion_ventana, ventana = elegir_parametros()

    bloques = dividir_en_bloques(x, M, hop)
    bloques_ventana = aplicar_ventana(bloques, expresion_ventana)

    X = calcular_dft(bloques_ventana)

    plot_espectrograma(X, M, hop, u_s, titulo = f"Audio original: {nombre_audio}")

    input("Presione enter para aplicar efecto")

    Y, nombre_efecto = aplicar_efecto(efectos, X)

    x_ola = ola(Y, M, hop)
    reconstruir_audio(x_ola, u_s, M, ventana, nombre_audio, nombre_efecto, A_max)
    plot_audio_y_reconstruccion(audio=x, reconstruccion=x_ola, u_s=u_s)
    plot_espectrograma(Y, M, hop, u_s, titulo = f"Reconstruccion con efecto: {nombre_efecto}")

    input("Presione enter para terminar programa")
