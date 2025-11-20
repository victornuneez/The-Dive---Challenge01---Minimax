
# Para limpiar la pantalla en cada turno del juego
import os 
 
# Tablero del juego: cada cadena es una fila.
# pared = '#'  camino = ' '  salida = 🚪
TABLERO = [ 
"######################",
"#🚪                   #",
"#    #           #   #",
"#                    #",
"#          #         #",
"#          #         #",
"#                    #",
"#    #           #   #",
"#                    #",
"######################",
]

# AHORA VAMOS A CREAR DOS VARIABLES PARA ALMACENAR EL VALOR DEL ALTO Y ANCHO.

# Altura del tablero
ALTO = len(TABLERO)    
                       

# Ancho del tablero
ANCHO = len(TABLERO[0]) 

# Posiciones iniciales (fila, columna)
raton = (6,19)        
gato = (1,3)         

# El primer número de la tupla (fila, columna) te dice qué tan arriba o abajo está un personaje.
# El segundo número te dice qué tan a la izquierda o derecha está.


# La variable turn indica de quien es el turno.
turn = 'Raton'     


# Movimientos posibles: w/s/a/d → cambios en fila y columna
MOVS = {
    "w": (-1,0),                      
    "s": (1,0),  
    "a": (0,-1), 
    "d": (0,1)   
}


# Limpia la pantalla según el sistema operativo
def limpiar ():
    os.system("cls" if os.name == "nt" else "clear")  

  
# Verifica si la posición está dentro del tablero
def en_rango(f,c):
    return 0 <= f < ALTO and 0 <= c < ANCHO     


# Verifica si hay una pared en la posición
def es_pared(f,c):                                                       
    return TABLERO [f][c] == "#"            


# Verifica si la posición es la salida
def es_salida(f,c):                    
    return TABLERO [f][c] == "🚪"


# Verifica si la celda se puede usar para moverse
def celda_libre(f,c):
    return en_rango(f,c) and not es_pared(f,c)          


# Imprime el tablero en consola.
def imprimir_tablero(raton, gato):
    # Creamos una copia del tablero como una lista de listas.
    # Esto nos permite modificar los elementos sin cambiar el tamaño de la fila.
    tablero_para_imprimir = []
    for fila_str in TABLERO:
        tablero_para_imprimir.append(list(fila_str))

    # Actualizamos la posición del ratón o el gato en el tablero de copia
    if raton == gato:
        tablero_para_imprimir[raton[0]][raton[1]] = "❌"
    else:
        tablero_para_imprimir[raton[0]][raton[1]] = "🐭"
        tablero_para_imprimir[gato[0]][gato[1]] = "🐱"

    # Ahora imprimimos la versión modificada del tablero.
    # Recorremos cada fila de la nueva lista de listas.
    for fila_lista in tablero_para_imprimir:
        # Unimos los caracteres de la lista para formar una sola cadena para imprimir
        fila_str = "".join(fila_lista)
        
        # Agregamos espacios manualmente para que el tablero se vea uniforme
        linea_con_espacios = ""
        for char in fila_str:
            # Toma cada carácter de la fila (char) y lo agrega a la nueva cadena
            linea_con_espacios += char 
            # Si el carácter no es un emoji o la puerta de salida, agrega un espacio extra
            if char not in ["🐭", "🐱", "❌", "🚪"]:
                linea_con_espacios += " "
        print(linea_con_espacios)



# Devuelve las celdas donde un jugador puede moverse
def movimientos_validos(pos): 
    
    f,c = pos        
    validos = []  
    
    for df, dc in MOVS.values(): 
        nf, nc = f + df, c + dc  


        if celda_libre(nf,nc): 
            validos.append((nf,nc)) 
    return validos 

# Delta fila (df): es el cambio que vas a hacer en la fila.
# Delta columna (dc): es el cambio que vas a hacer en la columna.



# Movimiento del ratón controlado por el jugador
def mover_raton(raton): 
    while True: # Bucle que se repite hasta que ingreses un movimiento válido.
        tecla = input("Tu movimiento (w/a/s/d): ").lower().strip()
        if tecla not in MOVS: # Verifica si la tecla no está entre las permitidas (w, a, s, d).
                print("Tecla invalida. Usa w/a/s/d.")
                continue
        df, dc = MOVS[tecla] 
                            
        nf, nc = raton[0] + df, raton[1] + dc 
                                                    
        if not celda_libre(nf,nc): # Revisa si la celda destino no es válida (fuera de rango o pared).
            print("Pared! elige otra direccion.") 
            continue
        return(nf,nc) # Si todo está bien, devuelve la nueva posición del ratón y sale del bucle.



# Movimiento del gato usando estrategia "greedy" (se acerca al ratón)
def mover_gato_greedy(gato,raton): 
# Calcula todas las celdas a las que el gato puede moverse desde su posicion actual.(Sin salir del tablero ni atravesar paredes)    
    ops = movimientos_validos(gato) 
