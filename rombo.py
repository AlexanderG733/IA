def rombo(n):
    # Parte superior
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

    # Parte inferior
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Especifica el número de filas que deseas
filas = 5
rombo(filas)