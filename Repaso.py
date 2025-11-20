# PRIMERO VAMOS A IMPORTAR LAS HERRAMIENTAS DE LA BIBLIOTECA DE PYTHON QUE VAMOS A USAR .

# Vamos a importar a la herramienta os (Operating System).
# Esta herramienta sirve para comunicarse con la computadora, basicamente para agregar, crear y eliminar carpetas.
# En el juego usaremos esta herramienta para limpiar la pantalla de la consola para imprimir solamente el tablero actualizado.
import os

# Vamos a importar ahora a la herramienta random.
# Esta herramienta es como un dado digital, no sabes que numero puede salir, pero son numeros de un rango establecido.
# Inicialmente lo usamos para que el gato se mueva con movimientos aleatorios sin tener inteligencia aun. 
import random 

# Vamos a importar ahora a la herramienta time.
# Su funcion principal es medir el tiempo o pausar un programa por un momento.
# En el juego lo vamos a usar para tener una pausa entre los turnos del jugador y la computadora.
# Sin time el jugador no podria ver el tablero ni reaccionar?
import time

# Ahora vamos a importar de la collection la clase "deque", esta va a ser nuestra cola.
# La cola es una estructura de datos que funciona con el principio de FIFO, primero que entra, primero que sale.
# En una cola agregamos nuevos elementos en la cola, y eliminas los elementos que estan al principio.
# "deque" seria como la hoja en donde vas a guardar los datos de las rutas que vas a recorrer en un laberinto hasta llegar al destino.
# "deque" es una version optimizada de la cola y la vamos a usar para poder implementar el algoritmo BFS(Busqueda en Amplitud).
from collections import deque 



# AHORA PASAMOS A CREAR EL TABLERO DE EL JUEGO.

# Voy a usar una cadena de texto para crear el tablero.
# Una cadena de texto es una secuencia de caracteres, letras, numeros, espacios o simbolos.
# Cada cadena de texto es una fila del tablero.
# Al igual que una tupla una cadena de texto no puede ser modificada una vez que es creada.
# Dentro de la cadena de texto, cada caracter es un elemento que el programa lee para saber si hay una pared, un espacio o salida
# Usamos un "#" para representar la pared, " " para una celda libre(camino) y una puerta para la salida 🚪
# Ancho = 22, Altura = 10 

TABLERO = [
    "######################",
    "#🚪                   #",
    "#                    #",
    "#                    #",
    "#                    #",
    "#                    #",
    "#                    #",
    "#                    #",
    "#                    #",
    "######################",
]

# AHORA VAMOS A CREAR DOS VARIABLES PARA ALMACENAR EL VALOR DEL ALTO Y ANCHO.


ALTO = len(TABLERO)    # Creamos la variable ALTO
                       # Con len(TABLERO) lo que hacemos es contar cuantos caracteres que tiene verticalmente el tablero
                       # Asi sabemos la altura del tablero y lo guardamos en la variable ALTO. ALTO = 10



ANCHO = len(TABLERO[0]) # Creamos la variable ANCHO.
                        # Con len(TABLERO[0]) lo que hacemos es contar los caracteres de la primera fila horizontalmente.
                        # Asi sabemos el valor del ancho del tablero y lo guardamos en la variable ANCHO. ANCHO = 22 

# EN RESUMEN.
# Las variables ALTO y ANCHO son esenciales para decirle al programa los limites del tablero.
# Es una forma de hacer que el tablero sea mas flexible, si cambiamos el tamanho de laberinto las variables toman esos valores nuevos.
# Estas variables garantizan que el juego o programa sepan donde estan los limites todo el tiempo.



# AHORA VAMOS A DEFINIR UNA POSICION INICIAL PARA EL GATO Y EL RATON.
# Que son las Tuplas?
# Es una lista con elementos que no puedes modificar al crearla.
# Se pueden acceder a sus elementos usando indices.
# Son muy utiles para guardar datos que no quieres que se modifiquen, como en este caso las coordenadas del gato y el raton.

# La posicion inicial del gato y el raton lo definimos en "Tuplas" porque no queremos que se cambien por error en el medio del juego.
# Ya que las tuplas sus datos son inmutables podemos asegurar que no van a variar las posiciones del gato y el raton

# Vamos a usar pares de valores para representar las filas y las columnas en el tablero.
# El primer numero representa la fila (Verticalmente, de arriba a abajo. Desde 0) "Y"
# El segundo numero representa la columna (Horizontalmente, de izquierda a derecha. Desde 0) "X"

#        y,x)
raton = (7,1)

#      (y,x)
gato = (2,1)



# El primer número de la tupla (fila, columna) te dice qué tan arriba o abajo está un personaje.
# El segundo número te dice qué tan a la izquierda o derecha está.


# ACA DEFINIMOS QUIEN COMENZARA PRIMERO, PRIMERO VA A SER EL TURNO DEL RATON.
# La variable turn indica de quien es el turno.

turno = 'Raton' 



# AHORA VAMOS A DEFINIR LOS MOVIMIENTOS POSIBLES DEL TABLERO TANTO COMO PARA EL GATO Y EL RATON.
# Vamos a usar un diccionario para crear los movimientos posibles en nuestro juego.
# Un diccionario es una estructura de datos que almecena informacion en pares de (Clave - Valor).
# Un diccionario puede usar cualquier tipo de dato como valor, la unica regla es que tiene que ser inmutable ese valor.
# Puede usar como valor (numeros, cadenas, listas, tuplas, etc)
# Vamos a hacer que nuestro diccionario MOVS haga un mapeo entre las teclas (w,s,a,d) y los movimientos correspondientes en el tablero.
# Mapeo es como adjuntar a un elemento su valor correspondiente.

MOVS = {
    "w" : (-1,0), # 1 paso arriba, 0 pasos al costado
    "s" : (1,0),  # 1 paso abajo, 0 pasos al costado
    "a" : (0,-1), # 0 pasos arriba, 1 paso a la izquierda
    "d" : (0,1),  # 0 pasos arriba, 1 paso a la derecha
}


# Al usar tuplas para los valores nos aseguramos de que el movimiento para cada tecla sea un conjunto de valores fijos.
# Que no puedan ser modificados durante la ejecuion del juego.
# Si usamos una lista como valor para el diccionario MOVS [-1,0] en otra parte del codigo se podria cambiar por error.
# Usar una tupla previene este tipo de errores. 


