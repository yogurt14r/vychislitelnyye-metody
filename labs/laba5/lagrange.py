import numpy as np
import matplotlib.pyplot as plt

# Функция, которую интерполируем
def f(x):
    return np.sin(x)

# Функция для построения многочлена Лагранжа
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Узлы интерполяции: 3 и 5 точек, равномерно на [0, π]
x_nodes_3 = np.linspace(0, np.pi, 3)
y_nodes_3 = f(x_nodes_3)

x_nodes_5 = np.linspace(0, np.pi, 5)
y_nodes_5 = f(x_nodes_5)

# Точки для построения графика
x_plot = np.linspace(0, np.pi, 500)
y_true = f(x_plot)

# Вычисляем интерполяции
y_interp_3 = [lagrange_interpolation(x, x_nodes_3, y_nodes_3) for x in x_plot]
y_interp_5 = [lagrange_interpolation(x, x_nodes_5, y_nodes_5) for x in x_plot]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_true, label='sin(x)', color='black', linewidth=2)
plt.plot(x_plot, y_interp_3, label='Интерполяция 3 точки', linestyle='--')
plt.plot(x_plot, y_interp_5, label='Интерполяция 5 точек', linestyle=':')
plt.scatter(x_nodes_3, y_nodes_3, color='blue', label='Узлы (3 точки)')
plt.scatter(x_nodes_5, y_nodes_5, color='red', label='Узлы (5 точек)', marker='x')
plt.title('Интерполяция функции sin(x) многочленами Лагранжа')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
