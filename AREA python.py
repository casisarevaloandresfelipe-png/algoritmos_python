def obtener_dimension(nombre_dimension):
    """Solicita y valida una dimensión del rectángulo"""
    while True:
        try:
            valor = float(input(f"Ingrese la {nombre_dimension} del rectángulo (cm): "))
            if valor <= 0:
                print(f"❌ Error: La {nombre_dimension} debe ser mayor que cero\n")
            else:
                return valor
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido\n")

def calcular_area_perimetro():
    """Calcula el área y perímetro de un rectángulo"""
    # Encabezado
    print("╔═════════════════════════════════════════════════════╗")
    print("║  CÁLCULO DE ÁREA Y PERÍMETRO DE UN RECTÁNGULO      ║")
    print("╚═════════════════════════════════════════════════════╝")
    print()
    
    # Solicitar y validar datos
    base = obtener_dimension("base")
    altura = obtener_dimension("altura")
    
    # Calcular área y perímetro
    area = base * altura
    perimetro = 2 * (base + altura)
    
    # Mostrar resultados
    print()
    print("╔═════════════════════════════════════════════════════╗")
    print("║                    RESULTADOS                       ║")
    print("╚═════════════════════════════════════════════════════╝")
    print(f"📏 Base:        {base:.2f} cm")
    print(f"📏 Altura:      {altura:.2f} cm")
    print(f"📐 Área:        {area:.2f} cm²")
    print(f"📏 Perímetro:   {perimetro:.2f} cm")
    print()
    print("¡Cálculo completado exitosamente! ✓")

# Ejecutar el programa
if _name_ == "_main_":
    calcular_area_perimetro()