# Apuntes de Python - el comienzo del análisis de datos

El objetivo de este repositorio es documentar los conceptos básicos y necesarios de Python antes de comenzar con el análisis de datos.

## 1. Tipos y conversiones

Python trabaja con distintos tipos de datos según la información que necesitemos representar. Además, podemos identificar y convertir estos valores cuando sea necesario.

Tipos fundamentales usados para representar números, texto y valores lógicos.

| Tipo        | Descripción                      | Ejemplo            |
| ----------- | -------------------------------- | ------------------ |
| `int`       | Número entero                    | `10`, `-5`         |
| `float`     | Número decimal                   | `3.14`, `-2.7`     |
| `str`       | Texto o caracteres               | `"Hola"`           |
| `bool`      | Valor lógico                     | `True`, `False`    |
| `dict`      | Diccionario: pares clave-valor   | `{"a": 1, "b": 2}` |
| `list`      | Lista ordenada y modificable     | `[1, 2, 3]`        |
| `tuple`     | Tupla ordenada e inmutable       | `(1, 2, 3)`        |
| `set`       | Conjunto sin elementos repetidos | `{1, 2, 3}`        |

Podemos saber el tipo de dato utilizando la función `type()`.

| Función  | Ejemplo        | Resultado       |
| -------- | -------------- | --------------- |
| `type()` | `type(10)`     | `<class 'int'>` |
|          | `type("Hola")` | `<class 'str'>` |

También, podemos transformar diferentes tipos según lo que necesitemos, por ejemplo, transformar valores de `str` a `int` para realizar operaciones aritméticas. 

| Conversión | Ejemplo         | Resultado |
| ---------- | --------------- | --------- |
| `int()`    | `int("100")`    | `100`     |
|            | `int(9.99)`     | `9`       |
| `float()`  | `float("3.14")` | `3.14`    |
| `str()`    | `str(99)`       | `"99"`    |
| `bool()`   | `bool(0)`       | `False`   |
|            | `bool(1)`       | `True`    |
|            | `bool("")`      | `False`   |
|            | `bool("texto")` | `True`    |

## 2. Operadores y comparadores

Esta tabla muestra los operadores matemáticos básicos utilizados en programación, que permiten realizar operaciones sobre números. Estos operadores incluyen la suma, resta, multiplicación, división, entre otros.

| Operador Aritmético | Expresión | Resultado        |
| ------------------- | --------- | ---------------- |
| Suma                | `a + b`   | `8 + 5 = 13`     |
| Resta               | `a - b`   | `8 - 5 = 3`      |
| Multiplicación      | `a * b`   | `8 * 5 = 40`     |
| División            | `a / b`   | `8 / 5 = 1,6`    |
| División entera     | `a // b`  | `8 // 5 = 1`     |
| Módulo              | `a % b`   | `8 % 5 = 3`      |
| Potencia            | `a ** b`  | `8 ** 5 = 32768` |

Esta tabla contiene operadores que se utilizan para comparar dos valores, retornando un valor booleano (`True` o `False`) según el resultado de la comparación.

| Comparador    | Expresión | Resultado       |
| ------------- | --------- | --------------- |
| Igualdad      | `a == b`  | `8 == 5 #False` |
| Desigualdad   | `a != b`  | `8 != 5 #True`  |
| Mayor que     | `a > b`   | `8 > 5 #True`   |
| Menor que     | `a < b`   | `8 < 5 #False`  |
| Mayor o igual | `a >= b`  | `8 >= 5 #True`  | 
| Menor o igual | `a <= b`  | `8 <= 5 #False` |

Los operadores lógicos permiten combinar expresiones booleanas, es decir, valores que son `True` o `False`. Se utilizan para tomar decisiones o realizar validaciones.

| Operador Lógico  | Resultado |
| ---------------- | --------- |
| `True and False` | `False`   |
| `True or False`  | `True`    |
| `not True`       | `False`   |

