def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = [1] * (i + 1) + [0] * (n - i - 1)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(",".join(map(str, fila)))

# Dimensiones de la matriz
n = 6
matriz = crear_matriz(n)
imprimir_matriz(matriz)