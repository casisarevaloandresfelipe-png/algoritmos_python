# Algoritmo nota definitiva

print("=== CÁLCULO DE NOTA DEFINITIVA ===")
print()

# Leer las 4 notas
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))

# Calcular la suma y el promedio
suma = nota1 + nota2 + nota3 + nota4
definitiva = suma / 4

# Mostrar el resultado
print()
print(f"Su nota definitiva es: {definitiva:.2f}")

# Opcional: Mostrar estado (aprobado/reprobado)
if definitiva >= 3.0:
    print("Estado: APROBADO ✓")
else:
    print("Estado: REPROBADO ✗")