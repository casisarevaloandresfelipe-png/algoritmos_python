def convertir_centimetros():
    """
    Convierte centímetros a yardas, metros, pies y pulgadas
    """
    print("=== CONVERSIÓN DE CENTÍMETROS ===")
    print()
    
    # Solicitar el valor en centímetros con validación
    while True:
        try:
            centimetros = float(input("Ingrese el valor en centímetros: "))
            
            if centimetros < 0:
                print("Error: El valor debe ser positivo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido.")
    
    # Realizar las conversiones
    # 1 metro = 100 centímetros
    metros = centimetros / 100
    
    # 1 yarda = 91.44 centímetros
    yardas = centimetros / 91.44
    
    # 1 pie = 30.48 centímetros
    pies = centimetros / 30.48
    
    # 1 pulgada = 2.54 centímetros
    pulgadas = centimetros / 2.54
    
    # Mostrar los resultados
    print()
    print("=== RESULTADOS DE LA CONVERSIÓN ===")
    print(f"{centimetros} cm equivalen a:")
    print(f"Metros:   {metros:.4f} m")
    print(f"Yardas:   {yardas:.4f} yd")
    print(f"Pies:     {pies:.4f} ft")
    print(f"Pulgadas: {pulgadas:.4f} in")
    print()


def main():
    """
    Función principal con opción de repetir conversiones
    """
    while True:
        convertir_centimetros()
        
        respuesta = input("¿Desea realizar otra conversión? (S/N): ").strip().upper()
        
        if respuesta != 'S':
            print("¡Hasta luego!")
            break
        print()


# Ejecutar el programa
if __name__ == "_main_":
    main()