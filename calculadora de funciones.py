import math

# Solicitar el número al usuario
numer = float(input("El numero que quiere operar es: "))

# Calcular las funciones matemáticas
seno = math.sin(numer)
coseno = math.cos(numer)
tangente = math.tan(numer)
rai = math.sqrt(numer)
logaritmoNatural = math.log(numer)
logaritmo10 = math.log10(numer)

# Mostrar los resultados
print(f"Del numero: {numer}")
print(f"Su seno es: {seno}")
print(f"Su coseno es: {coseno}")
print(f"Su tangente es: {tangente}")
print(f"Su raiz es: {rai}")
print(f"Su logaritmo natural es: {logaritmoNatural}")
print(f"Su logaritmo es: {logaritmo10}")