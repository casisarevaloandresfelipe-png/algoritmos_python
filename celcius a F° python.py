def celsius_a_fahrenheit(celsius):
    """
    Convierte temperatura de Celsius a Fahrenheit
    Fórmula: F = (9/5) × C + 32
    """
    return (9/5) * celsius + 32


def obtener_info_temperatura(fahrenheit):
    """
    Proporciona información contextual sobre la temperatura
    """
    if fahrenheit <= 32:
        return "❄️  Punto de congelación o menor"
    elif fahrenheit >= 212:
        return "♨️  Punto de ebullición o mayor"
    elif 98.6 <= fahrenheit <= 99.6:
        return "🌡️  Temperatura corporal normal"
    elif fahrenheit < 32:
        return "🥶 Muy frío"
    elif fahrenheit > 86:
        return "🔥 Caluroso"
    else:
        return "🌤️  Temperatura ambiente agradable"


def mostrar_encabezado():
    """Muestra el encabezado del programa"""
    print("\n" + "="*40)
    print("  CONVERSIÓN DE TEMPERATURA")
    print("  Celsius a Fahrenheit")
    print("="*40)


def version_basica():
    """Versión básica del conversor"""
    mostrar_encabezado()
    
    # Solicitar temperatura en Celsius
    celsius = float(input("\nIngrese la temperatura en °C: "))
    
    # Calcular Fahrenheit
    fahrenheit = celsius_a_fahrenheit(celsius)
    
    # Mostrar resultado
    print("\n" + "="*40)
    print("         RESULTADO")
    print("="*40)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
    print("="*40)


def version_completa():
    """Versión completa con ciclo y validaciones"""
    print("\n" + "╔" + "="*38 + "╗")
    print("║  CONVERSIÓN DE TEMPERATURA           ║")
    print("║  Celsius a Fahrenheit                ║")
    print("╚" + "="*38 + "╝")
    
    while True:
        try:
            # Solicitar temperatura
            print("\n" + "-"*40)
            celsius = float(input("Ingrese temperatura en °C: "))
            
            # Calcular Fahrenheit
            fahrenheit = celsius_a_fahrenheit(celsius)
            
            # Mostrar resultado
            print("\n" + "╔" + "="*38 + "╗")
            print("║         RESULTADO                    ║")
            print("╚" + "="*38 + "╝")
            print(f"  {celsius}°C = {fahrenheit:.2f}°F")
            
            # Información adicional
            info = obtener_info_temperatura(fahrenheit)
            print(f"\n  {info}")
            
            # Preguntar si desea continuar
            print("\n" + "-"*40)
            continuar = input("¿Realizar otra conversión? (S/N): ").strip().upper()
            
            if continuar != 'S':
                print("\n¡Gracias por usar el conversor! 👋\n")
                break
                
        except ValueError:
            print("\n⚠️  Error: Por favor ingrese un número válido")
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario! 👋\n")
            break


def menu_principal():
    """Menú con conversión bidireccional"""
    while True:
        print("\n" + "╔" + "="*38 + "╗")
        print("║  CONVERSOR DE TEMPERATURA            ║")
        print("╚" + "="*38 + "╝")
        print("\n1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        print("3. Salir")
        
        try:
            opcion = input("\nSeleccione una opción (1-3): ").strip()
            
            if opcion == '1':
                celsius = float(input("\nIngrese temperatura en °C: "))
                fahrenheit = celsius_a_fahrenheit(celsius)
                print(f"\n✓ {celsius}°C = {fahrenheit:.2f}°F")
                print(f"  {obtener_info_temperatura(fahrenheit)}")
                
            elif opcion == '2':
                fahrenheit = float(input("\nIngrese temperatura en °F: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"\n✓ {fahrenheit}°F = {celsius:.2f}°C")
                
            elif opcion == '3':
                print("\n¡Hasta luego! 👋\n")
                break
            else:
                print("\n⚠️  Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("\n⚠️  Error: Ingrese un número válido")
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido! 👋\n")
            break


# Programa principal
if _name_ == "_main_":
    print("\n¿Qué versión desea ejecutar?")
    print("1. Versión básica (una conversión)")
    print("2. Versión completa (múltiples conversiones)")
    print("3. Menú con conversión bidireccional")
    
    try:
        seleccion = input("\nSeleccione (1-3): ").strip()
        
        if seleccion == '1':
            version_basica()
        elif seleccion == '2':
            version_completa()
        elif seleccion == '3':
            menu_principal()
        else:
            print("\nOpción no válida. Ejecutando versión completa...\n")
            version_completa()
            
    except KeyboardInterrupt:
        print("\n\n¡Programa cancelado! 👋\n")