#  RESUMEN DE ESTA SECCION DE CODIGO.
# IMPORTACION DE BIBLIOTECAS: Importamos herramientas necesarias (os, random, time, deque) 
# Para usar fuciones especificas que nos permiten limpiar la pantalla y actualizar la consola.
# Generar aleatoriedad, manejar el tiempo y encontrar la ruta mas corta con Bfs.

# CREACION DEL TABLERO: Definimos el laberinto como una lista de cadena de textos.
# Esto nos permite representar las paredes, el camino y la salida del juego de manera visual y organizada.

# IMPLEMENTAMOS DOS VARIABLES: ANCHO Y ALTURA 
# Estas variables toman el tamanho exacto del tablero haciendo que el codigo sea adaptable y robusto.
# Podemos modificar el tamanho del tablero sin tener que modificar el resto del codigo.

# POSICIONES Y TURNO INICIAL: Almacenamos las coordenadas del gato y el raton en tuplas.
# Sus posiciones son pares de valores que no deben ser modificados por separado.
# Establecemos una variable para definir el primer turno del juego.

# MAPEO DE MOVIMIENTOS: 
# Utilizamos un diccionario para mapear cada tecla de movimiento a su coordenada correspondiente.
# Esto hace que el codigo sea mas claro y eficiente que usar multiples condiciones if.   




#  ACA VAMOS A COMENZAR CON LA PARTE DE LAS FUNCIONES DEL JUEGO.

# Primero vamos a definir una funcion para limpiar la pantalla de la consola con la herramienta "os".
# os.system() ejecuta un comando del sistema operativo desde python.
# En este caso limpiar la pantalla de la consola actual, e imprimir el tablero actualizado de forma limpia.

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear") 
    
# os. system es una funcion que recibe como argumento un operador condicional ternario para funcionar.
# Una mini condicional de una sola linea.
# En este caso el argumento es la cadena de texto que os.system debe ejecutar que se determina usando una logica condicional de una sola linea. 
# "cls" comando que se ejecuta en windows para limpiar la pantalla
# "clear" comando que se ejecuta en mac/linux para limpiar la pantalla
# "os.name" name es un atributo definido para os que devuelve el nombre del sistema operativo.

#RESUMEN DE LA FUNCION
# Definimos una funcion para limpiar la pantalla.
# Detecta si tu sistema operativo es Windows, Mac o Linux y ejecuta el comando adecuado.

# Vamos a definir una funcion que verifica si una posicion(fila,columna) esta dentro de los limites del tablero.
# return 0 <= f < ALTO and 0 <= c <ANCHO esta linea de codigo se lee asi:
# Revisa si la fila(f) es mayor o igual a 0 y si es menor que el ALTO del tablero.
# Pregunta, si la fila esta entre el borde de arriba(0) o el borde de abajo?
# Revisa si la columna(c) es mayor o igual a 0 y si es menor que el ANCHO del tablero.
# Pregunta, si la columna esta entre el borde izquierdo(0) y el borde derecho?
# "and" es crucial porque significa que las dos condiciones deben de ser verdaderas para que toda la linea sea verdadera.
# Si una de las dos falla, toda la condicion falla.

def en_rango(f,c):
    return 0 <= f < ALTO and 0 <= c < ANCHO


# EN RESUMEN
# La funcion en rango devuelve True si la posicion esta dentro del tablero y False si esta fuera.
# Esto hace al codigo robusto porque evita que el gato y el raton se muevan a posiciones que no existen. 
# La funcion solo verifica si las coordenadas de la fila y la columna estan dentro del area que definio como ALTO y ANCHO.
# Su funcion es evitar que el gato y el raton salgan de los limites del tablero.
# El codigo o la funcion no le permite al gato o al raton moverse a una posicion fuera del tablero.
# De esta manera el gato o el raton no podran salirse del tablero nunca.


# Ahora vamos a definir una funcion que defina que caracter es una pared.
# Esta funcion solo tiene una funcion es que verifique que "#" es una pared.
# La funcion toma las coordenadas de la fila(f) y la columna(c), verifica si el caracter en esa posicion del TABLERO es un #(una pared)
# Las toma por separado [f][c] para revisar la fila y luego la columna exacta donde se encuentra ese caracter para verificar si es pared

def es_pared(f,c):
    return TABLERO[f][c] == "#"

# Aca solo definimos la funcion mas adelante la vamos a usar en otras funciones.
# Una fila es todo el contenido de una línea horizontal (de izquierda a derecha).
# Una columna es todo el contenido de una línea vertical (de arriba a abajo).
# TABLERO [f][c] te permite encontrar el caracter exacto en la interseccion de una fila y una columna paso a paso.

# TABLERO[f][c] aca para que el codigo acceda a una celda del tablero se hace un proceso de dos pasos:
# [f] esto le dice a python que vaya directamente al indice f de la lista TABLERO. 
# Ej: si f es 2 salta directamente a la tercera fila del tablero.
# [c] una vez que esta en esa linea(la cadena de texto) le dices que vaya direcamente al indice c de esa cadena.
# Ej: si c es 5 salta directamente al sexto caracter de esa linea
# Se accede asi al tablero porque es una estructura de datos con dos dimensiones: (Fila y columna)
# El primer[f] selecciona la fila que quieres(cadena de texto) y el segundo[c] selecciona una columna(un caracter) dentro de esa fila.
# Es la unica forma de encontrar un elemento en un lugar especifico en una cuadricula.

# Ahora vamos a definir una funcion que especifique en el tablero el caracter que es una salida.
# En este caso este caracter "🚪"(una puerta) representa la salida al laberinto.

def es_salida(f,c):
    return TABLERO[f][c] == "🚪"

# EN RESUMEN
# Esta funcion comprueba si la posicion dada con coordenadas de fila y columna, es el caracter de "🚪"(salida) en el tablero.
# Si la celda en esta posicion es la salida, la funcion devuelve True y de lo contrario devuelve False, el juego va a seguir.
# Esto es util para saber si el raton ha llegado a su destino final y tambien si no, asi el juego sigue.

# TABLERO[f][c] aca para que el codigo acceda a una celda del tablero se hace un proceso de dos pasos:
# [f] esto le dice a python que vaya directamente al indice f de la lista TABLERO. 
# Ej: si f es 2 salta directamente a la tercera fila del tablero.
# [c] una vez que esta en esa linea(la cadena de texto) le dices que vaya direcamente al indice c de esa cadena.
# Ej: si c es 5 salta directamente al sexto caracter de esa linea
# Se accede asi al tablero porque es una estructura de datos con dos dimensiones: (Fila y columna)
# El primer[f] selecciona la fila que quieres(cadena de texto) y el segundo[c] selecciona una columna(un caracter) dentro de esa fila.
# Es la unica forma de encontrar un elemento en un lugar especifico en una cuadricula.  


