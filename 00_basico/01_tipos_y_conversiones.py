# --------------------------------------------
# Tipos de datos y conversiones en Python
# --------------------------------------------
# Tipos de básicos más comunes: int, float, str, bool.

# --------------------------------------------
# 1. Números (int, float)
# --------------------------------------------
entero = 10  # Int
decimal = 3.14  # Float
negativo = -5  # Int negativo
potencia = 2**3  # Operador de potencia

print("1. Números")
print(
    f"Entero: {entero}, Decimal: {decimal}, Negativo: {negativo}, Potencia: {potencia}"
)

# --------------------------------------------
# 2. Cadenas de texto (str)
# --------------------------------------------
texto1 = "Hola Python"
texto2 = """
Texto en varias lineas de código
"""
texto3 = "Comillas simples ' y dobles \" dentro de una cadena"
print("\n2. Cadenas de texto")
print(f"Texto1: {texto1}")
print(f"Texto2: {texto2}")
print(f"Texto3: {texto3}")
# Concatenación
saludo = texto1 + " - Bienvenido!"
print(f"Concatenación: {saludo}")

# --------------------------------------------
# 3. Booleanos (bool)
# --------------------------------------------
verdadero = True
falso = False
print("\n3. Booleanos")
print(verdadero and falso)  # Resultado: False
print(verdadero or falso)  # Resultado: True

# --------------------------------------------
# 4. Revisar el tipo de dato
# --------------------------------------------
print("\n4. Revisar tipo de dato")
print(type(entero))  # <class 'int'>
print(type(texto1))  # <class 'str'>
print(type(verdadero))  # <class 'bool'>

# --------------------------------------------
# 5. Conversiones entre tipos
# --------------------------------------------

print("\n5. Conversiones entre tipos")

x = "100"
y = int(x)
print(f"Sumar el valor string convertido a int: {y + 100}")  # Resultado: 200

decimal = 9.99
print(f"Convertir float a int: {int(decimal)}")  # Resultado: 9

# bool() convierte según el contenido:
print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("texto"))  # True
