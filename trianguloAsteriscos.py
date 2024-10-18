def cono_invertido(n):
    for i in range(n, 0, -1):
        # Imprimir espacios
        print(' ' * (n - i), end='')
        # Imprimir asteriscos
        print('*' * (2 * i - 1))

# Especifica el número de filas que deseas
filas = 5
cono_invertido(filas)