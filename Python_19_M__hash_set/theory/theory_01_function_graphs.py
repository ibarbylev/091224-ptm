"""pip install numpy matplotlib PyQt5"""

import numpy as np
import matplotlib.pyplot as plt

# Создаём диапазон значений x
x = np.linspace(-10, 10, 400)
x_nonzero = x[x != 0]  # Исключаем ноль для функции y = 1/x

# Вычисляем значения функций
y1 = x
y2 = x ** 2
y3 = 1 / x_nonzero
y4 = [hash(xi) for xi in x]  # Используем хеш-функцию
y4_normalized = np.array(y4) % 10000  # Нормализуем значения хеша для визуализации

# Создаём фигуру и оси для трёх функций
plt.figure(figsize=(10, 8))

# График y = x
plt.subplot(3, 1, 1)
plt.plot(x, y1, label='y = x', color='blue')
plt.title('y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# График y = x^2
plt.subplot(3, 1, 2)
plt.plot(x, y2, label='y = x^2', color='green')
plt.scatter(0, 0, color='red', zorder=5)  # Точка минимума
plt.title('y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# График y = 1/x
plt.subplot(3, 1, 3)
plt.plot(x_nonzero, y3, label='y = 1/x', color='red')
plt.title('y = 1/x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Настраиваем макет и отображаем графики
plt.tight_layout()
plt.show()

# Создаём фигуру для функции y = hash(x)
plt.figure(figsize=(10, 4))
plt.scatter(x, y4_normalized, label='y = hash(x) % 10000', color='purple', s=10)
plt.title('y = hash(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
