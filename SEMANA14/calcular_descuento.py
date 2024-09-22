# Crea una funcion para calcular el descuento utlizando el valor de compra y del descuento
def calcular_descuento(monto_total, porcentaje_descuento=30):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Bucle while True para mantener funcionanado el programa y usaremos ´try´para capturar errores
while True:
    try:
     # Solicitar al usuario el monto total
        monto_total = input("Ingrese el valor de su compra (o escriba 'salir' para terminar): ")
     # Utilizaremos ´lower´para convertir los caracteres a minuscula para evitar errores
        if monto_total.lower() == 'salir':
            break
        monto = float(monto_total)
    # Solicitar al usuario el porcentaje de descuento
        porcentaje_descuento = input("Ingrese el porcentaje de descuento (precione Enter para usar 30%): ")
        if not porcentaje_descuento:
            porcentaje = 30
        else:
            porcentaje = float(porcentaje_descuento)
    # Primera llamada a la funcion calcular_descuento
    # Aqui se calculara el descuento basado en el monto total y el porcentaje ingresado
        descuento = calcular_descuento(monto, porcentaje)
    # Calcular el monto final a pagar despues de aplicar el descuento
        monto_final = monto - descuento
    # Mostrar los resultados
        print(f"\nMonto total: ${monto:.2f}")
        print(f"Descuento: ${descuento:.2f}")
        print(f"Monto Final a pagar: ${monto_final:.2f}\n")


    # Solicitar al usuario un segundo monto para calcular un nuevo descuento
        segundo_monto = input("Ingrese otro monto total de la compra (o escriba 'salir' para terminar): ")
    # Nuevamente utilizaremos ´lower´para convertir a miniscula
        if segundo_monto.lower() == 'salir':
            break
        segundo_monto = float(segundo_monto)
    # Solicitar al usuario un segundo porcentaje
        segundo_porcentaje = float(input("Ingrese el porcentaje de descuento para este segundo monto:"))
    # Segunda llamada a la funcion calcular_descuento con nuevos valores
        segundo_descuento = calcular_descuento(segundo_monto, segundo_porcentaje)
        segundo_monto_final = segundo_monto - segundo_descuento
    # Mostrar los resultados
        print(f"\nSegundo Monto Total: ${segundo_monto:.2f}")
        print(f"Segundo Descuento: ${segundo_descuento:.2f}")
        print(f"Segundo Monto Final a Pagar: ${segundo_monto_final:.2f}\n")
     # Utilizaremos´except ValueError´ para capturar errores y mostrar un mensaje al usuario
    # pidiendole que ingrese un valor válido
    except ValueError:
        print("Por favor, ingrese un número válido.")
    # Usaremos´except KeyboardInterrupt´ por si el usuario interrumpe el programa con un ´Ctrl+C´
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        break
