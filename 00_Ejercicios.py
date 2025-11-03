# --------------------------------------------
# Ejercicios para foltalecer los apuntes
# --------------------------------------------

# --------------------------------------------
# 1.Tipos de datos y conversiones
# --------------------------------------------

# Declara una variable "edad" como string "25" y conviertela en entero. Luego suma y muestra el resultado
edad = "25"
print(int(edad) + 5)

# Crea una variable "precio" como float "19.99" y conviertela en string para cooncatenarla con "El precio es: "
precio = 19.99
print("El precio es: " + str(precio))

# --------------------------------------------
# 2. Operadores y comparadores
# --------------------------------------------

# Compara dos números y muestra si el primero es mayor, menor o igual al segundo.
numero_uno = 10
numero_dos = 20

if numero_uno > numero_dos:
    print("El primer número es mayor")
elif numero_uno < numero_dos:
    print("El primer numero es menor")
else:
    print("Los números son iguales")

# Evalúa si un número es par y mayor que 10 usando operadores lógicos.
numero = 20
if numero % 2 == 0:
    if numero > 10:
        print("El número es par y mayor que 10")
# --------------------------------------------
# 3. Control y flujo
# --------------------------------------------

# Escribe un condicional que verifique si un número está en el rango 1-100: si es menor a 50 imprime "bajo", si está entre 50 y 80 "medio", y si es mayor "alto".
numero = 70
if numero > 0 and numero < 50:
    print("bajo")
elif numero >= 50 and numero <= 80:
    print("medio")
elif numero > 80 and numero <= 100:
    print("alto")
else:
    print("número fuera de rango 1 - 100")

# Crea un mini menú: pide al usuario un número del 1 al 3 y muestra "opción A", "opción B", o "opción C" según corresponda.
opcion = int(input("Ingrese la opción 1, 2 o 3: "))
if opcion == 1:
    print("Opcion A")
elif opcion == 2:
    print("Opcion B")
elif opcion == 3:
    print("Opcion C")
else:
    print("Opcion no valida")

# --------------------------------------------
# 4. Bucles
# --------------------------------------------

# Imprime los números impares entre 0 y 20 usando for.
for i in range(21):
    if i % 2 != 0:
        print(i)

# Pide un número n al usuario y usa un while para imprimir todos los números de 1 a n.
n = int(input("Ingresa un numero: "))
contador = 1
while contador <= n:
    print(contador)
    contador += 1

# Crea un bucle anidado que genere una tabla de multiplicar del 1 al 5 (filas y columnas).
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print("\n")

# --------------------------------------------
# 5. Funciones
# --------------------------------------------


# Crea una función que reciba una lista de números y devuelva la suma de todos los elementos.
def sumar(numeros):
    total = 0
    for num in numeros:
        total += num
    return total


# Escribe una función que reciba cualquier cantidad de argumentos *args y devuelva el máximo.
def maximo(*numeros):
    mayor = None
    for num in numeros:
        if (mayor is None) or (num > mayor):
            mayor = num
    return mayor


# Escribe una función que reciba palabras como **kwargs y las imprima en formato "clave: valor".
def imprimir(**diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")


# --------------------------------------------
# 6. Strings
# --------------------------------------------

# Pide al usuario una frase y cuenta cuántas veces aparece la letra "a".
frase = input("Ingresa una palabra: ").lower()
contador = frase.count("a")
print("La letra aparece:", contador, "veces.")

# Convierte la frase en mayúsculas, reemplaza espacios por guiones y muestra el resultado.
frase_mayus = frase.upper()
frase_mayus = frase_mayus.replace(" ", "-")
print(frase_mayus)

# Separa la frase en palabras usando .split() y muestra cada palabra en una línea.
lista_mayus = frase_mayus.split("-")
for palabra in lista_mayus:
    print(palabra, end=" ")
