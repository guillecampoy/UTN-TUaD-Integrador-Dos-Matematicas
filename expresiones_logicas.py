# Ejercicio 5
# Redactar al menos dos expresiones lógicas en lenguaje natural,
# que puedan luego implementarse en Python y escribir en la documentación
# que van a presentar cual seria el resultado con los conjuntos que tienen.

# Listado de DNI's
# 38095321
# 35109356
# 38537195
# 35051272
# 30485503

# Conjuntos de dígitos 
A = {1, 2, 3, 5, 8, 9, 0}
B = {0, 1, 3, 5, 6, 9, 7}
C = {1, 3, 5, 7, 8, 9}
D = {0, 1, 2, 3, 5, 7}
E = {0, 3, 4, 5, 8}

# Expresión lógica 1: Lenguaje natural: "El conjunto A y el conjunto B tienen al menos un dígito en común."
# Resultado: {0, 1, 3, 5, 9}
resultado_1 = A.intersection(B)
print(f"Expresión lógica 1: {resultado_1}")

# Expresión lógica 2: Lenguaje natural: "El conjunto C tiene al menos un dígito en común con el conjunto D."
# Resultado: {1, 3, 5, 7}
resultado_2 = C.intersection(D)
print(f"Expresión lógica 2: {resultado_2}")

# Expresión lógica 3: Lenguaje natural: "El conjunto E no tiene dígitos en común con el conjunto A."
# Resultado: {0, 3, 5, 8}
resultado_3 = E.intersection(A)
print(f"Expresión lógica 3: {resultado_3}")

# Expresión lógica 4: Lenguaje natural: "El conjunto B tiene al menos un dígito que no está en el conjunto C."
# Resultado: {0, 6}
resultado_4 = B.difference(C)
print(f"Expresión lógica 4: {resultado_4}")