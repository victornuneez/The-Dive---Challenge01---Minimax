

# Ejercicio 1
# Objetivo: Crear una función que calcule la distancia Manhattan entre dos puntos.

print("Ejercicio 1")
def distancia_manhattan(punto1, punto2):
    # Tu código aquí


    dist = abs (punto1[0] - punto2[0]) + abs (punto1[1] - punto2[1])
    return dist
    

# Pruebas:
print(distancia_manhattan((0,0), (3,4)))  # Debería dar 7
print(distancia_manhattan((1,1), (1,1)))  # Debería dar 0
print(distancia_manhattan((2,5), (7,1)))  # Debería dar 9 



# Ejercicio 2
# Objetivo: Hacer una función que diga si una posición está dentro de un tablero de 10x22.

print("Ejercicio 2")
ALTO = 10

ANCHO = 22


def posicion_valida(fila, columna):
    # Tu código aquí
    return 0 <= fila < ALTO and 0 <= columna < ANCHO


# Pruebas:
print(posicion_valida(5, 10))   # True
print(posicion_valida(-1, 5))   # False
print(posicion_valida(10, 5))   # False (recorda que va de 0 a 9)
print(posicion_valida(9, 21))   # True



# Ejercicio 3: Generar Movimientos
# Objetivo: Dada una posición, generar todas las posiciones vecinas (arriba, abajo, izq, der).
print("Ejercicio 3")
def obtener_vecinos(fila, columna):
    # Tu código aquí
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]
    vecinos = []

    for mov in movimientos:

        nueva_fila = fila + mov[0]
        
        nueva_columna = columna + mov[1]
        
        vecinos.append((nueva_fila,nueva_columna))
    
    return vecinos


       
    
  
    # Debería devolver una lista de tuplas

# Pruebas:
print(obtener_vecinos(5, 5))  # [(4,5), (6,5), (5,4), (5,6)]
print(obtener_vecinos(0, 0))  # [(-1,0), (1,0), (0,-1), (0,1)]


print("Ejercicio 4")
# Ejercicio 4: Filtrar Movimientos Válidos
# Objetivo: De una lista de posiciones, quedarse solo con las que estén dentro del tablero.


def filtrar_validos(lista_posiciones):
    # Tu código aquí
    validos = []

    for posicion in lista_posiciones:
      fila_valida = posicion[0]
      columna_valida = posicion[1]
        
    # Usar la función posicion_valida del ejercicio 2
      if posicion_valida(fila_valida,columna_valida):
          
          validos.append((fila_valida,columna_valida))


    return validos

# Pruebas:
posiciones = [(1,1), (-1,5), (15,3), (8,20), (9,21)]
print(filtrar_validos(posiciones))  # [(1,1), (8,20), (9,21)]


print("Ejercicio 5")
# Ejercicio 5: Crear Mini-Tablero (ACTUAL)
# Objetivo: Crear una matriz 5x5 llena de espacios " " y poner un "X" en el centro.

def crear_tablero_mini():
    # Tu código aquí
    tablero = []

    for fila in range(5): # cuántas filas
        fila = ["."] *5 # cuántas columnas por fila
        tablero.append(fila)
    # Devolver una lista de listas
    tablero[2][2] = "X"
    tablero[0][0] = "V"
    return tablero
    

def imprimir_tablero_mini(tablero):
    for fila in tablero:
        print(fila)
    

# Prueba:
tablero = crear_tablero_mini()
imprimir_tablero_mini(tablero)
# Debería mostrar:
#     
#     
#   X  
#     
#


# Ejercicio Extra: Matriz con For Anidado
# Objetivo: Crear una matriz 4x6 (4 filas, 6 columnas) donde cada posición tenga el número de la fila + columna.
print("Matriz")
def crear_matriz_suma():
    matriz = []

    for fila in range(4):
       filas_completas = []

       for columna in range(6):
            filas_completas.append(fila + columna)

       matriz.append(filas_completas)
    return matriz

def imprimir_matriz(matriz):
    for filas in matriz:
        print(filas)



tabla = crear_matriz_suma()
imprimir_matriz(tabla)

    
            
    

# minimax 
# Mini-Ejercicio: Minimax Básico
# Objetivo: Crear un juego simple donde dos jugadores eligen números, y implementar minimax para el segundo jugador.


