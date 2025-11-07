import math
#Declaración de variables
cateto1 = 0.0
cateto2 = 0.0
hipotenusa = 0.0
#Solicitar los catetos al usuario
print("=== CÁLCULO DE LA HIPOTENUSA ===")
print("Teorema de Pitágoras")
print("")
print("Ingrese la longitud del primer cateto:")
cateto1 = float(input())
print("Ingrese la longitud del segundo cateto:")
cateto2 = float(input())
#Calcular la hipotenusa
#Fórmula: hipotenusa = √(cateto1² + cateto2²)
hipotenusa = math.sqrt((cateto1)**2+((cateto2)**2))
#Mostrar resultados
print("")
print("=== RESULTADO ===")
print("Cateto 1:", cateto1)
print("Cateto 2:", cateto2)
print("Hipotenusa:", hipotenusa)