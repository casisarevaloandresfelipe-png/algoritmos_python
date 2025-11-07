# Algoritmo para calcular el salario de un empleado
# con base en las horas laboradas y el valor de la hora

# Solicitar datos al usuario
numero_horas = int(input("Ingrese el número de horas laboradas: "))
valor_hora = float(input("Ingrese el valor de la hora: "))

# Calcular salario
salario_pagar = numero_horas * valor_hora

# Mostrar resultado
print(f"El salario a pagar es: ${salario_pagar:.2f}")