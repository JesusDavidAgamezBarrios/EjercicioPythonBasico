# Solicitar al usuario ingresar el número n de días
n = int(input("Ingrese el número de días: "))

# Si n es menor o igual a 1, no hay alzas
if n <= 0:
    print("No hubo alzas.")
else:
    # Crear una lista vacía para almacenar los precios del dólar para cada día
    precios_dolares = []

    # Solicitar al usuario ingresar el precio del dólar para cada uno de los n días
    for i in range(n):
        precio_dolar = float(input(f"Ingrese el precio del dólar para el día {i+1}: "))
        precios_dolares.append(precio_dolar)

    # Crear una lista vacía para almacenar las alzas de un día para el otro
    alzas = []

    # Calcular las alzas de un día para el otro
    for i in range(n-1):
        alza = precios_dolares[i+1] - precios_dolares[i]
        alzas.append(alza)

    # Buscar la mayor alza
    mayor_alza = max(alzas)

    # Mostrar la mayor alza
print(f"La mayor alza fue de {mayor_alza}.")