# Esta condicional dice que si no hay movimientos posibles(El gato esta bloqueado, el gato se queda donde esta.)
    if not ops:
        return gato

    def dist(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    return min(ops, key=lambda p: dist(p, raton))
       

         

# Esta función evalúa qué tan buena es una posición del tablero para el gato.
# Retorna un valor numérico.
def evaluar(raton, gato):
    if raton == gato:       
        return 100
   
    if es_salida(raton[0], raton[1]):
        return -100
    
    # Si ninguno gana, el valor depende de la distancia.
    # Queremos que el gato se acerque al ratón, así que un valor menor en la distancia Manhattan es mejor.
    # Restamos la distancia a un número grande para que un valor menor de distancia se traduzca en un valor mayor de puntuación.
    dist_gato_raton = abs(gato[0] - raton[0]) + abs(gato[1] - raton[1])
    return 50 - dist_gato_raton    
    



# Algoritmo Minimax para el gato
def minimax(pos_gato, pos_raton, profundidad, es_turno_gato):
    # Condición de parada (si llegamos al final del juego o a la profundidad máxima).
    if profundidad == 0 or pos_gato == pos_raton or es_salida(pos_raton[0], pos_raton[1]):
        return evaluar(pos_raton, pos_gato)

    if es_turno_gato: # Turno del Gato (MAXimizador)
        mejor_valor = -float('inf') # Empezamos con un valor muy bajo
        movimientos_posibles = movimientos_validos(pos_gato)
        for mov in movimientos_posibles:
            valor = minimax(mov, pos_raton, profundidad - 1, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    
    else: # Turno del Ratón (MINimizador)
        mejor_valor = float('inf') # Empezamos con un valor muy alto
        movimientos_posibles = movimientos_validos(pos_raton)
        for mov in movimientos_posibles:
            valor = minimax(pos_gato, mov, profundidad - 1, True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor


# Decide el siguiente movimiento del gato usando Minimax
def mover_gato_minimax(gato, raton):
    movimientos_validos_gato = movimientos_validos(gato)
    
    if not movimientos_validos_gato:
        return gato

    mejor_movimiento = None
    mejor_valor = -float('inf')
    
    # Itera sobre los movimientos posibles del gato
    for mov in movimientos_validos_gato:
        # Llama a minimax para ver cuál sería el resultado si el gato se moviera a 'mov'.
        # La profundidad de 4 turnos hace que el gato anticipe el movimiento del raton.
        valor_movimiento = minimax(mov, raton, 4, False)
        
        if valor_movimiento > mejor_valor:
            mejor_valor = valor_movimiento
            mejor_movimiento = mov
            
    # Si el mejor valor sigue siendo "infinito negativo",
    # significa que no se encontró un camino para el gato dentro de la profundidad del minimax.
    if mejor_valor == -float('inf') and mejor_movimiento is None:
        print("El gato no encontro un camino con minimax, usara la estrategia 'greedy'.")
        # El gato usará la estrategia codiciosa, que siempre lo acercara al ratón.
        return mover_gato_greedy(gato, raton)
        
    # Si se encontró un buen movimiento, el gato lo ejecutara
    return mejor_movimiento 



# LOOP PRINCIPAL

MAX_TURNOS = 100
turno_num = 1 

# Mientras turno_num sea menor que MAX_TURNOS se ejecuta el bucle principal.
while turno_num <= MAX_TURNOS: 
    limpiar() # Llamamos a nuestra funcion de limpiar la pantalla de la consola
    print(f"Turno {turno_num} - Juega: {turn}") # Imprimimos el numero de turno 1, y quien juega(gato o raton)
    imprimir_tablero(raton,gato) # Llamamos a la funcion que muestra el tablero de juego
    #print() # Imprimimos el tablero 

    # Condiciones para el fin del juego.
    if raton == gato:
        print("El gato atrapo al raton! 🐱🗿")
        break
    

    if es_salida(raton[0], raton[1]): 
        print("El raton llego a la salida! 🐭🎉")
        break

    if turn == "Raton":
        raton = mover_raton(raton)

# Chequeos despues de mover
        if raton == gato:
            limpiar()
            imprimir_tablero(raton, gato)
            print("\n! El gato atrapo al raton! 🐱🗿")
            break

        if es_salida(raton[0], raton[1]):
            limpiar()
            imprimir_tablero(raton, gato)
            print("\n! El raton llego a la salida! 🐭🎉")
            break
        
        # Alterna el turno
        turn = "Gato"
        

    else:  # turn == "Gato"

      
        # gato = mover_gato_greedy(gato,raton)
        gato = mover_gato_minimax(gato, raton) 
        
        if raton == gato:
            limpiar()
            imprimir_tablero(raton, gato)
            print("\n!El gato atrapo al raton! 🐱🗿")
            break
       
        # Alterna el turno
        turn = "Raton"
        
    turno_num +=1 

if turno_num > MAX_TURNOS:
    print("\nFin por turnos: !empate tecnico!")

