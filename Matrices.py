# EJERCICIO 1: Matriz de ceros
# Completa el código donde veas los comentarios # TODO

print("=== EJERCICIO 1: Matriz de ceros ===")
# Genera una matriz de 3x4 llena de ceros

filas = 5
columnas = 5


# TODO: Crear la matriz usando list comprehension
# Pista: [[valor for j in range(columnas)] for i in range(filas)]
matriz_ceros = [["." for j in range(columnas)] for i in range(filas)]

# TODO: Imprimir la matriz
# Pista: usa un bucle for para cada fila
# Tu código aquí
#for elemento in matriz_ceros:

matriz_ceros[0][0] = "G"
matriz_ceros[4][4] = "R"

for elemento in matriz_ceros:
    print((elemento))


print("\n¡Completa este ejercicio y avísame para darte el siguiente! 🚀")
print()


matriz = []
contador = 1

for a in range(4):

    fila = []

    for b in range(3): 
        fila.append(contador)
        contador += 1

    matriz.append(fila)
for elemento in matriz:
    print(elemento)


# EJERCICIO 1: Tablero básico con personajes
# Similar a lo que te pidieron en tu review

print("=== EJERCICIO 1: Tablero básico con personajes ===")
# Crear matriz 5x5 con personajes en esquinas opuestas

filas = 5
columnas = 5

# TODO: Crear matriz 5x5 llena de puntos '.'
tablero = [["." for c in range(5)] for f in range(5)]



# TODO: Colocar personajes en esquinas opuestas
# Gato '🐱' en esquina superior izquierda (0,0)
# Ratón '🐭' en esquina inferior derecha (4,4)
# Tu código aquí
gato = "🐱"
raton = "🐭"

tablero[0][0] = gato
tablero[4][4] = raton

for en_filas in tablero:

    print(en_filas)
# TODO: Imprimir el tablero fila por fila
# Tu código aquí

print("\n¡Completa este ejercicio y avísame para darte el siguiente! 🎮")