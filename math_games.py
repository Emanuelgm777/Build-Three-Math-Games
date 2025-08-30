import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
import sympy as sp
from ipywidgets import interactive
import ipywidgets as widgets

# Scatter Plot Game
def scatter_plot_game():
    # Generar un punto aleatorio en el gráfico
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    
    print(f"Intenta adivinar las coordenadas del punto ({x}, {y}) en el gráfico.")
    
    # Crear un gráfico
    plt.figure(figsize=(6,6))
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)
    plt.scatter(x, y, c='r', label='Punto a adivinar')
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True)
    plt.legend()
    plt.title("Scatter Plot Game")
    plt.show()
    
    # Pedir al jugador las coordenadas
    guess_x = int(input("¿Cuál es el valor de x?: "))
    guess_y = int(input("¿Cuál es el valor de y?: "))
    
    if guess_x == x and guess_y == y:
        print("¡Correcto! Has adivinado las coordenadas.")
    else:
        print(f"Incorrecto. Las coordenadas correctas eran ({x}, {y}).")

# Algebra Practice Game
def algebra_practice_game():
    # Generar aleatoriamente una pregunta de álgebra
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    operation = random.choice(["+", "-"])
    
    if operation == "+":
        print(f"Resuelve la ecuación: {a}x + {b} = {c}")
        answer = (c - b) / a
    else:
        print(f"Resuelve la ecuación: {a}x - {b} = {c}")
        answer = (c + b) / a
    
    guess = float(input("¿Cuál es tu respuesta para x?: "))
    
    if np.isclose(guess, answer, atol=0.1):
        print("¡Correcto!")
    else:
        print(f"Incorrecto. La respuesta correcta es x = {answer:.2f}.")

# Projectile Game
def projectile_game():
    # Definir el rango de parámetros de la trayectoria
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(-10, 10)
    
    print(f"Te toca ajustar la parábola y hacerla pasar por encima del muro con altura aleatoria.")
    
    # Crear el muro aleatorio
    wall_height = random.randint(5, 10)
    wall_position = random.randint(-10, 10)
    
    print(f"El muro tiene altura {wall_height} en la posición x = {wall_position}.")
    
    # Crear la trayectoria parabólica
    x_vals = np.linspace(-15, 15, 400)
    y_vals = a*x_vals**2 + b*x_vals + c
    
    plt.figure(figsize=(6,6))
    plt.xlim(-15, 15)
    plt.ylim(-10, 15)
    plt.plot(x_vals, y_vals, label="Trayectoria Parabólica")
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.fill_between(x_vals, y_vals, where=(y_vals > wall_height), color='lightgreen', alpha=0.5)
    
    plt.plot(wall_position, wall_height, marker='o', markersize=10, color='r', label='Muro')
    plt.legend()
    plt.title("Projectile Game")
    plt.grid(True)
    plt.show()
    
    # Permitir al jugador mover los controles deslizantes para ajustar la trayectoria
    def update_parabola(a_slider, b_slider, c_slider):
        y_vals_new = a_slider*x_vals**2 + b_slider*x_vals + c_slider
        plt.figure(figsize=(6,6))
        plt.xlim(-15, 15)
        plt.ylim(-10, 15)
        plt.plot(x_vals, y_vals_new, label="Trayectoria Ajustada")
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.fill_between(x_vals, y_vals_new, where=(y_vals_new > wall_height), color='lightgreen', alpha=0.5)
        plt.plot(wall_position, wall_height, marker='o', markersize=10, color='r', label='Muro')
        plt.legend()
        plt.title("Projectile Game - Ajustando la Trayectoria")
        plt.grid(True)
        plt.show()
    
    # Controles deslizantes
    interactive(update_parabola, a_slider=widgets.FloatSlider(min=-10, max=10, step=0.1, value=a),
                                    b_slider=widgets.FloatSlider(min=-10, max=10, step=0.1, value=b),
                                    c_slider=widgets.FloatSlider(min=-10, max=10, step=0.1, value=c))

# Iniciar los juegos
def main():
    print("¡Bienvenido a los tres juegos matemáticos!")
    print("1. Scatter Plot Game")
    print("2. Algebra Practice Game")
    print("3. Projectile Game")
    choice = int(input("Selecciona un juego (1, 2, 3): "))
    
    if choice == 1:
        scatter_plot_game()
    elif choice == 2:
        algebra_practice_game()
    elif choice == 3:
        projectile_game()
    else:
        print("Selección no válida.")

# Ejecutar el juego
main()