## 3. Control de flujo

Permiten tomar decisiones dentro del programa según condiciones que pueden cumplirse o no. Se basan en expresiones que se evalúan como `True` o `False`.

| Estructura | Descripción                                                      | Ejemplo        |
| ---------- | ---------------------------------------------------------------- | -------------- |
| `if`       | Ejecuta un bloque si la condición es verdadera                   | `if x > 0:`    |
| `elif`     | Evalúa otra condición si las anteriores no se cumplen            | `elif x == 0:` |
| `else`     | Se ejecuta solo si ninguno de los casos anteriores fue verdadero | `else:`        |

Podemos realizar condiciones más complejas utilizando distintos operadores.

| Operador | Significado                            | Ejemplo           | Resultado      |
| -------- | -------------------------------------- | ----------------- | -------------- |
| `and`    | Ambas condiciones deben ser verdaderas | `x > 0 and y < 5` | `True / False` |
| `or`     | Basta con que una sea verdadera        | `x > 0 or y < 5`  | `True / False` |
| `not`    | Invierte el valor lógico               | `not True`        | `False`        |

## 4. Bucles

Los bucles permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o durante un número definido de veces.

| Bucle   | Descripción                                    | Ejemplo              |
| ------- | ---------------------------------------------- | -------------------- |
| `for`   | Recorre una secuencia (lista, rango, texto...) | `for i in range(5):` |
| `while` | Se repite mientras la condición sea verdadera  | `while x < 10:`      |

Además, existen palabras clave que permiten controlar el flujo dentro del bucle:

| Palabra clave | Acción                         | Ejemplo               |
| ------------- | ------------------------------ | --------------------- |
| `break`       | Termina el bucle por completo  | `if i == 3: break`    |
| `continue`    | Salta a la siguiente iteración | `if i == 1: continue` |

## 5. Funciones

Una función es un bloque de código reutilizable que se ejecuta cuando es llamado. Permiten organizar el código y evitar repetición.

| Concepto | Descripción                             | Ejemplo             |
| -------- | --------------------------------------- | ------------------- |
| `def`    | Palabra clave para definir una función  | `def mi_funcion():` |
| `return` | Devuelve un valor y finaliza la función | `return x * 2`      |

A veces no sabemos cuántos argumentos vamos a recibir. Para eso existen:

| Tipo de parámetro | Uso          | Descripción                          | Ejemplo                  |
| ----------------- | ------------ | ------------------------------------ | ------------------------ |
| `*args`           | Posicionales | Recibe cualquier cantidad de valores | `def funcion(*args):`    |
| `**kwargs`        | Nombrados    | Recibe valores por clave-valor       | `def funcion(**kwargs):` |

## 6. Strings

Representan texto dentro del programa y permiten manipularlo de muchas maneras: concatenar, buscar, dividir, reemplazar, etc.

Existen diferentes formas de escribir strings en el código, ya sea con `" "`, `' '`, o `""" """`.

| Forma                     | Ejemplo                        |
| ------------------------- | ------------------------------ |
| Comillas simples o dobles | `"Hola"` — `'Python'`          |
| Multilínea                | `"""Texto en varias líneas"""` |

Además, podemos concatenar o multiplicar strings.

| Acción     | Ejemplo              | Resultado        |
| ---------- | -------------------- | ---------------- |
| Concatenar | `"Hola" + " Python"` | `"Hola Python"`  |
| Repetir    | `"Hola" * 3`         | `"HolaHolaHola"` |

Podemos formatear el texto con estos dos métodos, aunque el recomendado es el primero ya que es más legible para documentar.

| Método      | Ejemplo                            |
| ----------- | ---------------------------------- |
| f-string    | `f"Mi nombre es {nombre}"`         |
| `.format()` | `"Mi nombre es {}".format(nombre)` |

Existen diferentes métodos para los strings, que nos permitirá modificar o buscar cuando lo necesitemos.

