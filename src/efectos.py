import numpy as np

#Función general para aplicar efectos
def aplicar_efecto(efectos: dict, X):
    print("\n\n\n\n\n")
    print("Escoja un efecto: ")
    for i, efecto in enumerate(efectos):
        print(f"    [{i}] {efecto}")

    while True:
        try: 
            n_elegido = int(input("Eliga un numero: "))
            if n_elegido not in range(len(efectos)):
                print("Ingrese un número dentro del rango")
                continue
            else:
                eleccion = list(efectos.keys())[n_elegido]
                break
        except ValueError:
            print("Ingrese un número")
            continue
    
    return (efectos[eleccion](X), eleccion)

def sin_efecto(X):
    Y = X
    return Y

def anular_fase(X):
    Y = np.abs(X)
    return Y

def proyeccion_real(X):
    Y = np.real(X)
    return Y

efectos = {
    "Sin efecto": sin_efecto,
    "Anular Fase": anular_fase,
    "Proyeccion Real": proyeccion_real
}