# Ahora vamos a definir una funcion que verifica si la posicion(fila,columna) se puede usar para moverse.
# Para que una celda sea libre deben cumplirse dos cosas al mismo tiempo:
# Que la celda este dentro de los limites del tablero(en_rango), que este dentro del rango del tablero.
# Que la celda no sea una pared(es_pared), que la celda no sea una pared.

def celda_libre(f,c):
    return en_rango(f,c) and not es_pared(f,c)

# A la funcion se le dan los parametros de fila y columna porque queres saber que celda especifica queres verificar.
# Luego tenes una condicion de dos partes:
# en_rango(f,c): Esta parte pregunta, La posicion(f,c) esta dentro de los limites?
# and not es_pared(f,c): Luego si la primera parte es True. Esta parte pregunta la celda en esa posicion no es una pared(#)?
# Solo si ambas condiciones son True la funcion confirmara que la celda es segura para moverse.
# Si la funcion devuelve un False entonces el gato o el raton no podran moverse a esa posicion, se quedaran en es posicion.


# Ahora definimos la funcion para imprimir el tablero del juego en la consola.
# Va a recibir las posiciones como parametro del gato y el raton como tuplas(fila,columna).
# Usamos tuplas porque asegura que la funcion imprimir_tablero siempre recibira las dos coordenadas (f,c) juntas y sin cambios.

# La cadena de texto lo convertimos en una lista para modificar el contenido de esa lista, en este caso (la fila del tablero).
# Luego con el metodo .join el codigo une de nuevo todos los caracteres de la lista en una sola cadena de texto. 
# Esta nueva cadena es la que se imprime para mostrar el tablero actualizado en cada turno. 

def imprimir_tablero(gato,raton):

# Recorre todas la filas una por una. La variable f tomara cada valor de cada numero en la fila, de 0 hasta ALTO -1.(10-1)
# Esto permite trabajar con cada fila del tablero                               # El ultimo numero de ALTO no es 10, es 9
    for f in range(ALTO):
    
# Creamos una variable vacia donde durante el bucle le vamos a almacenar los caracteres que componen cada fila del tablero.    
# Una vez que este completa, se imprimira en la consola.
        fila_para_imprimir = "" 

# Esta linea toma la cadena de texto de la fila actual (TABLERO[f]) y la convierte en una lista de caracteres        
# Al convertir la fila en una lista se puede modificar facilmente 
        fila_original = list(TABLERO[f])

# Este bucle recorre cada columna de la fila convertida en lista  
# Recorre todas las columnas una por una. La variable c tomara cada valor de cada numero en la columna, de 0 hasta ANCHO -1= (22-1)
# Esto permite trabajar con cada columna de la fila convertida en lista                  # El ultimo numero del ancho no es 22 es 21
  
        for c in range(ANCHO):
# Guarda el caracter que se encuentra en la columna[c] de la fila_original en la variable caracter
# Toma el caracter especifico que esta en la posicion c de la lista que creamos(fila_original) y la guarda en la variable caracter.
# Lo obtiene que pase pueda trabajar con el
 
            caracter = fila_original[c]
# Si f(Fila actual) es igual a la fila del raton[0] y si la c(columna actual) es igual a la columna raton[1].
# Estamos comprobando que la posicion actual del bucle(f,c) sea exactamente igual que la posicion del raton.
# and raton != gato es una condicion adicional que comprueba que el raton no este en la misma posicion del raton.
# Si es asi el emoji el raton no se imprimira, se imprimira un emoji que indique el gato atrapo al raton.
# Si la posicion del raton no es la misma que la del gato imprimimor el emoji del raton para visualizar su lugar en el tablero.
            if f == raton[0] and c == raton[1] and raton != gato:

                fila_para_imprimir += "🐭"

# Si la f(fila actual) es igual a la fila del gato[0] y si la c(columna actual) es igual a la columna del gato[1].
# Estamos comprobando que la posicion actual del bucle(f,c) sea exactamente igual que la posicion del gato.
# "and gato != raton:" es una condicion adicional que verifica que el gato no este en la misma posicion del raton.
# Si lo esta el emoji del gato no se imprimira , se imprimira un emoji que indica que el gato atrapo al raton.
# Si la posicion del gato no es la misma que el del raton, el emoji del gato se imprimira para visualizar su posicion en el tablero.
            elif f == gato[0] and c == gato[1] and gato != raton:
                fila_para_imprimir += "🐱"

# "+=" es un operador de asignacion en python.
# Toma el caracter actual de la variable(fila_para_imprimir) y le anhade el emoji del raton o el gato.
# Luego lo vuelve a guardar en la misma variable(fila_para_imprimir), reemplazando el valor anterior.


# La primera parte de la condicion verifica si el raton esta en la misma posicion que el gato.
# La segunda parte de la condicion verifica que la posicion actual del bucle(f,c) es la misma que la posicion del raton(y del gato)
# Si la posicion del gato y del raton es la misma, se imprime el emoji "❌" que significa que le gato atrapo al raton.
            elif raton == gato and f == raton[0] and c == raton[1]:
                fila_para_imprimir += "❌"


            else: # Si no hay el emoji del gato, el raton o la x, imprime el caracter original que es una celda vacia.
                fila_para_imprimir += caracter


# Despues de agregar los emojis recorremos una nueva linea para agregar los espacios.
# Creamos una variable en donde vamos a almacenar los espacios.
# Esta variable para construir la nueva linea con espacios adicionales.
        linea_con_espacios = ""

 # Este bucle recorre cada caracter de la cadena fila_para_imprimir. 
 # En cada vuelta la variable caracter tomara el valor del caracter actual en esa vuelta      
        for caracter in fila_para_imprimir:

# Esta linea siempre se ejecuta
# Agrega el caracter actual(caracter) a la cadena (linea_con_espacios) esto asegura que los elementos de la fila original se mantengan
# En el nuevo string.
            linea_con_espacios += caracter

#  Esta condicional verifica que el caracter actual no se encuentre en la lista de emojis, si ese caracter no es un emoji la condicion es verdadera. 
            if caracter not in ["🐭","🐱","❌","🚪"]:

