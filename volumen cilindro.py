import math

def calcular_volumen_cilindro(radio, altura):
    """
    Calcula el volumen de un cilindro.
    
    Args:
        radio: Radio del cilindro
        altura: Altura del cilindro
    
    Returns:
        Volumen del cilindro
    """
    return math.pi * (radio ** 2) * altura

def obtener_numero_positivo(mensaje):
    """
    Solicita un número positivo al usuario con validación.
    
    Args:
        mensaje: Mensaje a mostrar al usuario
    
    Returns:
        Número positivo ingresado
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("❌ Error: El valor debe ser mayor que cero.")
            else:
                return valor
        except ValueError:
            print("❌ Error: Debe ingresar un número válido.")

def main():
    """Función principal del programa."""
    print("=" * 50)
    print("   CALCULADORA DE VOLUMEN DE CILINDRO")
    print("=" * 50)
    
    continuar = 's'
    
    while continuar.lower() == 's':
        print("\n📏 Ingrese los datos del cilindro:")
        print("-" * 50)
        
        # Solicitar datos con validación
        radio = obtener_numero_positivo("Ingrese el radio del cilindro: ")
        altura = obtener_numero_positivo("Ingrese la altura del cilindro: ")
        
        # Calcular volumen
        volumen = calcular_volumen_cilindro(radio, altura)
        
        # Mostrar resultados
        print("\n" + "=" * 50)
        print("   RESULTADOS")
        print("=" * 50)
        print(f"📐 Radio:    {radio:.2f} unidades")
        print(f"📏 Altura:   {altura:.2f} unidades")
        print(f"📦 Volumen:  {volumen:.2f} unidades cúbicas")
        print("=" * 50)
        
        # Preguntar si desea continuar
        print("\n¿Desea calcular otro cilindro? (S/N): ", end="")
        continuar = input().strip()
        print()
    
    print("✅ ¡Gracias por usar el programa!")
    print("=" * 50)

if __name__ == "__main__":
    main()