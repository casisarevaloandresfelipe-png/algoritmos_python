def main():
    # Mostrar título
    print("=== CUADRADO Y CUBO DE UN NÚMERO ===")
    print()
    
    # Solicitar el número al usuario
    try:
        numero = float(input("Ingrese un número: "))
        
        # Calcular el cuadrado y el cubo
        cuadrado = numero ** 2
        cubo = numero ** 3
        
        # Mostrar los resultados
        print()
        print(f"Número ingresado: {numero}")
        print(f"El cuadrado es: {cuadrado}")
        print(f"El cubo es: {cubo}")
        
    except ValueError:
        print("Error: Debe ingresar un número válido")

# Ejecutar el programa
if __name__ == "_main_":
    main()