# Esta linea lo que hace es agregar un espacio en blanco (" ") a la cadena(linea_con_espacios).
# Esto crea el espacio adicional a los caracteres normales                
                linea_con_espacios += " "

# Esta linea imprime la cadena final que se creo, con un espacio adicional para el caracter normal y los emojis se imprimen normal
        print(linea_con_espacios)




# Esta funcion construye la lista de celdas a las que se pueda mover el raton o el gato considerando los limites del tabler y paredes.
# La funcion recibe un argumento llamado posicion, que es la posicion de un personaje en el tablero.(Gato o raton)
# posicion es una tupla con dos valores fijos(fila,columna)
def movimientos_validos(posicion): 

# Desempaqueta la variable posicion, toma el primer valor de la tupla y lo guarda en la variable f(fila)
# Luego toma el segundo valor de la tupla y lo guarda en la variable c(columna)     
    f,c = posicion 

# Creamos una lista vacia en donde vamos a almacenar a las posiciones que se pueden mover el gato y el raton.
    validos = []    

# Recorre sobre los posibles movimientos, permitiendo calcular la nueva posicion, sumando estos cambios a la posicion actual del personaje.
# MOVS.values con ".values" solo usas los valores del diccionario MOVS, solo necesitamos los valores sin la clave.
# Es decir solo nos da las tuplas que contienen los cambios de fila y columna para cada movimiento.
# for df, dc in MOVS.values es un bucle que solo desempaqueta cada una de esas tuplas.
# En cada vuelta, "df" se convierte en el cambio de fila y "dc" se convierte en el cambio de columna
    for df, dc in MOVS.values():

# Suma la fila actual(f) con el cambio de fila del movimiento(df)
# Suma la columna actual(c) con el cambio de columna del movimiento(dc)
# El resultado de esas dos sumas se guarda en las variables nf(nueva fila) y nc(nueva columna).
        nf, nc = f + df, c + dc 

# La funcion celda_libre recibe como argumentos, nueva fila y nueva columan(nf,nc) para determinar si la celda es un lugar valido para moverse.
# Recordemos que la funcion revisa dos cosas que este en_rango(dentro del limite) y que no sea una pared(es_pared).
# Solo los caracteres en blanco " " se consideran una celda libre en el tablero del juego.
        if celda_libre(nf,nc):

# Anhadimos la celda a la lista de movimientos validos una vez pasada la verificacion de la funcion celda_libre.
# Tienen doble parentesis la nueva fila(nf) y la nueva columna(nc) porque las agregamos como una tupla dentro de la lista.
# El parentesis interno es la que convierte los dos valores(nf,nc) en tuplas.
# El parentesis exterior es parte de la sintaxis del metodo .append, debes agregar() al elemento que quieres agregar a la lista.
# En este caso a la tupla (nf,nc).          
            validos.append((nf,nc))
 
 # Retornamos la lista de movimientos validos(validos) al lugar donde se llamo la funcion.
 # Esto permite al resto del programa saber cuales son los movimientos posibles desde la posicion actual del personaje.
    return posicion


# Ahora vamos a hacer una funcion para mover al raton, para darle movimientos
# Al usar la posicion inicial(raton) como parametro, le permite a la funcion saber donde esta el raton para calcular su proximo movimiento.  
def mover_raton(raton):

# Definimos un bucle que se repite hasta que ingreses un movimiento valido.
# Al ingresar un movimiento valido el bucle se rompera hasta el proximo turno del raton.
    while True:

# Creamos una variable en donde le pedimos al usuario ingresar los movimientos permitidos que quiera hacer.
# Con .lower cualquier caracter que ingrese sera en minuscula y con .strip eliminara los espacios que se puedan poner por error.
# El movimiento permitido ingresado se almacena en la variable "tecla".
        tecla = input("Tus movimientos(w/s/a/d): ").lower().strip()

# Definimos una condicional si el usuario ingresa una tecla invalida, imprimimos un mensaje avisandole y mostrandole las teclas validas.
        if tecla not in MOVS:
            print('Tecla invalida. Usa w/s/a/d')

# Es una palabra clave de python, cuando se ejecuta lo que hace es saltar el resto del bloque de codigo que le sigue.
# Reiniciando la iteracion, volviendo a iniciar la funcion hasta que el usuario ingrese la tecla correcta.                       
            continue

# MOVS[tecla] busca la tecla que el usuario ingreso.
# Cuando el codigo lo encuentra adquiere el valor de la tupla que esta asociada a la tecla en el diccionario MOVS.
# "df, dc" desempaqueta la tupla, se asigna el primer valor de la tupla a la variable "df", y el segundo valor a la variable "dc".
# Si MOVS["w"] = (-1, 0), entonces:
#  df = -1 
#  dc = 0
        df, dc = MOVS[tecla] 

# "raton[0] + df": calcula la nueva fila. (raton[0] es la posicion actual de la fila del raton)
# "df" es el valor que cambia de fila que se adquirio del diccionario MOVS, segun la tecla que el usuario ingreso
# "raton[1] + dc": calcula la nueva columna. (raton[1] es la posicion actual de la columna del raton)
# "dc" es el valor que cambia de columna que tambien se adquirio del diccionario MOVS, segun la tecla que el usuario ingreso.
# El resultado de la primera suma se le asigna a la variable "nf"
# El resutaldo de la segunda suma se le asigna a la variable "nc"
        nf, nc = raton[0] + df, raton[1] + dc

#  Esta condicional verifica si la celda de destino esta libre o no (Fuera de rango o si es una pared).
        if not celda_libre(nf,nc):
# Informamos que es una pared y que ingrese otra tecla en otra direccion.
            print("Pared! Elige otra direccion.")

# Con este continue saltamos la linea de codigo que sigue.
# Reiniciamos la funcion para volver a pedir al usuario que ingrese otra tecla.
            continue

# Retornamos la nueva posicion calculada del raton en forma de tupla(nueva fila, nueva columna) al lugar donde la funcion fue llamada.
# Permitiendo al raton que se mueva a esa posicion.    
        return(nf,nc) 


# Ahora vamos a definir una funcion con una estrategia greedy(codicioso) para mover al gato.
# Le damos a la funcion como parametros las posiciones iniciales del gato y el raton.
def mover_gato_greedy(gato,raton):

