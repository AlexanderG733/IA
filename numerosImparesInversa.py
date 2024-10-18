def imprimir_impares_inverso(inicio, fin):
    # Crear una lista para almacenar los números impares
    impares = []

    # Recorrer el rango de inicio a fin
    for num in range(inicio, fin + 1):
        if num % 2 != 0:  # Verifica si el número es impar
            impares.append(num)

    # Imprimir los números impares en orden inverso
    for num in range(inicio, fin + 1):
        if num % 2 != 0:  # Verifica si el número es impar
            impares.append(num)

    # Imprimir los números impares en orden inverso, separados por comas
    print(", ".join(map(str, reversed(impares))))


# Ejemplo de uso
imprimir_impares_inverso(1, 20)