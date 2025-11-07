def calcular_intereses():
    """
    Calcula los intereses ganados de una inversión,
    los impuestos aplicables y el valor neto a recibir.
    """
    print("=" * 50)
    print("    CALCULADORA DE INTERESES GANADOS")
    print("=" * 50)
    print()
    
    # Entrada de datos con validación
    while True:
        try:
            cantidad = float(input("Ingrese la cantidad de dinero invertida: $"))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido")
    
    while True:
        try:
            porcentaje_intereses = float(input("Ingrese el porcentaje de interés anual (%): "))
            if porcentaje_intereses <= 0:
                print("Error: El porcentaje debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido")
    
    while True:
        try:
            periodo = float(input("Ingrese el periodo en días: "))
            if periodo <= 0:
                print("Error: El periodo debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número válido")
    
    # Cálculos
    # Fórmula de interés simple con año comercial de 360 días
    valor_intereses = (cantidad * (porcentaje_intereses / 100) * periodo) / 360
    
    # Impuesto del 7% sobre los intereses
    impuesto_intereses = valor_intereses * 0.07
    
    # Valor neto a recibir
    valor_neto_pagar = cantidad + valor_intereses - impuesto_intereses
    
    # Mostrar resultados
    print()
    print("=" * 50)
    print("              RESULTADOS")
    print("=" * 50)
    print(f"Capital invertido:        ${cantidad:,.2f}")
    print(f"Intereses ganados:        ${valor_intereses:,.2f}")
    print(f"Impuestos (7%):           ${impuesto_intereses:,.2f}")
    print("-" * 50)
    print(f"Valor neto a recibir:     ${valor_neto_pagar:,.2f}")
    print("=" * 50)


# Ejecutar el programa
if __name__ == "__main__":
    calcular_intereses()
    
    # Opción para calcular nuevamente
    while True:
        respuesta = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if respuesta == 's':
            print("\n")
            calcular_intereses()
        elif respuesta == 'n':
            print("\n¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción no válida. Ingrese 's' para sí o 'n' para no.")