# movimientos_validos(gato) Esta parte llama a la funcion movimientos_validos y le pasa como argumento la posicion inicial del gato.
# movimientos_validos ejecuta su funcion y devuelve una lista de todas las posiciones a las que el gato puede ir.
# ops recibe recibe el valor de esa lista de movimientos
# ops es una lista de tuplas con las coordenadas de los movimientos validos.
    ops  = movimientos_validos(gato)

# Esta condicional dice que si no hay movimientos posibles en la lista ops. (el gato se queda en su lugar.)
# Si no hay movimientos posibles la condicion es verdadera.
    if not ops:
# Retorna la misma posicion del gato dejandolo en su lugar.
        return gato

# Definimos una funcion auxiliar que mide la distancia Manhattan entre dos posiciones (a y b).
# Recibe dos parametros (a,b) que son las posiciones(tuplas) a comparar
    def dist_Manhattan(a,b):
    # a[0] y b[0] son las coordenadas de la fila del punto a y del punto b.
    # a[1] y b[1] son las coordenadas de la columna del punto a y del punto b.
    # "abs"(valor absoluto) es una funcion que elimina el signo negativo de un numero.
    # El resultado de las restas de las coordenadas de la fila(a[0]-b[0]) y columna(a[1]-b[1]) se suman.
    # Para saber cuantos pasos das en vertical y en horizontal para llegar a tu destino o objetivo.
    # Esta formula devuelve la suma de las distancias entre filas(a[0]-b[0]) y la distancia entre las columnas (a[1]-b[1]) entre dos puntos (a,b) 
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

# La funcion min() busca el menor valor en una lista, la lista es "ops" que contiene todos los posibles movimientos del gato.
# "key=lambda p:" le dice a a min() como decidr cual es valor pequenho, no compara las tuplas, usa una clave para la comparacion.
# La clave es resultado lampda p: dist_Manhattan(p,raton).
# dist_Manhattan(p,raton) Esta funcion calcula la distancia entre el movimiento posible(p) y la distancia del raton.
# min() usara esta distancia para encontrar el movimiento que le de el valor mas bajo.
# min() no devuelve la distancia sino la posicion(p) que produce esta distancia minima.
    return min(ops, key=lambda p: dist_Manhattan(p, raton))
    
# EN RESUMEN.
# Esta linea devuelve el movimiento de la lista "ops" que tenga la distancia manhattan mas corta al raton.
# El codigo usa lambda p: para que min() sepa que debe comparar distancias y no las coordenadas de las tuplas.



# Aca vamos a colocar nuestra funcion de Busqueda en anchura(Bfs).
# La funcion toma dos parametros: 'inicio' la posicion inicial, y 'destino' la posicion final.
def ruta_bfs(inicio,destino):

# Si el destino es igual que el inicio, devuelve una lista con solo el punto de inicio.
# Comprueba si el punto de inicio y el destino de la ruta son la misma celda. Si es asi ya estas donde necesitas estar.
# La funcion ya no necesita buscar en camino, simplemente devuelve una lista con el unico punto de la ruta.
# Esto evita que el algoritmo Bfs haga un trabajo innecesario cuando el destino ya se alcanzo.
    if destino == inicio:
        return [inicio]

# Creamos la estructura de datos principal del Algoritmo Bfs, una cola utilizando la clase "deque".
# deque funciona como una lista optimizada, te permite agregar y eliminar elementos de forma muy rapida.
# La cola va a almacenar las posiciones que el algoritmo debe visitar.
# Se inicializa con la posicion de inicio. 
    cola = deque([inicio])

# Creamos un conjunto (set) llamados visitados.
# Conjunto (set) es una estructura de datos que solo almacena elementos unicos y sin duplicados.
# {inicio} inicializa el conjunto(set) con la posicion de inicio.
# Esto es importante porque el algoritmo no necesita procesar la celda inicial, que es el punto de partida.
# "visitados" es una coleccion que lleva un registro de las celdas por las que el algoritmo ya ha pasado.
# Evita que entre en bucles infinitos y garantiza que cada celda solo se procese una vez.
# {inicio} esta entre corchetes porque se utiliza para crear un conjunto. 
    visitados = {inicio}

# Creamos un diccionario padres que asocia la posicion de inicio a un valor vacio(None)
# Padre Es el nombre del diccionario que se esta creando.
# {inicio: None} Esto inicializa el diccionario con una sola entrada. La clave es la posicion de inicio(inicio) y el valor es None(nada)
# Este diccionario actua como un mapa, registrando de donde viene cada celda
# Si el algoritmo se mueve de la celda A a la celda B, el diccionario guardara que el "padre" de B es A.(padres[B]= A)
# El algoritmo primero explora para encontrar el destino y guarda la informacion de la ruta en el diccionario(padres).
# Cuando el algoritmo llega al destino, no retrocede de inmediato consulta al diccionario para reconstruir el camino que ya tomo.
# Yendo del destino al punto de partida, luego le da la vuelta a esa lista para tener la ruta correcta.
    padres = {inicio: None}

# Se ejecuta un bucle while, en donde el algoritmo toma y revisa cada celda de la cola hasta que se vacie.
# Cuando se vacia la cola, la condicion while cola se vuelve falsa y el bucle se detiene.
    while cola:


# "cola.popleft" es una operacion que se realiza en una cola(deque) Saca el elemento que esta mas a la izquierda(mas antiguo) y lo elimina.
# Bfs funciona como una linea de espera, procesa a los elementos en el orden en el que llegan.
# Usar popleft garantiza que siempre se procese la celda que esta primero en la fila, lo cual es la clave para encontrar el camino mas corto
# "popleft" agarra la lista de "cola" y extrae el primer elemento en la variable actual para que el algoritmo lo analice.
# pop = extraer
# left = izquierda
       actual = cola.popleft() 

# Verificamos si la posicion actual que estamos revisando es el destino.
# Si es asi, significa que hemos encontrado el camino mas corto.
       if actual == destino:
 
 # Creamos una lista vacia dentro del if para reconstruir y almacenar la ruta encontrada.           
           ruta = []

# Mientras la variable "actual" no tenga el valor de None, ejecuta lo que hay dentro de este bloque
           while actual is not None:

 # Agregamos a la lista ruta la posicion actual que el algoritmo analizo, con el metodo ".append" para agregar elementos a una estrutura de datos.
 # Al usar el metodo ."append" el codigo va a guardar cada paso en el orden correcto, para al final tener la ruta completa desde el raton al gato.            
               ruta.append(actual)

