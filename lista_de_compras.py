print("#------------------------#")
print("#--| lista de compras |--#")
print("#------------------------#")
lista_compras = []
producto = ""
while producto.lower() != "fin":
    producto = input("ingresa un producto (escribe 'fin' para terminar): ")
    if producto.lower() != "fin":
        lista_compras.append(producto)
        print("producto agregado a la lista.")
print("\n--- lista de compras ---")
if len(lista_compras) == 0:
    print("no se ingresaron productos.")
else:
    for item in lista_compras:
        print(f"- {item}")