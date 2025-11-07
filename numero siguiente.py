# Programa: Número Siguiente
# Descripción: Calcula el número siguiente al ingresado por el usuario

def numero_siguiente():
    """
    Solicita un número al usuario y muestra el número siguiente
    """
    # Mostrar título
    print("=== NÚMERO SIGUIENTE ===")
    print()
    
    # Solicitar el número
    print("Ingrese un número:")
    numero = float(input())
    
    # Calcular el número siguiente
    siguiente = numero + 1
    
    # Mostrar el resultado
    print()
    print(f"Número ingresado: {numero}")
    print(f"El número siguiente es: {siguiente}")

# Ejecutar el programa
if __name__ == "__main__":
    numero_siguiente()