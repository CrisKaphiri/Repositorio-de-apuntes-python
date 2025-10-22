# --------------------------------------------
# Control de flujo: if, elif, else
# --------------------------------------------

# --------------------------------------------
# 1. Condicional simple
# --------------------------------------------
numero = 10
if numero > 0:
    print("El número es positivo")

# --------------------------------------------
# 2. Condicional con else
# --------------------------------------------
if numero > 0:
    print("Es positivo")
else:
    print("Es negativo o cero")

# --------------------------------------------
# 3. Condicional con elif
# --------------------------------------------
nota = 70
if nota == 70:
    print("Excelente")
elif nota < 70 and nota >= 40:
    print("Bueno")
else:
    print("Insuficiente")

# --------------------------------------------
# 4. Operadores lógicos combinados
# --------------------------------------------
edad = 20
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

# --------------------------------------------
# 5. Condicional anidado
# --------------------------------------------
temperatura = 27
soleado = True
if temperatura > 25:
    if soleado:
        print("Hace calor y está soleado")
    else:
        print("Hace calor pero está nublado")
else:
    print("No hace calor")
