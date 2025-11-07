import random

# Generar número aleatorio entre 10 y 50
numero_aleatorio = random.randint(10, 50)

# Calcular el número disminuido en 15%
numero_disminuido = numero_aleatorio - (numero_aleatorio * 0.15)

# Mostrar los resultados
print("=== NÚMERO ALEATORIO CON DISMINUCIÓN DEL 15% ===")
print()
print(f"Número aleatorio generado: {numero_aleatorio}")
print(f"Número disminuido en 15%: {numero_disminuido:.2f}")