# --------------------------------------------
# 1. Definir funciones
# -------------------------------------------
def duplicar(numero):  # Definir una función con parametros
    return numero * 2  # Devuelve el doble de un número


# Llamada a la función
resultado = duplicar(10)
print("El doble de 10 es:", resultado)


# --------------------------------------------
# 2. Funciones con *args
# --------------------------------------------
def suma_todos(*numeros):  # Acepta múltiples argumentos
    total = 0  # Inicializa la suma
    for num in numeros:
        total = total + num  # Suma cada número al total
    return total


resultado_suma = suma_todos(10, 20, 30, 40)
print("La suma de todos los números es:", resultado_suma)


# --------------------------------------------
# 3. Funciones con **kwargs
# --------------------------------------------
def mostrar_info(**informacion):
    for clave, valor in informacion.items():
        print(f"{clave} : {valor}")
    print(informacion)


mostrar_info(nombre="Nombre", edad=28, ciudad="Ciudad")
