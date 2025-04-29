import matplotlib.pyplot as plt
import numpy as np

def jacobi(A, b, eps=0.01, max_iterations=1000):
    n = len(A)
    x = [0.0 for _ in range(n)]
    x_new = x.copy()
    history = [x.copy()]

    for iteration in range(max_iterations):
        for i in range(n):
            sum_ = 0.0
            for j in range(n):
                if j != i:
                    sum_ += A[i][j] * x[j]
            x_new[i] = (b[i] - sum_) / A[i][i]

        history.append(x_new.copy())

        converged = True
        for i in range(n):
            if abs(x_new[i] - x[i]) > eps:
                converged = False
                break

        if converged:
            print(f"Метод Якоби: решение найдено за {iteration + 1} итераций")
            return x_new, history

        x = x_new.copy()

    print("Метод Якоби: достигнуто максимальное количество итераций")
    return x, history

def seidel(A, b, eps=0.01, max_iterations=1000):
    n = len(A)
    x = [0.0 for _ in range(n)]
    history = [x.copy()]

    for iteration in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]

        history.append(x_new.copy())

        converged = True
        for i in range(n):
            if abs(x_new[i] - x[i]) > eps:
                converged = False
                break

        if converged:
            print(f"Метод Зейделя: решение найдено за {iteration + 1} итераций")
            return x_new, history

        x = x_new.copy()

    print("Метод Зейделя: достигнуто максимальное количество итераций")
    return x, history

A = [
    [5, 2, -1],
    [-4, 7, 3],
    [2, -2, 4]
]
b = [12, 24, 9]

jacobi_solution, jacobi_history = jacobi(A, b)
seidel_solution, seidel_history = seidel(A, b)

print("\nРешение методом Якоби:", jacobi_solution)
print("Решение методом Зейделя:", seidel_solution)

plt.figure(figsize=(12, 8))

plt.subplot(1, 2, 1)
jacobi_history = np.array(jacobi_history)
for i in range(3):
    plt.plot(jacobi_history[:, i], label=f'$x_{i + 1}$', marker='o', linestyle='-')
plt.xlabel('Итерации')
plt.ylabel('Значение переменной')
plt.title('Метод Якоби: изменение значений $x_1, x_2, x_3$')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
seidel_history = np.array(seidel_history)
for i in range(3):
    plt.plot(seidel_history[:, i], label=f'$x_{i + 1}$', marker='s', linestyle='--')
plt.xlabel('Итерации')
plt.ylabel('Значение переменной')
plt.title('Метод Зейделя: изменение значений $x_1, x_2, x_3$')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()