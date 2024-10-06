# Programa para escribir notas personales desde un archivo de texto

# Crear un nuevo archivo llamado my_notes.txt y escribir tres líneas de texto personales en el archivo
with open("my_notes.txt", "w") as file:
    file.write("Linea1: Terminar las tareas a tiempo.\n")
    file.write("Linea2: Ver el anime que se estreno el sabado.\n")
    file.write("Linea3: Comprar medicina para la gripe.\n")

# Metodo writelines(): escribir una lista de lineas
lineas = [ "Linea4: Finalizamos.\n"]
with open("my_notes.txt", "a") as file:  # Usamos "a" para añadir al archivo existente
    file.writelines(lineas)

# Lectura del archivo de texto
# Abre el archivo my_notes.txt y lee el contenido línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # muestra cada línea leída en la consola

# Nota: El uso de 'with' asegura que el archivo se cierre automáticamente
