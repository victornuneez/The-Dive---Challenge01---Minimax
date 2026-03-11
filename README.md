# 🐭😺 Proyecto: Gato y Ratón — IA con Minimax

Este proyecto es un **simulador de persecución** basado en consola. El jugador controla a un ratón que intenta escapar hacia una salida, mientras que la computadora controla a un gato potenciado por inteligencia artificial.

## 📖 Descripción del Juego

El juego se desarrolla en un tablero bidimensional (matriz) con obstáculos. 

* **Objetivo del Ratón:** Llegar a la salida (**🚪**) antes de ser capturado.
* **Objetivo del Gato:** Anticipar los movimientos del jugador y capturarlo.

El gato no solo te sigue; utiliza algoritmos de búsqueda para "pensar" cuál es su mejor jugada según el estado del tablero.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías:** `os` (para la manipulación y limpieza de la terminal).
* **Conceptos Clave:** * Estructuras de datos (Matrices, Tuplas, Diccionarios).
    * Recursividad para algoritmos de IA.
    * Copia profunda de estados de juego para simulación.

---

## 🧠 Lógica y Algoritmos (IA)

Este proyecto destaca por implementar dos niveles de dificultad o estrategias para el enemigo:

### 1. Estrategia Greedy (Codiciosa)
El gato calcula la **distancia Manhattan** hacia el ratón en cada paso y elige el movimiento inmediato que más reduce esa distancia. Es eficiente pero "miope", ya que no prevé obstáculos a largo plazo.

### 2. Algoritmo Minimax (Inteligencia Real)
Es el componente más avanzado del proyecto. El gato "imagina" el futuro mediante un árbol de decisión:



* **Profundidad:** Analiza hasta **4 turnos adelante**.
* **Simulación:** Evalúa tanto sus mejores movimientos como los posibles movimientos de escape del jugador.
* **Evaluación:** Asigna valores críticos (ej: `+100` si atrapa al ratón, `-100` si el ratón escapa) para decidir la ruta óptima.

### 🖥️ Sistema de Renderizado
El tablero utiliza una lógica de **limpieza y redibujo** (`os.system('cls'/'clear')`) en cada turno. Esto crea una experiencia fluida de "animación" en la consola, utilizando una técnica de copia del mapa base para no degradar el escenario original con los movimientos.

---

## 🚀 Cómo Ejecutarlo

1.  **Requisito:** Tener Python 3 instalado.
2.  **Preparación:** Guarda el código en un archivo llamado `gato_raton.py`.
3.  **Lanzamiento:** Ejecuta el siguiente comando en tu terminal:
    ```bash
    python gato_raton.py
    ```

### 🎮 Controles
Mueve al ratón usando las teclas de dirección clásicas:
* **W**: Arriba
* **A**: Izquierda
* **S**: Abajo
* **D**: Derecha