# Hace un recorrido hacia atras para reconstruir la ruta que ha seguido el gato para encontrar al raton.
# Asigna a la variable "actual" el valor que se encuentra en el diccionario padres, usando la posicion actual como la clave.
# Esta linea de codigo te permite ir de un hijo a un padre, reconstruyendo el camino en orden inverso desde el punto de llegada al punto de partida.
# Ej: Actual es (2,1), el codigo hace lo siguiente busca la clave (2,1) en el diccionario padres, encuentra su valor (1,1), entonces asigna (1,1) a la variable "actual".
# Este proceso se repite hasta llegar a la posicion inicial, esto permite al programa saber el camino completo que debe seguir el gato.
               actual = padres[actual]

# Esta linea de codigo invierte el orden de la ruta de forma inversa desde el destino(raton) hasta el inicio(gato).
# El metodo .reverse invierte el orden la lista para que el camino se lea en orden correcto, del inicio al destino.
# Esto permite al gato moverse paso a paso en la direccion correcta para atrapar al raton.
           ruta.reverse()

# Aca devolvemos el valor de la ruta reconstruida y con el orden correcto (inicio a destino).
           return ruta
       

# Para cada movimiento posible en la lista de movimientos, haz lo siguiente.
# Asigna a las variables df(delta fila) y dc(delta columna) los valores de la tupla de movimiento.
# .values(), accede a los valores del diccionario MOVS, que son las tuplas que representan los movimientos.
# Este caso es si no hemos llegado a destino, el algortimo explora las posiciones vecinas.
# Este bucle recorre todos los movimientos posibles definidos en el diccionario MOVS.
       for df, dc in MOVS.values():

# En esta linea calculamos el proximo paso o celda que puede dar el gato.
# La nueva fila(nf) toma el valor de la suma de la celda actual + el cambio de fila(df), (nc) toma el valor de la suma de la celda actual + el cambio de columna(dc)
# (nf,nc) toman el valor de las coordenadas de las celdas vecinas, las ubicaciones que se van a analizar.
# (nf,nc) representan el proximo posible paso del gato.
          nf, nc = actual[0] + df, actual[1] + dc 

# Guardamos esos proximos pasos posbles o celdas posibles en una tupla.
          vecino = (nf,nc)

# Creamos una condicional en donde comprobamos si las celdas vecinas son celdas libres, y no son celdas ya visitadas.
# Es una condicional que comprueba dos cosas para decidir si puede moverse a una nueva celda vecina.
# la funcion "celda_libre(nf,nc)" comprueba si la celda vecina es un lugar valido para moverse(no es una pared, esta dentro de los limites del tablero.)
# "vecino not in visitados" si es un lugar valido verfica que esa celda no haya sido visitada ya por el algoritmo de busqueda.
# Si ambas condiciones se cumplen la celda se consideda un lugar seguro y nuevo para explorar.
# Esta doble verificacion es clave en algoritmos de busqueda como (Bfs) para encontrar el camino de manera eficiente y evitar bucles infinitos.
          if celda_libre(nf,nc) and vecino not in visitados:
              
# Esta linea de codigo agrega la posicion de la celda vecina analizada al conjunto set "visitados" para marcarlo como visitado.
# Para evitar analizar de nuevo esa celda asi evita entrar en un bucle infinito. Hacemos al algoritmo mas eficiente y que siempre analice nuevos territorios.
              visitados.add(vecino)

# Esta linea de codigo registra el camino, es como dejar migas de pan.
# Guarda en el diccionario "padres" que la celda actual es la que lleva a la celda vecina(vecino). 
# Significa que la posicion de la celda vecina (vecino) se convierte en la 'clave' y la posicion de la celda actual(actual) se convierte en el 'valor'.
# "= actual" Almacena la posicion de la celda actual(actual) como el 'valor' de la 'clave'[vecino] 
# Asi cuando el algortimo encuentra el destino podra usar al diccionario padres para retroceder de una celda a otra y reconstruir la ruta completa. 
              padres[vecino] = actual


# Aca agregamos a la posicion de la celda vecina a la cola para que sea analizado mas tarde.
# La cola agrega la posicion de la celda vecina a la cola de celdas pendientes. 
# Almacena los lugares a los que se puede mover para explorarlos despues.
# Esto asegura que el algoritmo analice todas opciones posibles para encontrar el mejor camino.
              cola.append(vecino)


# Esta linea se usa para indicar que el algoritmo de busqueda no pudo encontrar una ruta del inicio(posicion inicial gato) al destino(raton).
# return devuelve una lista vacia para que el resto del programa sepa que no hay una ruta posible.
# Si el bucle while cola termina (la cola se vacía) sin haber encontrado una ruta que llegue al destino.
# Significa que no hay un camino posible entre el inicio y el destino. 
# En ese caso, la función devuelve una lista vacía.
    return[]



# Ahora vamos a crear una funcion la que le da una logica para cada decision al gato..
# Esta funcion de la un puntaje a cada posible posicion en el tablero, lo que le permite al gato elegir la posicion con el puntaje mas alto, la que le acerca mas al raton.
# Un puntaje mas alto significa que esta mas cerca de ganar el gato, y un puntaje bajo significa que esta mas cerca de ganar el raton.
# Por eso el gato siempre buscara el puntaje mas alto porque es por definicion lo que le acercara a su objetivo(el raton).
# El código le permite al gato "pensar" y tomar decisiones estratégicas basadas en el puntaje, lo que lo hace más inteligente.

def evaluar_movimiento(raton, gato):

# Si el gato atrapa al raton, es la mejor situacion para el gato (ya que es el objetivo del gato) devolvemos 100 puntos. 
    if raton == gato:
        return 100

# Si el raton se encuentra en la posicion de salida del juego (el raton gana) devolvemos -100 puntos, la peor situacion posible. 
    if es_salida(raton[0], raton[1]):
         return -100


    
# En la variable ruta llamamos a la funcion ruta_bfs para encontrar el camino mas corto entre el gato y el raton.
# Esto ayuda a entender al gato que tan lejos esta de su objetivo.
    ruta = ruta_bfs(gato, raton)


# Si no se encuentra una ruta, la distancia se establece como infinita, esto le dice al programa que el raton esta a salvo y no se puede llegar a el.
    if not ruta:        
        dist_gato_raton = float("inf")

