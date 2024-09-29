# Crear un diccionario que contenga información ficticia sobre una persona
# incluyendo claves "nombre", "edad", "ciudad" y "profesión"

informacion_personal = {
    "nombre": "Gojo Saturo",
    "edad": 27,
    "ciudad": "Tokio",
    "profesión": "Hechicero"
}

# Acceder y modificar valores
# Acceder al valor de la clave "ciudad", para esto usaremos la clave entre corchetes
ciudad_actual = informacion_personal["ciudad"]

# Modificar el valor de la clave "ciudad" para que sea diferente
informacion_personal["ciudad"] = "Mexico"

# Ingresar una nueva clave_valor
informacion_personal["telefono"] = "011-486-4041"

# Verificar la existencia de la clave "telefono" existente en el diccionario
# Usaremos el operador "in" si no existe la agregamos con un nuevo número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "011-486-4041"

# Ahora vamos a eliminar la clave "edad" del diccionario utilizando el metodo "del"
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print("Diccionario Final:", informacion_personal)

# Función para buscar información
def buscar_informacion(diccionario):
    while True:
        clave = input("¿Qué información deseas buscar? (nombre, ciudad, profesión, teléfono) o escribe 'salir' para terminar: ")
        if clave.lower() == "salir":
            print("Saliendo del programa.")
            break
        elif clave in diccionario:
            print(f"{clave.capitalize()}: {diccionario[clave]}")
        else:
            print("La clave no existe en el diccionario. Inténtalo de nuevo.")

# Llamar a la función de búsqueda
buscar_informacion(informacion_personal)