| Método           | Descripción                     | Ejemplo                              | Resultado            |
| ---------------- | ------------------------------- | ------------------------------------ | -------------------- |
| `.upper()`       | Todo en mayúsculas              | `"python".upper()`                   | `"PYTHON"`           |
| `.lower()`       | Todo en minúsculas              | `"Python".lower()`                   | `"python"`           |
| `.title()`       | Capitaliza cada palabra         | `"python es genial".title()`         | `"Python Es Genial"` |
| `.replace(a, b)` | Reemplaza texto                 | `"hola mundo".replace("hola", "hi")` | `"hi mundo"`         |
| `.split()`       | Convierte en lista por espacios | `"a b c".split()`                    | `['a','b','c']`      |
| `.find()`        | Devuelve índice encontrado o -1 | `"python".find("o")`                 | `4`                  |
| `.partition()`   | Divide en 3 partes              | `"a-b".partition("-")`               | `('a','-','b')`      |

También existen maneras de saber la longitud de nuestro string o cortar en caso de que necesitemos solamente una parte, esto será útil más adelante al trabajar con listas.

| Acción         | Ejemplo         | Resultado |
| -------------- | --------------- | --------- |
| Longitud       | `len("Python")` | `6`       |
| Índice inicial | `"Python"[0]`   | `"P"`     |
| Último índice  | `"Python"[-1]`  | `"n"`     |
| Slicing        | `"Python"[0:3]` | `"Pyt"`   |
| Salto          | `"Python"[::2]` | `"Pto"`   |

> [!NOTE] 
> Los strings son **inmutables**: no se puede cambiar un carácter directamente, solo crear una nueva cadena modificada.

## 7. Listas

Una lista es una colección **ordenada y mutable** que puede almacenar cualquier tipo de dato.

##### 7.1 Crear listas

| Tipo de Listas          | Ejemplo                              | Resultado                        |
| ----------------------- | ------------------------------------ | -------------------------------  |
| lista vacía             | `l = []` — `l = list()`              | `[]`                             |
| Lista de enteros        | `l = [1, 2, 3, 4, 5]`                | `[1, 2, 3, 4, 5]`                |
| Lista de strings        | `l = ['Manzana', 'Pera', 'Naranja']` | `['Manzana', 'Pera', 'Naranja']` |
| Lista mixta             | `l = [1, "a", True, 3.5]`            | `[1, "a", True, 3.5]`            |
| Lista anidada           | `l = [1, 2, [3, 4], 5]`              | `[1, 2, [3, 4], 5]`              |
| Convertir rango a lista | `l = list(range(1,6))`               | `[1, 2, 3, 4, 5]`                |
| Compresión de listas    | `l = [x**2 for x in range(1,5)]`     | `[1, 4, 9, 16]`                  |

##### 7.2 Indexar y acceder a elementos

Permite acceder a valores dentro de una lista. Para la siguiente tabla usaremos `[1, 2, [3, 4], 5]`.

| Acción                | Ejemplo       | Resultado |
| --------------------- | ------------- | --------- |
| Primer elemento       | `lista[0]`    | `1`       |
| Segundo elemento      | `lista[1]`    | `2`       |
| Último elemento       | `lista[-1]`   | `5`       |
| Acceder lista interna | `lista[2][0]` | `3`       |


##### 7.3 Slicing (cortar listas)

Permite obtener sublistas, sin modificar la original. 
La sintaxis de cortar listas es: `lista[inicio: fin: paso]`.
Para la siguiente tabla usaremos `[10, 20, 30, 40, 50, 60]`.

| Descripción        | Ejemplo         | Resultado                  |
| ------------------ | --------------- | -------------------------- |
| Primeros elementos | `numeros[:3]`   | `[10, 20, 30]`             |
| Rango específico   | `numeros[2:5]`  | `[30, 40, 50]`             |
| Cada 2 elementos   | `numeros[::2]`  | `[10, 30, 50]`             |
| Lista invertida    | `numeros[::-1]` | `[60, 50, 40, 30, 20, 10]` |

