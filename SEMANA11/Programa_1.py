#Crear una matriz bidimencional de 3x3.
matriz = [
    [40, 70, 20],
    [10, 90, 60],
    [80, 30, 50]
]

# Valor que estamos buscando
valor_buscado = 10

# Inicializar variables para rastrear la posición del valor
fila_encontrada = 1
columna_encontrada = 0

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != 1:
        break

# Verificar si se encontró el valor y mostrar la posición
if fila_encontrada != 0:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")