# Si se encuentra una ruta, se calcula la distancia. La longitud de la lista ruta se usa para saber a cuantos pasos esta el gato del raton.
# Con len() en Python se utiliza para obtener la longitud(cantidad de elementos) de la lista.
# La formula len(ruta) - 1 siempre dara el numero correcto de movimientos, sin importar cuan larga sea la ruta.
# La lista "len(ruta) - 1" solo te dara el numero de celdas en la ruta, no el numero de movimientos. 
    else:
        dist_gato_raton = len(ruta) - 1

# El codigo evalua las distancias y las convierte en puntuaciones que el gato pueda entender.
# dis_gato_raton Representa el numero de pasos que el gato necesita para atrapar al raton.
# 50 - dist_gato_raton. El 50 se resta al numero de pasos que el gato necesita para atrapar al raton, de esta manera un numero de pasos mas corto al raton.
# Resulta en un puntaje mas alto y una distancia de pasos mas larga al raton resulta resulta en un puntaje mas bajo.
# el gato a tomar una dcision simplemente elige el movimiento que le da el puntaje mas alto, que es el que lo acerca mas al raton.
# El 50 sirve para convertir un numero de pasos corto al raton en un puntaje mas alto que necesita el gato para tomar la mejor decision que lo acerque al raton.
    return 50 - dist_gato_raton 


# Ahora vamos a crear la funcion principal del algorimo minimax.
# La funcion toma estos parametros, son la informacion base que necesita el algoritmo para comenzar a analizar la situacion del juego.
# pos_gato y pos_raton, son las posiciones actuales del gato y el raton en el tablero.
# profundidad, es la cantidad de turnos que el algoritmo va a pensar por adelantado(4).
# es_turno_gato este parametro booleano es clave para que el algoritmo sepa de quien es el turno. 
# Esto le permite si debe maximizar(gato) o debe minimizar(raton) la puntuacion en cada paso.

def minimax(pos_gato, pos_raton, profundidad, es_turno_gato):

# Casos base del algoritmo minimax: Su proposito es detener la busqueda recursiva del algoritmo cuando ya no es necesario seguir explorando mas movimientos.
# Si profundidad es iguala cero o si el gato atrapo al raton o el raton se encuentra en la salida.
# Al cumplirse una de estas condiciones el algoritmo detiene la busqueda recursiva.
     if profundidad == 0 or pos_gato == pos_raton or es_salida(pos_raton[0],pos_raton[1]):
         
# Al cumplirse una de estas condiciones el algorimo deja de pensar y devuelve un puntaje.
# Este puntaje es calculado por la funcion evaluar_movimiento(),este le dice que tan buena es la situacion del gato en ese momento.
# Al usar esta logica el algoritmo Minimax evitas bucles infinitos y encuentra el resultado final para tomar una decision.
         return evaluar_movimiento(pos_gato, pos_raton)
     
# Este bloque maneja la parte del algoritmo de Minimax que corresponde al turno del gato.
# Esta condicional verifica si es turno del gato, si esa asi se ejecuta el siguiente bloque de codigo.
     if es_turno_gato:

# "mejor_valor" es una variable que guardara el mejor puntaje que el gato puede obtener.
# Se inicializa con - infinito para que cualquier puntaje que se obtenga de un movimiento sea siempre mayor y lo reemplace.
          mejor_valor = - float("inf")

# Esta linea encuentra todas las celdas posibles a las que el gato se puede mover desde su posicion actual con la funcion 'movimientos_validos'.
# La variable movimientos_posibles guardara las celdas posibles a la que el gato se pueda mover.
          movientos_posibles = movimientos_validos(pos_gato)

# El codigo entra en un bucle for en donde recorre todos los movimientos posibles que puede hacer el gato
     for mov in movientos_posibles:

# En esta linea, el algoritmo se llama a si mismo de una manera recursiva.
# Le dice a la funcion Minimax que simule que pasaria si el gato se moviera a la posicion 'mov' analizada.
# 'produndidad - 1, disminuye la prufundidad y False indica que ahora simule que es el turno del raton.
         valor = minimax(mov, pos_raton, profundidad - 1, False)

# Esta linea compara el 'mejor_valor' actual con el 'valor' que se obtuvo de la simulacion del movimiento. 
# 'max' selecciona el puntaje mas alto porque el gato quiere obtener el mejor puntaje posible 
         mejor_valor = max(mejor_valor, valor)

# Finalmente el codigo devuelve el 'mejor_valor' que el gato puede lograr considerando sus movimientos, es la decision que tomara el gato en su turno,
         return mejor_valor    

# En resumen el codigo le permite al gato simular cada uno de sus movimientos posibles, elegir el que le de mejor puntaje mas alto y luego descartar el resto.


# Este bloque de codigo se encarga de simular los movimientos del raton, el cual siempre buscara minimizar la puntuacion del gato.
     else: # Simulamos el turno del raton.
         
#'mejor_valor' es una variable que que guardar el peor puntaje para el gato.
# Se inicializa con un valor de infinito para que cualquier puntaje que se obtenga sea siempre menor y lo reemplace. 
         mejor_valor = float("inf")

# Esta linea encuentra todas las celdas a la que el raton desde su posicion actual se puede mover.
# En la variable 'movimientos_posibles' se guarda los movimientos posibles que el raton pueda hacer.
         movientos_posibles = movimientos_validos(pos_raton)


# Creamos un bucle for en donde el programa recorre cada uno de los movimientos posibles del raton.
     for mov in movientos_posibles:

# En esta linea el algoritmo se llama a si misma de manera recursiva.
# Le dice a la funcion Minimax que simule que pasaria si el raton se moviera a la posicion 'mov' analizada.
# 'profundidad - 1' disminuye la profundidad y 'True' indica que ahora es de vuelta el turno del gato.
         valor = minimax(mov, pos_raton, profundidad - 1, True)

# Esta linea compara al 'mejor_valor' actual con el 'valor' que se obtuvo de la simulacion del movimiento.
# 'min()' seleeciona el puntaje mas bajo, ya que el raton siempre quiere que el gato sea lo mas bajo posible. 
         mejor_valor = min(mejor_valor, valor)

# Finalmente el codigo devuelve el 'mejor_valor' que el raton pudo encontrar, lo que le indica al gato cual es la estrategia para si mismo.
         return mejor_valor 



# Ahora vamos a hacer la funcion que le va a decir al gato a donde moverse en cada turno.
# Esta funcion es el cerebro del gato porque le dice a donde moverse.
# Usa como base o parametros las posiciones actuales del gato y del raton.
# Esta funcion utilizara el algoritmo Minimax para analizar todas las opciones posibles y elegir la mejor jugada para el gato en su turno.

