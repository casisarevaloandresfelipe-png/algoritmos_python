def obtener_dato(mensaje):
    """Solicita un dato y valida que no esté vacío"""
    while True:
        dato = input(mensaje).strip()
        if len(dato) > 0:
            return dato
        else:
            print("Error: El nombre no puede estar vacío")
            print()

# Solicitar los datos
print("=== PAÍS Y CAPITAL ===")
print()

pais = obtener_dato("Ingrese el nombre del país: ")
capital = obtener_dato("Ingrese el nombre de la capital: ")

# Mostrar el resultado
print()
print(f"{capital} es la capital de {pais}.")