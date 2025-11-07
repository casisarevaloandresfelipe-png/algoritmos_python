# Algoritmo Operación Módulo en Python

def operacion_modulo():
    """
    Calcula el residuo de dividir dos números enteros
    """
    print("=== OPERACIÓN MÓDULO ===")
    print()
    
    try:
        # Solicitar los dos números
        print("Ingrese el primer número:")
        numero1 = int(input())
        
        print("Ingrese el segundo número:")
        numero2 = int(input())
        
        # Validar que el divisor no sea cero
        if numero2 == 0:
            print("\nError: No se puede calcular el módulo con divisor 0")
            return
        
        # Calcular la operación módulo
        resultado = numero1 % numero2
        
        # Mostrar el resultado
        print()
        print("=== RESULTADO ===")
        print(f"{numero1} MOD {numero2} = {resultado}")
        print()
        print(f"El residuo de dividir {numero1} entre {numero2} es: {resultado}")
        
    except ValueError:
        print("\nError: Por favor ingrese solo números enteros válidos")

# Ejecutar el programa
if __name__ == "__main__":
    operacion_modulo()