def mover_gato_minimax(gato,raton):

# Esta linea encuentra todas las posiciones a las que el gato se puede mover en el tablero.
# Utiliza la funcion 'movimientos_validos' para revisar las celdas alrededor del gato y ver cuales son accesibles.
# El resultado es una lista de posiciones o movimientos que el gato puede hacer, se guarda en la variable movimientos_validos_gato.
# Usamos esta linea de codigo para que el algoritmo Minimax sepa que movimientos tiene el gato para analizar.
# Sin ella, el algoritmo no podria simular el juego, ya que no sabria a done se puede mover el gato.
    movimientos_validos_gato = movimientos_validos(gato)

# Si la variable no contiene los movimeintos posibles del gato desde su posicion actual, entonces el codigo devuelve la posicion actual del gato.
# Se usa para manejar una situacion en donde el gato no encuentre una ruta hacia el raton, esta condicional le dice al gato que se quede en su lugar.
# En lugar de causar un error en el programa. 
    if not movimientos_validos_gato:
        return gato 

# Esta variable se inicializar con un valor de None(nada), esto significa que al principio no hay un mejor movimiento seleccionado.
# Esta variable se actualizara mas tarde con el movimiento real que el gato debe hacer.
    mejor_movimiento = None

# Esta variable se inicializa con un valor de - infinito. 
# Esto se hace para asegurar que el puntaje del primer movimiento que el algoritmo evalue siempre sea mayor que el valor inicial - infinito.
# Lo que garantiza que se registre como el mejor primer movimiento.
    mejor_valor = - float('inf')


# Este bloque de codigo analiza cada movimiento posibe del gato para encontrar el mejor movimiento. Es la parte central de la funcion 'mover?gato_minimax'
#Este bucle for revisa cada movimiento posible del gato, en cada vuelta la variable mov guarda una de las posiciones a las que el gato se puede mover.
    for mov in movimientos_validos_gato:

# Esta linea llama al algoritmo minimax para cada movimiento posible del gato.
# Le dice a Minimax que simule el juego 4 turnos hacia adelante(profundidad 4).
# Con False que ahora asuma que es el turno del raton.
# La funcion minimax devuelve un puntaje para ese movimiento
        valor_movimiento = minimax(mov, raton, 4, False)

# Esta linea crea una condicional en donde compara el puntaje del movimiento actual(valor_movimiento) con el puntaje que se ha encontrado hasta ahora(mejor_valor).
# Si el puntaje actual(valor_movimiento) es mayor que el puntaje encontrado(mejor_valor) significa que es la mejor opcion para el gato.
        if valor_movimiento > mejor_valor:

# Si se encuentra un puntaje mejor, esta línea actualiza la variable mejor_valor con el nuevo puntaje más alto.
            mejor_valor = valor_movimiento

# Y esta línea actualiza la variable mejor_movimiento con la posición (mov) que generó ese puntaje. 
# Así, el código recuerda no solo el mejor puntaje, sino también el movimiento que lo causó. 
            mejor_movimiento = mov 


#  En este bloque de codigo hacemos un plan de respaldo para el gato si el algoritmo Minimax np logra encontrar una ruta para atrapar al raton.
# El gato cambia a una estrategia mas basica.

# Esta linea verifica si el algoritmo Minimax fracaso en encontrar un movimiento hacia al raton.
# Lo sabe porque el mejor valor se mantuvo en -infinito y la variable 'mejor_movimiento' sigue teniendo un valor de None.
    if mejor_valor == - float('inf') and mejor_movimiento is None:

# Si la condicion anterior se cumple, se imprime un mensaje en la pantalla informando que el gato usara la estrategia greedy
        print("El gato no encontro un camino con Minimax, usara la estrategia greedy")

# El rpograma le dice al gato que use la estrategia greedy como respaldo.
# Esta estrategia es sencilla y siempre mueve al gato a la celda que mas le acerque al raton 
        return mover_gato_greedy(gato, raton)

# Esta linea devuelve el mejor movimiento que el algoritmo encontro. El gato se mover a esa posicion.    
    return mejor_movimiento 



# LOOP PRINCIPAL

MAX_TURNOS = 200
turno_num = 1 

# Mientras turno_num sea menor que MAX_TURNOS haz esto
while turno_num <= MAX_TURNOS: 
    limpiar_pantalla() # Llamamos a nuestra funcion de limpiar_pantalla  de la consola
    print(f"Turno {turno_num} - Juega: {turn}") # Imprimimos el numero de turno 1, y quien juega(gato o raton)
    imprimir_tablero(raton,gato) # Llamamos a la funcion que muestra el tablero de juego
    print() # Imprimimos el tablero 

    # Condiciones para el fin del juego.
    if raton == gato:
        print("El gato atrapo al raton! 🐱🗿")
        break
    
# El 0=(x) y el 1=(y) son índices que dicen “toma el primer número” o “toma el segundo número” de la posición”
# se usan para poder pasar cada coordenada por separado a funciones como:
# es_salida(raton[0], raton[1])
# dist(raton[0], raton[1])
# Así la función sabe exactamente dónde está el ratón en X y Y.
    if es_salida(raton[0], raton[1]): 
        print("El raton llego a la salida! 🐭🎉")
        break

    if turn == "Raton":
        raton = mover_raton(raton)

# Chequeos despues de mover
        if raton == gato:
            limpiar_pantalla()
            imprimir_tablero(raton, gato)
            print("\n! El gato atrapo al raton! 🐱🗿")
            break

        if es_salida(raton[0], raton[1]):
            limpiar_pantalla()
            imprimir_tablero(raton, gato)
            print("\n! El raton llego a la salida! 🐭🎉")
            break
        
        # Alterna el turno
        turn = "Gato"
        


    else:  # turn == "Gato"


        # gato = mover_gato_random(gato)
        # gato = mover_gato_greedy(gato,raton)
        gato = mover_gato_minimax(gato, raton) 
        
        if raton == gato:
            limpiar_pantalla()
            imprimir_tablero(raton, gato)
            print("\n!El gato atrapo al raton! 🐱🗿")
            break
        # Alterna el turno
        turn = "Raton"
        
    turno_num +=1 

if turno_num > MAX_TURNOS:
    print("\nFin por turnos: !empate tecnico!")