##### 7.4 Modificar elementos

| Tipo de modificación  | Ejemplo                          | Resultado                     |
| --------------------- | -------------------------------- | ----------------------------- |
| Cambiar un valor      | `numeros[0] = 100`               | Reemplaza el primer elemento  |
| Cambiar valor anidado | `mixta[2][1] = "modificado"`     | Edita dentro de una sublista  |
| Reemplazar rango      | `numeros[1:3] = [200, 300, 400]` | Ajusta tamaño automáticamente |

##### 7.5 Operaciones con listas

Para la siguiente tabla usaremos la `lista_1 = [1, 2]` y `lista_2 = [3, 4]`.
| Operación            | Ejemplo              | Resultado      |
| -------------------- | -------------------- | -------------- |
| Concatenar           | `lista_1 + lista_2`  | `[1, 2, 3, 4]` |
| Repetir              | `lista_1 * 2`        | `[1, 2, 1 ,2]` |
| Verificar existencia | `1 in lista_1`       | `True`         |
| Verificar ausencia   | `1 not in lista_1`   | `False`        |

##### 7.6 Métodos útiles

| Método                | Acción                     | Ejemplo                    | Resultado            |
| --------------------- | -------------------------- | -------------------------- | -------------------- |
| `.append()`           | Agrega al final            | `lista.append("Nuevo")`    | Añadido al final     |
| `.insert()`           | Inserta en índice          | `lista.insert(2, "Fruta")` | Desplaza el resto    |
| `.remove()`           | Borra primera coincidencia | `lista.remove("Manzana")`  | Elimina ese valor    |
| `.pop()`              | Elimina por índice o fin   | `lista.pop(2)`             | Retorna el eliminado |
| `.clear()`            | Vacía la lista             | `lista.clear()`            | `[]`                 |
| `.index()`            | Ubica un elemento          | `lista.index("Naranja")`   | Devuelve índice      |
| `.count()`            | Cuenta repeticiones        | `lista.count("Manzana")`   | Cantidad encontrada  |
| `.sort()`             | Ordena (ascendente)        | `lista.sort()`             | Lista ordenada       |
| `.sort(reverse=True)` | Ordena descendente         | `lista.sort(reverse=True)` | Orden inverso        |

> [!TIP] 
> `sort()` es un método que modifica la lista. Para obtener una nueva lista ordenada, usa la función `sorted(lista)`.

> [!NOTE] 
> Las listas son **mutables** -> puedes modificar elementos sin crear una nueva lista.

## 8. Diccionarios

Un diccionario es una estructura no ordenada que almacena datos en pares `clave : valor`.
Las claves deben ser únicas y normalmente son strings o números.

##### 8.1 Crear diccionarios

| Acción                | Ejemplo                         | Resultado             |
| --------------------- | ------------------------------- | --------------------- |
| Diccionario vacío     | `{}` — `dict()`                 | `{}`                  |
| Con valores iniciales | `{"nombre": "Ana", "edad": 25}` | Diccionario con datos |
| Acceder a un valor    | `personas["nombre"]`            | `"Ana"`               |

##### 8.2 Modificar diccionarios

| Tipo de operación    | Ejemplo                               | Resultado                   |
| -------------------- | ------------------------------------- | --------------------------- |
| Modificar valor      | `personas["edad"] = 26`               | Cambia el valor de la clave |
| Agregar clave-valor  | `personas["profesion"] = "Ingeniera"` | Se añade al diccionario     |
| Eliminar clave-valor | `del personas["ciudad"]`              | Remueve esa entrada         |

##### 8.3 Métodos útiles

