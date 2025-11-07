import math

# Solicitar el radio al usuario
print("=== CÁLCULO DE CÍRCULO ===")
r = float(input("Ingrese el radio en cm: "))

# Validar que el radio sea positivo
if r <= 0:
    print("Error: El radio debe ser mayor que 0")
else:
    # Calcular superficie y perímetro
    superficie = math.pi * r**2
    perimetro = 2 * math.pi * r
    
    # Mostrar resultados
    print("--------------------------------")
    print(f"Radio: {r} cm")
    print(f"Superficie (área): {superficie:.2f} cm²")
    print(f"Perímetro (circunferencia): {perimetro:.2f} cm")
    print("--------------------------------")