# Desarrollo de una funcion para calcular la temperatura promedio de una ciudad durante un periodo de tiempo

matriz_temp = [
    [ # Ciudad A - Cuenca
        [20, 22, 21, 19], # semana1
        [21, 13, 20, 22], # semana2
        [19, 20, 21, 20], # semana3
        [22, 21, 23, 24], # semana4
    ],
    [ # Ciudad B - Loja
        [15, 16, 17, 15], # semana1
        [17, 16, 18, 20], # semana2
        [17, 15, 22, 23], # semana3
        [20, 21, 22, 24], # semana4
    ],
    [ # Ciudad C - Quito
        [25, 26, 27, 24], # semana1
        [26, 27, 28, 25], # semana2
        [24, 25, 26, 27], # semana3
        [27, 25, 26, 27], # semana4
    ]
]

# Función para calcular el promedio de temperaturas de una ciudad y una semana específica
def promedio_temp_ciudad(matriz_temp, ciudad, semana):
    acumulador = 0
    for temperatura in matriz_temp[ciudad][semana]:
        acumulador += temperatura
    promedio = acumulador / len(matriz_temp[ciudad][semana])
    return promedio


ciudad1 = 0  # Ciudad A - Cuenca
semana1 = 0  #semana1
resultado_prom = promedio_temp_ciudad(matriz_temp, ciudad1, semana1)
print(resultado_prom)
ciudad3 = 2 # Ciudad C -  Quito
semana3 = 3 #semana3
resultado_prom = promedio_temp_ciudad(matriz_temp, ciudad3, semana3)
print(resultado_prom)
ciudad2 = 1 #Ciudad B - Loja
semana4 = 3 #semana4
resultado_prom = promedio_temp_ciudad(matriz_temp, ciudad2, semana4)
print(resultado_prom)

#  al mometo de llamar a la funcion salia un error y para eso se definieron dos variables, en este caso son ciudad y semana
# para asi poder especificar la ciudad y semana que queremos analizar.

