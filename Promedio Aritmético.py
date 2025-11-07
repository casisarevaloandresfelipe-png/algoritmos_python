# Cálculo del Promedio Aritmético de Tres Números

print("=== CÁLCULO DEL PROMEDIO ARITMÉTICO ===")
print()

# Solicitar los tres números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio aritmético
promedio = (numero1 + numero2 + numero3) / 3

# Mostrar resultados
print()
print("=== RESULTADO ===")
print(f"Los números ingresados son: {numero1}, {numero2}, {numero3}")
print(f"El promedio aritmético es: {promedio:.2f}")