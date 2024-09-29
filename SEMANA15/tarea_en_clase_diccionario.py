# Realize la captura desde el teclado de los siguientes datos:
# Nombre del libro, categoria, año de publicación, número de hojas, autor
# Guardar en una variable libros
# Imprimir el listado

# Inicializamos una lista para almacenar los libros
libros = [
    {
        "nombre": "El Principito",
        "categoria": "Novela filosófica",
        "año_publicación": 1943,
        "num_hojas": 93,
        "autor": "Antoine de Saint-Exupéry"
    },
    {
        "nombre": "La canción de Aquiles",
        "categoria": "Novela histórica",
        "año_publicación": 2011,
        "num_hojas": 384,
        "autor": "Madeline Miller"
    }
]

# Función para capturar datos de un libro
def capturar_libro():
    nombre = input("Introduce el nombre del libro: ")
    categoria = input("Introduce la categoría del libro: ")
    año_publicación = input("Introduce el año de publicación: ")
    num_hojas = input("Introduce el número de hojas: ")
    autor = input("Introduce el autor del libro: ")

# Crear un diccionario con la información del libro
    libro = {
        "nombre": nombre,
        "categoria": categoria,
        "año_publicación": año_publicación,
        "num_hojas": num_hojas,
        "autor": autor
    }
    return libro


# Captura los datos de libros hasta que el usuario decida detenerse
while True:
    libro = capturar_libro()
    libros.append(libro)  #Utilizamos esto por si el usuario desea ingresar un libro aparte de los que estan en la lista
    respuesta = input("¿Desea agregar otro libro? (s/n): ")
    if respuesta.lower() != "s":
        break

# Imprimir listado de libros
print("\nListado de Libros:")
for i, libro in enumerate(libros, start=1):
    print(f"Libro {i}:")
    print(f"Nombre: {libro['nombre']}")
    print(f"Categoría: {libro['categoria']}")
    print(f"Año de publicación: {libro['año_publicación']}")
    print(f"Número de hojas: {libro['num_hojas']}")
    print(f"Autor: {libro['autor']}\n")

