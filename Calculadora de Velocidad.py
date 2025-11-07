# Calculadora de Velocidad
print("=== CALCULADORA DE VELOCIDAD ===\n")

# Solicitar distancia
distancia = float(input("Ingresa la distancia en km: "))

# Solicitar tiempo
tiempo = float(input("Ingresa el tiempo en horas: "))

# Validar que el tiempo no sea cero
if tiempo == 0:
    print("\nError: El tiempo no puede ser cero")
else:
    # Calcular velocidad
    velocidad = distancia / tiempo
    
    # Mostrar resultado
    print(f"\nTu velocidad es: {velocidad:.2f} km/h")