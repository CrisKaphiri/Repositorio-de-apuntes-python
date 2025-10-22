# --------------------------------------------
# 1. Bucle for
# --------------------------------------------
print("Bucle for:")

for i in range(10):
    # imprime el valor de i
    print(i)

# --------------------------------------------
# 2. Bucle while
# --------------------------------------------
print("\nBucle while:")

contador = 0  # inicializa el contador
while contador < 5:  # condición
    # imprime contador
    print(contador)
    contador += 1  # incrementa el contador

# --------------------------------------------
# 3. Bucles anidados
# --------------------------------------------
print("\nBucles anidados:")

for i in range(3):
    for j in range(3):
        # imprime i y j
        print("i:", i, "j:", j)

# --------------------------------------------
# 4. Uso de break y continue
# --------------------------------------------
print("\nBreak y continue:")

for i in range(5):
    if i == 4:
        # salir del bucle
        break
    if i == 1:
        # saltar esta iteración
        continue
    print(i)
