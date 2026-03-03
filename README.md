🐭🐱 Proyecto: Gato y Ratón - IA con Minimax
Este proyecto es un simulador de persecución basado en consola donde un jugador controla a un ratón que intenta escapar hacia una salida, mientras que la computadora controla a un gato con inteligencia artificial.

📖 Descripción
El juego se desarrolla en un tablero bidimensional (matriz) con obstáculos. El objetivo del ratón es llegar al emoji de la puerta (🚪) antes de ser capturado por el gato. El gato no solo te sigue, sino que utiliza algoritmos de búsqueda para anticipar tus movimientos.

🛠️ Tecnologías Utilizadas
Lenguaje: Python 3

Librerías: os (para manipulación de la terminal/consola).

Conceptos clave: Matrices, Tuplas, Diccionarios y Algoritmos de IA.

🧠 Lógica y Algoritmos (Paso a Paso)
Este proyecto destaca por el uso de dos estrategias para el enemigo (el gato):

Estrategia Greedy (Codiciosa): El gato calcula la distancia Manhattan hacia el ratón y elige el movimiento que más reduce esa distancia en el siguiente turno.

Algoritmo Minimax: * Es el corazón del proyecto. El gato "imagina" el futuro hasta 4 turnos adelante.

Simula tanto sus mejores movimientos como los posibles movimientos de escape del jugador.

Evaluación: Asigna puntajes (100 si atrapa al ratón, -100 si el ratón escapa) para decidir la ruta óptima.

Sistema de Renderizado: El tablero se limpia y se redibuja en cada turno para crear una sensación de animación en la consola, utilizando una lógica de "copia y reemplazo" para no dañar el mapa original.

🚀 Cómo Ejecutarlo
Asegúrate de tener Python instalado.

Guarda el código en un archivo llamado gato_raton.py.

Ejecuta en tu terminal:

Bash
python gato_raton.py
Usa las teclas W, A, S, D para mover al ratón.
