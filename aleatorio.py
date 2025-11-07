import random

# Generar número aleatorio entre 0 y 200
numero_aleatorio = random.uniform(0, 200)

# Calcular el número aumentado en 30%
numero_aumentado = numero_aleatorio + (numero_aleatorio * 0.30)

# Mostrar los resultados
print("=== NÚMERO ALEATORIO CON AUMENTO DEL 30% ===")
print()
print(f"Número aleatorio generado: {numero_aleatorio:.2f}")
print(f"Número aumentado en 30%: {numero_aumentado:.2f}")
print()
print(f"Diferencia: +{numero_aleatorio * 0.30:.2f}")