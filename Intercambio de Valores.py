# Algoritmo de Intercambio de Valores

# Solicitar las dos palabras
print("=== INTERCAMBIO DE VALORES ===")
print()
A = input("Ingrese la palabra A: ")
B = input("Ingrese la palabra B: ")

# Mostrar valores antes del intercambio
print()
print("--- Antes del intercambio ---")
print(f"A = {A}")
print(f"B = {B}")

# Realizar el intercambio usando variable auxiliar
auxiliar = A
A = B
B = auxiliar

# Mostrar valores después del intercambio
print()
print("--- Después del intercambio ---")
print(f"A = {A}")
print(f"B = {B}")

# BONUS: Método pythónico de intercambio (sin variable auxiliar)
print()
print("=== MÉTODO ALTERNATIVO EN PYTHON ===")
# Restaurar valores originales
A = input("Ingrese la palabra A: ")
B = input("Ingrese la palabra B: ")

print()
print("--- Antes del intercambio ---")
print(f"A = {A}")
print(f"B = {B}")

# Intercambio en una sola línea (desempaquetado de tuplas)
A, B = B, A

print()
print("--- Después del intercambio ---")
print(f"A = {A}")
print(f"B = {B}")