| Método      | Acción                     | Ejemplo                | Resultado                  |
| ----------- | -------------------------- | ---------------------- | -------------------------- |
| `.keys()`   | Lista de claves            | `personas.keys()`      | dict_keys([...])           |
| `.values()` | Lista de valores           | `personas.values()`    | dict_values([...])         |
| `.items()`  | Claves y valores en tuplas | `personas.items()`     | dict_items([...])          |
| `.get()`    | Obtener valor seguro       | `personas.get("edad")` | Devuelve el valor o `None` |
| `.pop()`    | Eliminar y devolver valor  | `personas.pop("edad")` | Borra la clave `"edad"`    |

##### 8.4 Iterar diccionarios

| Iteración            | Ejemplo                                 | Resultado                |
| -------------------- | --------------------------------------- | ------------------------ |
| Recorrer claves      | `for clave in personas:`                | Muestra claves           |
| Recorrer clave-valor | `for clave, valor in personas.items():` | Muestra claves y valores |

> [!NOTE]
> Para un ejemplo más detallado, revisar el archivo `08_diccionarios.ipynb`

## 9. Tuplas

Las tuplas son muy similares a las listas: permiten almacenar múltiples elementos.
La gran diferencia es que son inmutables, es decir, no se pueden modificar una vez creadas.

> [!NOTE]
> La inmutabilidad permite que las tuplas puedan usarse como claves en diccionarios y elementos de sets, cosa que no ocurre con las listas.

| Característica               | Lista (`list`)    | Tupla (`tuple`)                           |
| ---------------------------- | ----------------- | ----------------------------------------- |
| Mutable                      | Sí                | No                                        |
| Sintaxis                     | `[]`              | `()`                                      |
| ¿Puede ser clave en un dict? | No                | Sí                                        |
| Uso típico                   | Datos que cambian | Datos fijos, coordenadas, configuraciones |

##### 9.1 ¿Para qué sirven?
- Cuando necesitas asegurar que los datos no cambien
- Para representar coordenadas o pares ordenados
- Cuando requieres claves en diccionarios que representen combinaciones de datos
- Para optimizar memoria (las tuplas son un poco más ligeras)



## 10. Sets

Los sets son colecciones desordenadas de elementos únicos y mutables, pero solo pueden contener elementos inmutables (por ejemplo: números, strings, tuplas).

##### 10.1 Crear un Set

Al crear un set se debe especificar el contenido
```
variable = set(['foo', 'bar', 'baz', 'foo'])
print(variable)  # {'foo', 'bar', 'baz'} -> 'foo' no se repite
```
También se puede usar llaves directamente:
```
set_1 = {1, 2, 3}
```
##### 10.2 Métodos comunes
Para la siguiente tabla, usaremos los siguientes sets:
```
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6 ,7, 8, 9}
```
| Método                    | Ejemplo                             | Resultado                      |
| ------------------------- | ----------------------------------- | ------------------------------ |
| `.intersection()`         | `set_1.intersection(set_2)`         | `{4, 5, 6}`                    |
| `.union()`                | `set_1.union(set_2)`                | `{1, 2, 3, 4, 5, 6, 7, 8, 9}`  |
| `.difference()`           | `set_1.difference(set_2)`           | `{1, 2, 3}`                    |
| `.symmetric_difference()` | `set_1.symmetric_difference(set_2)` | `{1, 2, 3, 7, 8, 9}`           |
| `.add()`                  | `set_1.add(7)`                      | `{1, 2, 3, 4, 5, 6, 7}`        |

## Ejercicios resueltos

En el archivo `00_Ejercicios.py` se encontrarán ejercicios resueltos sobre los temas 1 al 6.
En el archivo `00_ejercicios.ipynb` se encontrarán ejercicios resueltos sobre los temas 7 al 10.

## Siguiente paso: Numpy y Pandas para análisis de datos

Para continuar con los apuntes, se dejarán enlazados los siguientes repositorios referente a Numpy y Pandas sobre manipulación, transformación y limpieza datos.

- [Apuntes de NumPy](https://github.com/CrisKaphiri/Apuntes_de_Numpy)
- [Pandas para el análisis de datos - En proceso]()
