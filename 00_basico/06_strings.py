# --------------------------------------------
# 1. Crear cadenas de texto
# --------------------------------------------

print("Cadenas de texto:")

texto1 = "Hola"
texto2 = "Python"
texto3 = """Texto en 
varias líneas"""

print(texto1)
print(texto2)
print(texto3)

# --------------------------------------------
# 2. Concatenar y repetir
# --------------------------------------------
print("\nConcatenar y repetir:")

saludo = texto1 + " " + texto2
print(saludo)
eco = texto1 * 3
print(eco)


# --------------------------------------------
# 3. Formateo de cadenas
# --------------------------------------------
print("\nFormateo de cadenas:")

nombre = "Nombre asignado"
edad = 28
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))

# --------------------------------------------
# 4. Métodos de strings
# --------------------------------------------
print("\nMétodos de strings:")

texto = "python es divertido"
print(texto.upper())  # mayúsculas = PYTHON ES DIVERTIDO
print(texto.lower())  # minúsculas = python es divertido
print(texto.title())  # primera letra en mayúscula = Python Es Divertido
print(texto.replace("divertido", "genial"))  # Reemplazar = python es genial
print(texto.split())  # Convierte en una lista = ['python', 'es', 'divertido']
print(
    texto.find("es")
)  # Devuelve el indide donde comienza la palabra = 7 ('e' en índice 7)
print(
    texto.partition("es")
)  # Divide en una tupla en partes = ('python', 'es', 'divertido')

# --------------------------------------------
# 5. Longitud de una cadena
# --------------------------------------------
print("\nLongitud de una cadena:")

texto = "python es divertido"
longitud = len(texto)
print(f"La longitud de la cadena es: {longitud}")  # Resultado: 19

# --------------------------------------------
# 6. Acceder a caracteres
# --------------------------------------------
print("\nAcceder a caracteres:")

texto = "python es divertido"
primer_caracter = texto[0]
ultimo_caracter = texto[-1]
print(f"Primer carácter: {primer_caracter}")  # Resultado: 'p'
print(f"Último carácter: {ultimo_caracter}")  # Resultado: 'o'
# Subcadena
subcadena = texto[0:6]
print(f"Subcadena (0-6): {subcadena}")  # Resultado: 'python'
# Subcadena desde el índice 7 hasta el final
subcadena_final = texto[7:]
print(f"Subcadena (7-fin): {subcadena_final}")  # Resultado: 'es divertido'
# Subcadena con paso
subcadena_paso = texto[0:19:2]
print(f"Subcadena con paso 2: {subcadena_paso}")  # Resultado: 'pto s ivrt'
# --------------------------------------------
