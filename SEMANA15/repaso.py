# Diccionario con informacion personal de los integrantes de una banda de K-POP

informacion_integrantes = {
    "integrante1" : {
        "nombre" : "Kim Namjoon",
        "edad" : 30,
        "ciudad" : "Corea del Sur",
        "profesion" : "Rapper"
    },
    "integrante2" : {
        "nombre" : "Kim SeokJin",
        "edad" : 33,
        "ciudad" : "Corea del Sur",
        "profesion" : "Vocalista"
    },
    "integrante3" : {
        "nombre" : "Min Yoongi",
        "edad" : 32,
        "ciudad" : "Corea del Sur",
        "profesion" : "Rapper"
    },
    "integrante4" : {
        "nombre" : "Jung Hoseok",
        "edad" : 29,
        "ciudad" : "Corea del Sur",
        "profesion" : "Dancer"
    },
    "integrante5" : {
        "nombre" : "Park Jimin",
        "edad" : 28,
        "ciudad" : "Corea del Sur",
        "profesion" : "Vocalista"
    },
    "integrante6" : {
        "nombre" : "Kim Taehyung",
        "edad" : 28,
        "cuidad" : "Corea del Sur",
        "profesion" : "Vocalista"
    },
    "integrante7" : {
        "nombre" : "Jeon Jungkook",
        "edad" : 27,
        "ciudad" : "Corea del Sur",
        "profesion" : "Vocalista"
    }
}
# Modificamos la ciudad de Kim Namjoon
informacion_integrantes ["integrante1"] ["ciudad"] = "Buenos Aires"

# Agregamos un telefono a Kim SeokJin
informacion_integrantes ["integrante2"] ["telefono"] = "010-1243-5679"

# Verificamos si la clave "telefono" existe para Min Yoongi
if "telefono" not in informacion_integrantes ["integrante3"]:
    informacion_integrantes ["integrante3"] ["telefono"] = "010-0545-2010"

# Eliminamos la clave "edad" de todos los integrantes
for integrante in informacion_integrantes :
    del informacion_integrantes [integrante] ["edad"]

# Imprimimos del diccionario final
print("Diccionario Final:", informacion_integrantes)

# Función para buscar información
def buscar_informacion_integrantes(diccionario):
    while True:
        clave = input("¿Qué información deseas buscar? (integrante 1,2,3,4,5,6,7) o escribe 'salir' para terminar: ")
        if clave.lower() == "salir":
            print("Saliendo del programa.")
            break
        elif clave in diccionario:
            print(f"{clave.capitalize()}: {diccionario[clave]}")
        else:
            print("La clave no existe en el diccionario. Inténtalo de nuevo.")

# Llamar a la función de búsqueda
buscar_informacion_integrantes(informacion_integrantes)

