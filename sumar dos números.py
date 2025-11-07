# Programa para sumar dos números

def suma_dos_numeros():
    # Mostrar título
    print("=== SUMA DE DOS NÚMEROS ===")
    print()
    
    # Solicitar los dos números
    print("Ingrese el primer número:")
    numero1 = float(input())
    
    print("Ingrese el segundo número:")
    numero2 = float(input())
    
    # Calcular la suma
    suma = numero1 + numero2
    
    # Mostrar el resultado
    print()
    print(f"La suma de {numero1} + {numero2} = {suma}")

# Ejecutar el programa
if __name__ == "__main__":
    suma_dos_numeros()