# diccionario para almacenar los precios de los productos
precios = {'A': 270, 'B': 340, 'C': 390}

# lista vacía para almacenar las monedas ingresadas
monedas = []

# Preguntar al usuario qué producto quiere y obtener el precio correspondiente
while True:
    producto = input("Seleccione el producto (A, B o C): ")
    if producto in precios:
        precio = precios[producto]
        break
    else:
        print("Producto inválido. Intente de nuevo.")

# Solicitar al usuario ingresar las monedas hasta alcanzar el monto a pagar
while True:
    moneda = int(input("Ingrese una moneda (10, 50 o 100): "))
    if moneda in [10, 50, 100]:
        monedas.append(moneda)
        total = sum(monedas)
        if total >= precio:
            break
    else:
        print("Moneda inválida. Intente de nuevo.")

# Calcular las monedas de vuelto y entregarlas una por una
monedasdeVuelto = sorted([100, 50, 10], reverse=True)

print("\nMonedas de vuelto:")
total -= precio  # calcular el cambio
for moneda in monedasdeVuelto:
    while total >= moneda:
        print(f"Devolviendo una moneda de ${moneda}.")
        total -= moneda